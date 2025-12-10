#!/usr/bin/env python3
"""
Database Migration Script for OTP Authentication
Adds OTP functionality to existing King Salomon Academy database
"""

import os
import sys
from datetime import datetime

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app, db, User, OTPCode

def migrate_database():
    """Add OTP tables and update existing users"""
    with app.app_context():
        print("🔄 Starting database migration for OTP authentication...")
        
        # Create OTP table
        try:
            db.create_all()
            print("✅ OTP tables created successfully")
        except Exception as e:
            print(f"❌ Error creating OTP tables: {e}")
            return False
        
        # Update existing users to be verified (for existing accounts)
        try:
            existing_users = User.query.filter_by(is_verified=None).all()
            for user in existing_users:
                user.is_verified = True
            
            # Add phone_number column if it doesn't exist
            try:
                # This will work if the column exists, fail if it doesn't
                User.query.filter(User.phone_number.isnot(None)).first()
            except:
                # Column doesn't exist, we need to add it
                print("📱 Adding phone_number column to User table...")
                # For SQLite, we need to recreate the table
                db.engine.execute('ALTER TABLE user ADD COLUMN phone_number VARCHAR(20)')
                print("✅ phone_number column added")
            
            db.session.commit()
            print(f"✅ Updated {len(existing_users)} existing users to verified status")
        except Exception as e:
            print(f"⚠️  Warning: Could not update existing users: {e}")
            db.session.rollback()
        
        # Clean up expired OTP codes
        try:
            expired_codes = OTPCode.query.filter(OTPCode.expires_at < datetime.utcnow()).all()
            for code in expired_codes:
                db.session.delete(code)
            db.session.commit()
            print(f"🧹 Cleaned up {len(expired_codes)} expired OTP codes")
        except Exception as e:
            print(f"⚠️  Warning: Could not clean up expired codes: {e}")
            db.session.rollback()
        
        print("🎉 Database migration completed successfully!")
        print("\n📋 OTP Authentication Features Added:")
        print("   • Email verification for registration")
        print("   • SMS verification (optional)")
        print("   • Login OTP verification")
        print("   • Secure 6-digit codes with expiration")
        print("   • Rate limiting (3 attempts per code)")
        print("   • Development mode (console display)")
        
        return True

def create_test_admin():
    """Create a test admin user for OTP testing"""
    with app.app_context():
        try:
            # Check if admin already exists
            admin = User.query.filter_by(username='admin').first()
            if admin:
                print("👤 Admin user already exists")
                return admin
            
            # Create new admin
            admin = User(
                username='admin',
                email='admin@kingsalomon.ac.rw',
                phone_number='+250123456789',
                full_name='King Salomon Academy Admin',
                role='admin',
                is_verified=True
            )
            admin.set_password('admin123')
            
            db.session.add(admin)
            db.session.commit()
            
            print("✅ Test admin user created:")
            print(f"   Username: admin")
            print(f"   Password: admin123")
            print(f"   Email: admin@kingsalomon.ac.rw")
            print(f"   Phone: +250123456789")
            
            return admin
        except Exception as e:
            print(f"❌ Error creating admin user: {e}")
            db.session.rollback()
            return None

if __name__ == '__main__':
    print("🎓 King Salomon Academy - OTP Authentication Setup")
    print("=" * 60)
    
    # Run migration
    if migrate_database():
        print("\n" + "=" * 60)
        print("🔧 Creating test admin user...")
        create_test_admin()
        
        print("\n" + "=" * 60)
        print("🚀 OTP Authentication Setup Complete!")
        print("\n📖 How to test:")
        print("1. Start the application: python app.py")
        print("2. Go to http://localhost:5000/register")
        print("3. Register a new account")
        print("4. Check the console for OTP code")
        print("5. Enter the code to verify your account")
        print("6. Login with your credentials")
        print("7. Check console again for login OTP")
        print("\n🔒 Security Features:")
        print("• Codes expire in 10 minutes")
        print("• Maximum 3 attempts per code")
        print("• Codes sent via email and SMS")
        print("• Development mode shows codes in console")
    else:
        print("❌ Migration failed!")
        sys.exit(1)
