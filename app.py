from flask import Flask, render_template, request, redirect, url_for, flash, send_file, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_mail import Mail, Message
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os
from datetime import datetime, timedelta
import uuid
from PIL import Image
import mimetypes
import pyotp
import qrcode
import io
import base64
import requests
import random
import string

app = Flask(__name__)

# Load configuration from environment variables
app.config['SECRET_KEY'] = os.environ.get(
    'SECRET_KEY', 'king-salomon-academy-2024')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', 'sqlite:///academy_media.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = os.environ.get('UPLOAD_FOLDER', 'static/uploads')
app.config['MAX_CONTENT_LENGTH'] = int(
    os.environ.get('MAX_CONTENT_LENGTH', 500 * 1024 * 1024))

# Email configuration for OTP
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
app.config['MAIL_PORT'] = int(os.environ.get('MAIL_PORT', 587))
app.config['MAIL_USE_TLS'] = os.environ.get(
    'MAIL_USE_TLS', 'True').lower() == 'true'
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME', '')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD', '')

# SMS configuration for OTP
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID', '')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN', '')
TWILIO_PHONE_NUMBER = os.environ.get('TWILIO_PHONE_NUMBER', '')

# Production security settings
if os.environ.get('FLASK_ENV') == 'production':
    app.config['SESSION_COOKIE_SECURE'] = True
    app.config['SESSION_COOKIE_HTTPONLY'] = True
    app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(os.path.join(app.config['UPLOAD_FOLDER'], 'images'), exist_ok=True)
os.makedirs(os.path.join(app.config['UPLOAD_FOLDER'], 'videos'), exist_ok=True)

db = SQLAlchemy(app)
mail = Mail(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Database Models


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(20), nullable=True)
    password_hash = db.Column(db.String(120), nullable=False)
    # student, teacher, admin
    role = db.Column(db.String(20), default='student')
    full_name = db.Column(db.String(100), nullable=False)
    is_verified = db.Column(db.Boolean, default=False)
    # 'pending', 'approved', 'rejected'
    approval_status = db.Column(db.String(20), default='approved')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class OTPCode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    phone_number = db.Column(db.String(20), nullable=True)
    code = db.Column(db.String(6), nullable=False)
    # 'registration', 'login', 'password_reset'
    purpose = db.Column(db.String(20), nullable=False)
    expires_at = db.Column(db.DateTime, nullable=False)
    is_used = db.Column(db.Boolean, default=False)
    attempts = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def is_expired(self):
        return datetime.utcnow() > self.expires_at

    def is_valid(self):
        return not self.is_used and not self.is_expired() and self.attempts < 3


class MediaFile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    original_filename = db.Column(db.String(255), nullable=False)
    file_type = db.Column(db.String(50), nullable=False)  # image, video
    file_size = db.Column(db.BigInteger, nullable=False)
    file_path = db.Column(db.String(500), nullable=False)
    uploaded_by = db.Column(
        db.Integer, db.ForeignKey('user.id'), nullable=False)
    category = db.Column(db.String(100), default='general')
    description = db.Column(db.Text)
    upload_date = db.Column(db.DateTime, default=datetime.utcnow)
    is_public = db.Column(db.Boolean, default=True)

    uploader = db.relationship('User', backref='uploaded_files')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# OTP Utility Functions


def generate_otp_code():
    """Generate a 6-digit OTP code"""
    return ''.join(random.choices(string.digits, k=6))


