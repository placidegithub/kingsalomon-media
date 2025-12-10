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
            role='admin'
        )
        admin.set_password('admin123')
        db.session.add(admin)
        db.session.commit()

# Create upload directories
os.makedirs('static/uploads/images', exist_ok=True)
os.makedirs('static/uploads/videos', exist_ok=True)

if __name__ == "__main__":
    app.run()
