#!/usr/bin/env python3
"""
Deployment Helper Script
This script helps prepare your project for deployment
"""

import os
import subprocess
import sys
import secrets
import string

def generate_secret_key():
    """Generate a secure random secret key"""
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for i in range(50))

def check_git_installed():
    """Check if Git is installed"""
    try:
        result = subprocess.run(['git', '--version'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Git is installed:", result.stdout.strip())
            return True
        else:
            return False
    except FileNotFoundError:
        return False

def check_files():
    """Check if all required files exist"""
    required_files = [
        'app.py',
        'requirements.txt',
        'Procfile',
        'wsgi.py',
        'templates',
        'static'
    ]
    
    missing = []
    for file in required_files:
        if not os.path.exists(file):
            missing.append(file)
    
    if missing:
        print("❌ Missing files:")
        for file in missing:
            print(f"   - {file}")
        return False
    else:
        print("✅ All required files are present")
        return True

def init_git_repo():
    """Initialize Git repository if not already initialized"""
    if os.path.exists('.git'):
        print("✅ Git repository already initialized")
        return True
    
    try:
        subprocess.run(['git', 'init'], check=True)
        print("✅ Git repository initialized")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to initialize Git repository")
        return False

def create_env_template():
    """Create .env template file"""
    secret_key = generate_secret_key()
    
    env_template = f"""# Environment Variables for Deployment
# Copy these values to your hosting platform

# Flask Configuration
FLASK_ENV=production
SECRET_KEY={secret_key}

# Database (will be provided by hosting platform)
# DATABASE_URL=postgresql://user:pass@host:port/dbname

# Port (for Render)
PORT=10000

# Email Configuration (Optional - for OTP)
# MAIL_SERVER=smtp.gmail.com
# MAIL_PORT=587
# MAIL_USE_TLS=True
# MAIL_USERNAME=your-email@gmail.com
# MAIL_PASSWORD=your-app-password
"""
    
    with open('.env.template', 'w', encoding='utf-8') as f:
        f.write(env_template)
    
    print("✅ Created .env.template with your SECRET_KEY")
    print(f"   Your SECRET_KEY: {secret_key}")
    return secret_key

def create_deployment_info():
    """Create a file with deployment information"""
    info = """# Deployment Information

## Your SECRET_KEY
Check .env.template file for your generated SECRET_KEY

## Required Environment Variables for Render:
1. FLASK_ENV=production
2. SECRET_KEY=(from .env.template)
3. DATABASE_URL=(from Render database - Internal URL)
4. PORT=10000

## Build Command:
pip install -r requirements.txt

## Start Command:
gunicorn --bind 0.0.0.0:$PORT wsgi:app

## Default Admin Account:
Username: admin
Password: admin123
⚠️ CHANGE THIS IMMEDIATELY AFTER FIRST LOGIN!

## Next Steps:
1. Push code to GitHub (see COMPLETE-BEGINNER-GUIDE.md)
2. Create database on Render
3. Create web service on Render
4. Set environment variables
5. Deploy!
"""
    
    with open('DEPLOYMENT-INFO.txt', 'w', encoding='utf-8') as f:
        f.write(info)
    
    print("✅ Created DEPLOYMENT-INFO.txt with all deployment details")

def main():
    print("=" * 60)
    print("🚀 King Salomon Academy - Deployment Preparation")
    print("=" * 60)
    print()
    
    # Check files
    print("📋 Checking required files...")
    if not check_files():
        print("\n❌ Please ensure all files are in the project directory")
        sys.exit(1)
    print()
    
    # Check Git
    print("🔍 Checking Git installation...")
    if not check_git_installed():
        print("❌ Git is not installed!")
        print("   Please install Git from: https://git-scm.com/download/win")
        sys.exit(1)
    print()
    
    # Initialize Git
    print("📦 Initializing Git repository...")
    init_git_repo()
    print()
    
    # Create environment template
    print("🔐 Generating SECRET_KEY...")
    secret_key = create_env_template()
    print()
    
    # Create deployment info
    print("📝 Creating deployment information...")
    create_deployment_info()
    print()
    
    print("=" * 60)
    print("✅ Preparation Complete!")
    print("=" * 60)
    print()
    print("📋 Next Steps:")
    print("1. Open DEPLOYMENT-INFO.txt to see your SECRET_KEY")
    print("2. Follow COMPLETE-BEGINNER-GUIDE.md for deployment")
    print("3. Use the SECRET_KEY when setting environment variables")
    print()
    print("💡 Your SECRET_KEY has been saved to .env.template")
    print("   Keep it safe - you'll need it for deployment!")
    print()

if __name__ == '__main__':
    main()