def send_email_otp(email, code, purpose):
    """Send OTP code via email"""
    try:
        # Always show OTP in console for development/testing
        print(f"\n🔐 OTP CODE FOR {email.upper()}: {code}")
        print(f"📧 Email would be sent to: {email}")
        print(f"🎯 Purpose: {purpose}")
        print("=" * 50)

        # Development mode - show OTP in console
        if os.environ.get('FLASK_ENV') == 'development' or not app.config['MAIL_USERNAME']:
            return True

        if purpose == 'registration':
            subject = "King Salomon Academy - Email Verification"
            body = f"""
            <html>
            <body style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
                <div style="background: linear-gradient(135deg, #2c3e50, #3498db); color: white; padding: 20px; text-align: center;">
                    <h1>🎓 King Salomon Academy</h1>
                    <h2>Email Verification</h2>
                </div>
                <div style="padding: 30px; background: #f8f9fa;">
                    <h3>Welcome to King Salomon Academy!</h3>
                    <p>Thank you for registering with our media management system. To complete your registration, please use the verification code below:</p>
                    
                    <div style="background: #e3f2fd; border: 2px solid #2196f3; border-radius: 10px; padding: 20px; text-align: center; margin: 20px 0;">
                        <h2 style="color: #1976d2; font-size: 32px; margin: 0; letter-spacing: 5px;">{code}</h2>
                    </div>
                    
                    <p><strong>This code will expire in 10 minutes.</strong></p>
                    <p>If you didn't request this verification, please ignore this email.</p>
                    
                    <hr style="margin: 30px 0; border: none; border-top: 1px solid #ddd;">
                    <p style="color: #666; font-size: 14px;">
                        King Salomon Academy<br>
                        Gicumbi District, Rwanda<br>
                        Media Management System
                    </p>
                </div>
            </body>
            </html>
            """
        elif purpose == 'login':
            subject = "King Salomon Academy - Login Verification"
            body = f"""
            <html>
            <body style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
                <div style="background: linear-gradient(135deg, #2c3e50, #3498db); color: white; padding: 20px; text-align: center;">
                    <h1>🎓 King Salomon Academy</h1>
                    <h2>Login Verification</h2>
                </div>
                <div style="padding: 30px; background: #f8f9fa;">
                    <h3>Security Verification</h3>
                    <p>Someone is trying to log into your King Salomon Academy account. If this is you, use the verification code below:</p>
                    
                    <div style="background: #e8f5e8; border: 2px solid #4caf50; border-radius: 10px; padding: 20px; text-align: center; margin: 20px 0;">
                        <h2 style="color: #2e7d32; font-size: 32px; margin: 0; letter-spacing: 5px;">{code}</h2>
                    </div>
                    
                    <p><strong>This code will expire in 10 minutes.</strong></p>
                    <p>If you didn't request this login, please secure your account immediately.</p>
                    
                    <hr style="margin: 30px 0; border: none; border-top: 1px solid #ddd;">
                    <p style="color: #666; font-size: 14px;">
                        King Salomon Academy<br>
                        Gicumbi District, Rwanda<br>
                        Media Management System
                    </p>
                </div>
            </body>
            </html>
            """

        msg = Message(subject, recipients=[email])
        msg.html = body
        mail.send(msg)
        return True
    except Exception as e:
        print(f"Email sending failed: {e}")
        return False


def send_sms_otp(phone_number, code, purpose):
    """Send OTP code via SMS using Twilio"""
    try:
        # Always show OTP in console for development/testing
        print(f"\n📱 SMS OTP CODE FOR {phone_number}: {code}")
        print(f"📞 SMS would be sent to: {phone_number}")
        print(f"🎯 Purpose: {purpose}")
        print("=" * 50)

        # Development mode - show OTP in console
        if os.environ.get('FLASK_ENV') == 'development' or not TWILIO_ACCOUNT_SID:
            return True

        from twilio.rest import Client
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        if purpose == 'registration':
            message_body = f"King Salomon Academy: Your verification code is {code}. This code expires in 10 minutes. Do not share this code."
        elif purpose == 'login':
            message_body = f"King Salomon Academy: Your login verification code is {code}. This code expires in 10 minutes. Do not share this code."

        message = client.messages.create(
            body=message_body,
            from_=TWILIO_PHONE_NUMBER,
            to=phone_number
        )
        return True
    except Exception as e:
        print(f"SMS sending failed: {e}")
        return False


def create_otp_code(email, phone_number=None, purpose='registration'):
    """Create and send OTP code"""
    # Generate 6-digit code
    code = generate_otp_code()

    # Set expiration time (10 minutes)
    expires_at = datetime.utcnow() + timedelta(minutes=10)

    # Invalidate any existing codes for this email/purpose
    OTPCode.query.filter_by(email=email, purpose=purpose,
                            is_used=False).update({'is_used': True})

    # Create new OTP record
    otp_record = OTPCode(
        email=email,
        phone_number=phone_number,
        code=code,
        purpose=purpose,
        expires_at=expires_at
    )

    db.session.add(otp_record)
    db.session.commit()

    # Send via email
    email_sent = send_email_otp(email, code, purpose)

    # Send via SMS if phone number provided
    sms_sent = False
    if phone_number:
        sms_sent = send_sms_otp(phone_number, code, purpose)

    return {
        'success': True,  # Proceed to verification even if delivery fails
        'email_sent': email_sent,
        'sms_sent': sms_sent,
        'code': code  # For testing and console display
    }


