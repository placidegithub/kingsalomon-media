#!/usr/bin/env python3
"""
King Salomon Academy - Simple Production Deployment
Works with existing dependencies
"""

import os
import sys
import shutil
from pathlib import Path

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
        
        print("⚠️  Please edit .env file with your production settings!")
    else:
        print("✅ .env file already exists")

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

def create_production_scripts():
    """Create production startup scripts"""
    
    # Windows batch file
    windows_script = """@echo off
echo.
echo ================================================
echo   King Salomon Academy - Production Server
echo ================================================
echo.
echo Starting the application...
echo.
echo Access your system at: http://localhost:5000
echo Admin login: username=admin, password=admin123
echo.
echo Press Ctrl+C to stop the server
echo.
python app.py
pause
"""
    
    with open('start-production.bat', 'w') as f:
        f.write(windows_script)
    
    # Unix shell script
    unix_script = """#!/bin/bash
echo ""
echo "================================================"
echo "  King Salomon Academy - Production Server"
echo "================================================"
echo ""
echo "Starting the application..."
echo ""
echo "Access your system at: http://localhost:5000"
echo "Admin login: username=admin, password=admin123"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Set production environment
export FLASK_ENV=production

# Start the application
python app.py
"""
    
    with open('start-production.sh', 'w') as f:
        f.write(unix_script)
    
    # Make Unix script executable
    if os.name != 'nt':
        os.chmod('start-production.sh', 0o755)
    
    print("📝 Created production startup scripts")

def create_nginx_config():
    """Create basic Nginx configuration"""
    nginx_config = """# Basic Nginx configuration for King Salomon Academy
# Place this in your Nginx sites-available directory

server {
    listen 80;
    server_name your-domain.com www.your-domain.com;
    
    # Redirect HTTP to HTTPS
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name your-domain.com www.your-domain.com;
    
    # SSL Configuration (replace with your certificates)
    ssl_certificate /path/to/your/cert.pem;
    ssl_certificate_key /path/to/your/key.pem;
    
    # Security headers
    add_header X-Frame-Options DENY;
    add_header X-Content-Type-Options nosniff;
    add_header X-XSS-Protection "1; mode=block";
    
    # File upload size
    client_max_body_size 500M;
    
    # Static files
    location /static/ {
        alias /path/to/your/app/static/;
        expires 1y;
    }
    
    # Main application
    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
"""
    
    with open('nginx-config.txt', 'w') as f:
        f.write(nginx_config)
    
    print("📝 Created Nginx configuration template")

def main():
    """Main deployment function"""
    print("🎓 King Salomon Academy - Simple Production Deployment")
    print("=" * 60)
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        sys.exit(1)
    
    # Create directories
    create_directories()
    
    # Setup environment
    setup_environment()
    
    # Initialize database
    if not initialize_database():
        print("❌ Failed to initialize database")
        sys.exit(1)
    
    # Create production scripts
    create_production_scripts()
    
    # Create Nginx config
    create_nginx_config()
    
    print("\n" + "=" * 60)
    print("✅ DEPLOYMENT COMPLETED SUCCESSFULLY!")
    print("=" * 60)
    print()
    print("🚀 To start your application:")
    print("   Windows: start-production.bat")
    print("   Linux/Mac: ./start-production.sh")
    print("   Or directly: python app.py")
    print()
    print("🌐 Access your system at:")
    print("   http://localhost:5000")
    print()
    print("👤 Admin login:")
    print("   Username: admin")
    print("   Password: admin123")
    print()
    print("🔧 For production deployment:")
    print("   1. Edit .env file with secure settings")
    print("   2. Change admin password")
    print("   3. Configure domain name")
    print("   4. Set up SSL certificate")
    print("   5. Use Nginx as reverse proxy (see nginx-config.txt)")
    print()
    print("📚 For detailed instructions, see DEPLOYMENT.md")
    print()
    print("🎉 Your King Salomon Academy system is ready!")

if __name__ == '__main__':
    main()
