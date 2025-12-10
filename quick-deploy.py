#!/usr/bin/env python3
"""
King Salomon Academy - Quick Production Deployment
Simple deployment script for immediate use
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e.stderr}")
        return False

def create_directories():
    """Create necessary directories"""
    directories = [
        'logs',
        'static/uploads/images',
        'static/uploads/videos',
        'backups'
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"📁 Created directory: {directory}")

def setup_environment():
    """Setup environment configuration"""
    if not os.path.exists('.env'):
        if os.path.exists('env.example'):
            shutil.copy('env.example', '.env')
            print("📝 Created .env file from template")
            print("⚠️  Please edit .env file with your production settings!")
        else:
            # Create basic .env file
            with open('.env', 'w') as f:
                f.write("""# King Salomon Academy Configuration
FLASK_ENV=production
SECRET_KEY=change-this-secret-key-in-production
DATABASE_URL=sqlite:///academy_media.db
MAX_CONTENT_LENGTH=524288000
""")
            print("📝 Created basic .env file")

def install_dependencies():
    """Install production dependencies"""
    if os.path.exists('requirements-prod.txt'):
        return run_command('pip install -r requirements-prod.txt', 'Installing production dependencies')
    else:
        return run_command('pip install -r requirements.txt', 'Installing dependencies')

def initialize_database():
    """Initialize database"""
    try:
        from app import app, db, User
        
        with app.app_context():
            db.create_all()
            
            # Create admin user if it doesn't exist
            admin = User.query.filter_by(username='admin').first()
            if not admin:
                admin = User(
                    username='admin',
                    email='admin@kingsalomon.ac.rw',
                    full_name='System Administrator',
                    role='admin'
                )
                admin.set_password('admin123')
                db.session.add(admin)
                db.session.commit()
                print("✅ Admin user created")
            else:
                print("✅ Admin user already exists")
        
        return True
    except Exception as e:
        print(f"❌ Database initialization failed: {e}")
        return False

def create_startup_script():
    """Create startup script for production"""
    startup_script = """#!/bin/bash
# King Salomon Academy - Production Startup Script

echo "🎓 Starting King Salomon Academy Media System..."

# Set environment
export FLASK_ENV=production

# Start with Gunicorn if available, otherwise use Flask
if command -v gunicorn &> /dev/null; then
    echo "🚀 Starting with Gunicorn..."
    gunicorn --bind 0.0.0.0:8000 --workers 4 --timeout 30 wsgi:app
else
    echo "🚀 Starting with Flask development server..."
    python app.py
fi
"""
    
    with open('start-production.sh', 'w') as f:
        f.write(startup_script)
    
    # Make executable on Unix systems
    if os.name != 'nt':
        os.chmod('start-production.sh', 0o755)
    
    print("📝 Created production startup script")

def main():
    """Main deployment function"""
    print("🎓 King Salomon Academy - Quick Production Deployment")
    print("=" * 60)
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        sys.exit(1)
    
    # Create directories
    create_directories()
    
    # Setup environment
    setup_environment()
    
    # Install dependencies
    if not install_dependencies():
        print("❌ Failed to install dependencies")
        sys.exit(1)
    
    # Initialize database
    if not initialize_database():
        print("❌ Failed to initialize database")
        sys.exit(1)
    
    # Create startup script
    create_startup_script()
    
    print("\n" + "=" * 60)
    print("✅ DEPLOYMENT COMPLETED SUCCESSFULLY!")
    print("=" * 60)
    print()
    print("🚀 To start your application:")
    print("   python app.py")
    print()
    print("🌐 Access your system at:")
    print("   http://localhost:5000")
    print()
    print("👤 Admin login:")
    print("   Username: admin")
    print("   Password: admin123")
    print()
    print("⚠️  IMPORTANT SECURITY STEPS:")
    print("   1. Change the admin password immediately")
    print("   2. Edit .env file with secure settings")
    print("   3. Configure your domain name")
    print("   4. Set up SSL certificate for HTTPS")
    print("   5. Configure firewall rules")
    print()
    print("📚 For detailed deployment instructions, see DEPLOYMENT.md")
    print()
    print("🎉 Welcome to King Salomon Academy Media Management System!")

if __name__ == '__main__':
    main()