def verify_otp_code(email, code, purpose='registration'):
    """Verify OTP code"""
    otp_record = OTPCode.query.filter_by(
        email=email,
        purpose=purpose,
        is_used=False
    ).order_by(OTPCode.created_at.desc()).first()

    if not otp_record:
        return False, "No OTP code found"

    if otp_record.is_expired():
        otp_record.is_used = True
        db.session.commit()
        return False, "OTP code has expired"

    if otp_record.attempts >= 3:
        otp_record.is_used = True
        db.session.commit()
        return False, "Too many failed attempts"

    if otp_record.code != code:
        otp_record.attempts += 1
        db.session.commit()
        return False, f"Invalid code. {3 - otp_record.attempts} attempts remaining"

    # Code is valid
    otp_record.is_used = True
    db.session.commit()
    return True, "OTP verified successfully"

# Routes


@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(f"DEBUG: Login attempt for username: {username}")
        user = User.query.filter_by(username=username).first()

        if user:
            print(f"DEBUG: User found: {user.username}")
            if user.check_password(password):
                print(f"DEBUG: Password correct for {user.username}")
                # Block login if not approved
                if getattr(user, 'approval_status', 'approved') != 'approved':
                    if user.approval_status == 'pending':
                        flash('Your account is awaiting admin approval.', 'warning')
                    elif user.approval_status == 'rejected':
                        flash('Your login is rejected by admin. Contact support.', 'danger')
                    else:
                        flash('Your account is not approved yet.', 'warning')
                    return render_template('login.html')
                # OTP disabled: log user in directly
                login_user(user)
                flash(f'Welcome back, {user.full_name}!', 'success')
                return redirect(url_for('dashboard'))
            else:
                flash('Invalid password', 'error')
        else:
            flash('Username not found', 'error')

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        full_name = request.form['full_name']
        phone_number = request.form.get('phone_number', '')
        role = request.form.get('role', 'student')

        # Validate required fields
        if not username or not email or not password or not full_name:
            flash('All fields are required', 'error')
            return render_template('register.html')

        # Check if username already exists
        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'error')
            return render_template('register.html')

        # Check if email already exists
        if User.query.filter_by(email=email).first():
            flash('Email already exists', 'error')
            return render_template('register.html')

        try:
            # Create new user (not verified yet)
            user = User(
                username=username,
                email=email,
                full_name=full_name,
                phone_number=phone_number,
                role=role,
                # OTP disabled: mark verified immediately
                is_verified=True,
                # New accounts require admin approval to login
                approval_status='pending'
            )
            user.set_password(password)
            db.session.add(user)
            db.session.commit()

            # OTP disabled: registration completes immediately
            flash('Registration successful! Waiting for admin approval before you can login.', 'info')
            return redirect(url_for('login'))

        except Exception as e:
            db.session.rollback()
            flash(f'Registration failed: {str(e)}', 'error')
            return render_template('register.html')

    return render_template('register.html')


@app.route('/verify-otp/<purpose>', methods=['GET', 'POST'])
def verify_otp(purpose):
    # OTP disabled: redirect away from this route
    flash('OTP verification is disabled. Please login directly.', 'info')
    return redirect(url_for('login'))


@app.route('/resend-otp', methods=['POST'])
def resend_otp():
    # OTP disabled: do nothing
    flash('OTP verification is disabled. No code was sent.', 'info')
    return redirect(url_for('login'))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/dashboard')
@login_required
def dashboard():
    # Get user's files and public files
    user_files = MediaFile.query.filter_by(
        uploaded_by=current_user.id).order_by(MediaFile.upload_date.desc()).all()
    public_files = MediaFile.query.filter_by(is_public=True).order_by(
        MediaFile.upload_date.desc()).limit(20).all()

    # Get file statistics
    total_files = MediaFile.query.count()
    user_file_count = len(user_files)
    total_size = sum(f.file_size for f in MediaFile.query.all())

    return render_template('dashboard.html',
                           user_files=user_files,
                           public_files=public_files,
                           total_files=total_files,
                           user_file_count=user_file_count,
                           total_size=total_size)


