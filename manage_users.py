#!/usr/bin/env python3
"""
King Salomon Academy - User Management Script
"""

from app import app, db, User

def list_users():
    """List all users in the database"""
    print("👥 King Salomon Academy - User Management")
    print("=" * 50)
    
    with app.app_context():
        users = User.query.all()
        
        if not users:
            print("❌ No users found in database")
            return
        
        print(f"📊 Total users: {len(users)}")
        print()
        
        for i, user in enumerate(users, 1):
            print(f"{i}. 👤 {user.full_name}")
            print(f"   Username: {user.username}")
            print(f"   Email: {user.email}")
            print(f"   Role: {user.role}")
            print(f"   Created: {user.created_at.strftime('%Y-%m-%d %H:%M')}")
            print()

def create_test_user():
    """Create a test student user"""
    print("🧪 Creating test student user...")
    
    with app.app_context():
        # Check if test student already exists
        test_user = User.query.filter_by(username='student1').first()
        if test_user:
            print("✅ Test student already exists")
            return
        
        # Create test student
        student = User(
            username='student1',
            email='student1@kingsalomon.ac.rw',
            full_name='Test Student',
            role='student'
        )
        student.set_password('student123')
        db.session.add(student)
        db.session.commit()
        
        print("✅ Test student created successfully!")
        print("   Username: student1")
        print("   Password: student123")
        print("   Role: student")

def create_test_teacher():
    """Create a test teacher user"""
    print("🧪 Creating test teacher user...")
    
    with app.app_context():
        # Check if test teacher already exists
        test_teacher = User.query.filter_by(username='teacher1').first()
        if test_teacher:
            print("✅ Test teacher already exists")
            return
        
        # Create test teacher
        teacher = User(
            username='teacher1',
            email='teacher1@kingsalomon.ac.rw',
            full_name='Test Teacher',
            role='teacher'
        )
        teacher.set_password('teacher123')
        db.session.add(teacher)
        db.session.commit()
        
        print("✅ Test teacher created successfully!")
        print("   Username: teacher1")
        print("   Password: teacher123")
        print("   Role: teacher")

def reset_user_password(username, new_password):
    """Reset a user's password"""
    with app.app_context():
        user = User.query.filter_by(username=username).first()
        if user:
            user.set_password(new_password)
            db.session.commit()
            print(f"✅ Password reset for {username}")
        else:
            print(f"❌ User {username} not found")

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == 'list':
            list_users()
        elif command == 'create-student':
            create_test_user()
        elif command == 'create-teacher':
            create_test_teacher()
        elif command == 'reset-password' and len(sys.argv) == 4:
            username = sys.argv[2]
            new_password = sys.argv[3]
            reset_user_password(username, new_password)
        else:
            print("Usage:")
            print("  python manage_users.py list")
            print("  python manage_users.py create-student")
            print("  python manage_users.py create-teacher")
            print("  python manage_users.py reset-password <username> <new_password>")
    else:
        list_users()
        print("\n🎯 Test Credentials for Login:")
        print("   Admin: username=admin, password=admin123")
        print("   Student: username=student1, password=student123")
        print("   Teacher: username=teacher1, password=teacher123")
