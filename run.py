#!/usr/bin/env python3
"""
King Salomon Academy Media Management System
Startup script for production deployment
"""

import os
import sys
from app import app, db

def create_tables():
    """Create database tables if they don't exist"""
    with app.app_context():
        db.create_all()
        print("✓ Database tables created successfully")

def create_admin_user():
    """Create admin user if it doesn't exist"""
    from app import User
    
    with app.app_context():
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
            print("✓ Admin user created: username='admin', password='admin123'")
        else:
            print("✓ Admin user already exists")

def setup_directories():
    """Create necessary directories"""
    directories = [
        'static/uploads',
        'static/uploads/images',
        'static/uploads/videos'
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"✓ Directory created: {directory}")

if __name__ == '__main__':
    print("🎓 King Salomon Academy Media Management System")
    print("=" * 50)
    
    # Setup directories
    setup_directories()
    
    # Create database tables
    create_tables()
    
    # Create admin user
    create_admin_user()
    
    print("\n🚀 Starting application...")
    print("📍 Access the system at: http://localhost:5000")
    print("👤 Admin login: username='admin', password='admin123'")
    print("⚠️  Remember to change the admin password after first login!")
    print("\n" + "=" * 50)
    
    # Run the application
    app.run(
        debug=False,
        host='0.0.0.0',
        port=5000,
        threaded=True
    )
