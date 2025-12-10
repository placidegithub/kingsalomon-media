#!/usr/bin/env python3
"""
Test script to check user registration and login functionality
"""

from app import app, db, User

def test_users():
    """Test user functionality"""
    print("🔍 Testing User Registration and Login")
    print("=" * 40)
    
    with app.app_context():
        # Check if database exists and has users
        users = User.query.all()
        print(f"📊 Total users in database: {len(users)}")
        
        for user in users:
            print(f"👤 User: {user.username}")
            print(f"   Name: {user.full_name}")
            print(f"   Email: {user.email}")
            print(f"   Role: {user.role}")
            print(f"   Password Hash: {user.password_hash[:20]}...")
            print()
        
        # Test creating a test user
        test_user = User.query.filter_by(username='testuser').first()
        if not test_user:
            print("🧪 Creating test user...")
            test_user = User(
                username='testuser',
                email='test@kingsalomon.ac.rw',
                full_name='Test User',
                role='student'
            )
            test_user.set_password('test123')
            db.session.add(test_user)
            db.session.commit()
            print("✅ Test user created successfully!")
        else:
            print("✅ Test user already exists")
        
        # Test password verification
        print("\n🔐 Testing password verification...")
        test_user = User.query.filter_by(username='testuser').first()
        if test_user:
            password_check = test_user.check_password('test123')
            print(f"✅ Password verification: {'PASSED' if password_check else 'FAILED'}")
            
            wrong_password = test_user.check_password('wrongpassword')
            print(f"✅ Wrong password test: {'PASSED' if not wrong_password else 'FAILED'}")
        
        print("\n🎯 Login Test Credentials:")
        print("   Username: testuser")
        print("   Password: test123")
        print("   Role: student")

if __name__ == '__main__':
    test_users()