@app.route('/upload', methods=['POST'])
@login_required
def upload_file():
    if 'file' not in request.files:
        flash('No file selected', 'error')
        return redirect(url_for('dashboard'))

    file = request.files['file']
    if file.filename == '':
        flash('No file selected', 'error')
        return redirect(url_for('dashboard'))

    if file:
        # Generate unique filename
        file_extension = os.path.splitext(file.filename)[1].lower()
        unique_filename = str(uuid.uuid4()) + file_extension
        original_filename = secure_filename(file.filename)

        # Determine file type and folder
        if file_extension in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp']:
            file_type = 'image'
            folder = 'images'
        elif file_extension in ['.mp4', '.avi', '.mov', '.wmv', '.flv', '.webm', '.mkv']:
            file_type = 'video'
            folder = 'videos'
        else:
            flash('Unsupported file type', 'error')
            return redirect(url_for('dashboard'))

        # Save file
        file_path = os.path.join(
            app.config['UPLOAD_FOLDER'], folder, unique_filename)
        file.save(file_path)

        # Get file size
        file_size = os.path.getsize(file_path)

        # Create database record
        media_file = MediaFile(
            filename=unique_filename,
            original_filename=original_filename,
            file_type=file_type,
            file_size=file_size,
            file_path=file_path,
            uploaded_by=current_user.id,
            category=request.form.get('category', 'general'),
            description=request.form.get('description', ''),
            is_public=request.form.get('is_public') == 'on'
        )

        db.session.add(media_file)
        db.session.commit()

        flash('File uploaded successfully!', 'success')

    return redirect(url_for('dashboard'))


@app.route('/download/<int:file_id>')
@login_required
def download_file(file_id):
    media_file = MediaFile.query.get_or_404(file_id)

    # Check if user can access the file
    if not media_file.is_public and media_file.uploaded_by != current_user.id:
        flash('You do not have permission to download this file', 'error')
        return redirect(url_for('dashboard'))

    return send_file(media_file.file_path, as_attachment=True, download_name=media_file.original_filename)


@app.route('/preview/<int:file_id>')
@login_required
def preview_file(file_id):
    media_file = MediaFile.query.get_or_404(file_id)

    # Check if user can access the file
    if not media_file.is_public and media_file.uploaded_by != current_user.id:
        flash('You do not have permission to preview this file', 'error')
        return redirect(url_for('dashboard'))

    return send_file(media_file.file_path, as_attachment=False)


@app.route('/delete/<int:file_id>')
@login_required
def delete_file(file_id):
    media_file = MediaFile.query.get_or_404(file_id)

    # Check if user can delete the file
    if media_file.uploaded_by != current_user.id and current_user.role != 'admin':
        flash('You do not have permission to delete this file', 'error')
        return redirect(url_for('dashboard'))

    # Delete file from filesystem
    if os.path.exists(media_file.file_path):
        os.remove(media_file.file_path)

    # Delete from database
    db.session.delete(media_file)
    db.session.commit()

    flash('File deleted successfully!', 'success')
    return redirect(url_for('dashboard'))


@app.route('/admin')
@login_required
def admin_panel():
    if current_user.role != 'admin':
        flash('Access denied', 'error')
        return redirect(url_for('dashboard'))

    users = User.query.all()
    all_files = MediaFile.query.order_by(MediaFile.upload_date.desc()).all()

    # Calculate detailed statistics
    total_users = len(users)
    total_files = len(all_files)
    total_size = sum(f.file_size for f in all_files)
    image_count = len([f for f in all_files if f.file_type == 'image'])
    video_count = len([f for f in all_files if f.file_type == 'video'])
    public_count = len([f for f in all_files if f.is_public])

    return render_template('admin.html',
                           users=users,
                           files=all_files,
                           total_users=total_users,
                           total_files=total_files,
                           total_size=total_size,
                           image_count=image_count,
                           video_count=video_count,
                           public_count=public_count)


@app.route('/admin/users/<int:user_id>/approve')
@login_required
def approve_user(user_id):
    if current_user.role != 'admin':
        flash('Access denied', 'error')
        return redirect(url_for('dashboard'))
    user = User.query.get_or_404(user_id)
    user.approval_status = 'approved'
    db.session.commit()
    flash(f"Approved {user.full_name} for login.", 'success')
    return redirect(url_for('admin_panel'))


