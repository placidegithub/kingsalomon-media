#!/usr/bin/env python3
"""
King Salomon Academy Media Management System
Database Initialization Script
"""

from app import app, db, User
import os


def init_database():
    """Initialize the database with tables and admin user"""
    print("🎓 King Salomon Academy Media Management System")
    print("=" * 50)
    print("📊 Initializing database...")

    with app.app_context():
        # Create all tables
        db.create_all()
        print("✅ Database tables created successfully")

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
            print("✅ Admin user created:")
            print("   Username: admin")
            print("   Password: admin123")
            print("   Email: admin@kingsalomon.ac.rw")
        else:
            print("✅ Admin user already exists")

        # Create upload directories
        directories = [
            'static/uploads',
            'static/uploads/images',
            'static/uploads/videos'
        ]

        for directory in directories:
            os.makedirs(directory, exist_ok=True)
            print(f"✅ Directory created: {directory}")

        print("\n🎉 Database initialization completed successfully!")
        print("🚀 You can now run the application with: python app.py")
        print("🌐 Access the system at: http://localhost:5000")


if __name__ == '__main__':
    init_database()
