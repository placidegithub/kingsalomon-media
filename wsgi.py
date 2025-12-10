#!/usr/bin/env python3
"""
King Salomon Academy Media Management System
WSGI Entry Point for Production Deployment
"""

import os
import sys
from app import app, db

# Add the project directory to Python path
project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_dir)

# Handle database URL conversion for PostgreSQL (common in free hosting)
database_url = os.environ.get('DATABASE_URL', 'sqlite:///academy_media.db')
# Convert postgres:// to postgresql:// (for compatibility)
if database_url.startswith('postgres://'):
    database_url = database_url.replace('postgres://', 'postgresql://', 1)
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url

# Initialize database
with app.app_context():
    db.create_all()
    
    # Create admin user if it doesn't exist
    from app import User
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
        print("Admin user created: username='admin', password='admin123'")
    else:
        # Ensure admin has correct role and status
        if admin.role != 'admin':
            admin.role = 'admin'
        if getattr(admin, 'approval_status', 'approved') != 'approved':
            admin.approval_status = 'approved'
        if not admin.is_verified:
            admin.is_verified = True
        db.session.commit()

# Create upload directories
os.makedirs('static/uploads/images', exist_ok=True)
os.makedirs('static/uploads/videos', exist_ok=True)

if __name__ == "__main__":
    app.run()