@app.route('/admin/users/<int:user_id>/reject')
@login_required
def reject_user(user_id):
    if current_user.role != 'admin':
        flash('Access denied', 'error')
        return redirect(url_for('dashboard'))
    user = User.query.get_or_404(user_id)
    user.approval_status = 'rejected'
    db.session.commit()
    flash(f"Rejected {user.full_name}'s login.", 'warning')
    return redirect(url_for('admin_panel'))


@app.route('/admin/users/<int:user_id>/pending')
@login_required
def pending_user(user_id):
    if current_user.role != 'admin':
        flash('Access denied', 'error')
        return redirect(url_for('dashboard'))
    user = User.query.get_or_404(user_id)
    user.approval_status = 'pending'
    db.session.commit()
    flash(f"Set {user.full_name} back to pending.", 'info')
    return redirect(url_for('admin_panel'))


@app.route('/admin/users/<int:user_id>/delete', methods=['POST'])
@login_required
def delete_user(user_id):
    if current_user.role != 'admin':
        flash('Access denied', 'error')
        return redirect(url_for('dashboard'))
    user = User.query.get_or_404(user_id)
    if user.id == current_user.id:
        flash('You cannot delete your own account while logged in.', 'warning')
        return redirect(url_for('admin_panel'))
    try:
        # Delete user's files from filesystem and database
        user_files = MediaFile.query.filter_by(uploaded_by=user.id).all()
        for f in user_files:
            try:
                if os.path.exists(f.file_path):
                    os.remove(f.file_path)
            except Exception:
                pass
            db.session.delete(f)
        # Finally delete the user
        db.session.delete(user)
        db.session.commit()
        flash('User and their files deleted.', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Failed to delete user: {e}', 'error')
    return redirect(url_for('admin_panel'))


if __name__ == '__main__':
    with app.app_context():
        # Ensure schema has latest columns before any ORM queries
        try:
            result = db.session.execute(db.text("PRAGMA table_info(user)"))
            columns = [row[1] for row in result.fetchall()]
            if 'approval_status' not in columns:
                db.session.execute(db.text("ALTER TABLE user ADD COLUMN approval_status VARCHAR(20)"))
                db.session.commit()
                db.session.execute(db.text("UPDATE user SET approval_status = 'approved' WHERE approval_status IS NULL"))
                db.session.commit()
        except Exception as e:
            print(f"Startup schema migration note (may be safe to ignore if non-SQLite/already applied): {e}")

        db.create_all()

        # Create admin user if it doesn't exist
        admin = User.query.filter_by(username='admin').first()
        if not admin:
            admin = User(username='admin', email='admin@kingsalomon.ac.rw',
                         full_name='System Administrator', role='admin')
            admin.set_password('admin123')
            db.session.add(admin)
            db.session.commit()
            print("Admin user created: username='admin', password='admin123'")

    app.run(debug=True, host='0.0.0.0', port=5000)

# Ensure default admin exists even when running via WSGI or other entry points
@app.before_first_request
def ensure_default_admin():
    try:
        # Ensure schema exists and includes approval_status
        try:
            # For SQLite, check columns
            result = db.session.execute(db.text("PRAGMA table_info(user)"))
            columns = [row[1] for row in result.fetchall()]
            if 'approval_status' not in columns:
                db.session.execute(db.text("ALTER TABLE user ADD COLUMN approval_status VARCHAR(20)"))
                db.session.commit()
                # Default existing users to approved
                db.session.execute(db.text("UPDATE user SET approval_status = 'approved' WHERE approval_status IS NULL"))
                db.session.commit()
        except Exception as e:
            print(f"Schema check/add column failed (may be non-SQLite or already exists): {e}")
        db.create_all()
        admin = User.query.filter_by(username='admin').first()
        if not admin:
            admin = User(
                username='admin',
                email='admin@kingsalomon.ac.rw',
                full_name='System Administrator',
                role='admin',
                is_verified=True,
                approval_status='approved'
            )
            admin.set_password('admin123')
            db.session.add(admin)
            db.session.commit()
            print("Default admin ensured: username='admin', password='admin123'")
        else:
            changed = False
            if admin.role != 'admin':
                admin.role = 'admin'
                changed = True
            if getattr(admin, 'approval_status', 'approved') != 'approved':
                admin.approval_status = 'approved'
                changed = True
            if changed:
                db.session.commit()
                print("Updated existing 'admin' user to admin role and approved status")
    except Exception as e:
        print(f"Failed to ensure default admin: {e}")
