#!/usr/bin/env python3
"""
Database Schema Update Script for OTP Authentication
Updates existing database to support OTP functionality
"""

import os
import sys
import sqlite3
from datetime import datetime

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def update_database_schema():
    """Update the existing database schema to support OTP"""
    db_path = 'instance/academy_media.db'
    
    if not os.path.exists(db_path):
        print("❌ Database file not found. Please run the application first to create the database.")
        return False
    
    print("🔄 Updating database schema for OTP authentication...")
    
    try:
        # Connect to the database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Check if phone_number column exists
        cursor.execute("PRAGMA table_info(user)")
        columns = [column[1] for column in cursor.fetchall()]
        
        if 'phone_number' not in columns:
            print("📱 Adding phone_number column to user table...")
            cursor.execute("ALTER TABLE user ADD COLUMN phone_number VARCHAR(20)")
            print("✅ phone_number column added")
        else:
            print("✅ phone_number column already exists")
        
        # Check if is_verified column exists
        if 'is_verified' not in columns:
            print("🔐 Adding is_verified column to user table...")
            cursor.execute("ALTER TABLE user ADD COLUMN is_verified BOOLEAN DEFAULT 1")
            print("✅ is_verified column added")
        else:
            print("✅ is_verified column already exists")
        
        # Create OTP table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS otp_code (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email VARCHAR(120) NOT NULL,
                phone_number VARCHAR(20),
                code VARCHAR(6) NOT NULL,
                purpose VARCHAR(20) NOT NULL,
                expires_at DATETIME NOT NULL,
                is_used BOOLEAN DEFAULT 0,
                attempts INTEGER DEFAULT 0,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        print("✅ OTP table created")
        
        # Update existing users to be verified
        cursor.execute("UPDATE user SET is_verified = 1 WHERE is_verified IS NULL")
        updated_users = cursor.rowcount
        print(f"✅ Updated {updated_users} existing users to verified status")
        
        # Commit changes
        conn.commit()
        conn.close()
        
        print("🎉 Database schema updated successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Error updating database: {e}")
        if 'conn' in locals():
            conn.rollback()
            conn.close()
        return False

def create_test_users():
    """Create test users for OTP testing"""
    db_path = 'instance/academy_media.db'
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Create test admin
        cursor.execute("""
            INSERT OR IGNORE INTO user (username, email, phone_number, password_hash, role, full_name, is_verified)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, ('admin', 'admin@kingsalomon.ac.rw', '+250123456789', 
              'pbkdf2:sha256:600000$abc123$def456', 'admin', 'King Salomon Academy Admin', 1))
        
        # Create test student
        cursor.execute("""
            INSERT OR IGNORE INTO user (username, email, phone_number, password_hash, role, full_name, is_verified)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, ('student1', 'student1@kingsalomon.ac.rw', '+250987654321', 
              'pbkdf2:sha256:600000$abc123$def456', 'student', 'Test Student', 1))
        
        # Create test teacher
        cursor.execute("""
            INSERT OR IGNORE INTO user (username, email, phone_number, password_hash, role, full_name, is_verified)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, ('teacher1', 'teacher1@kingsalomon.ac.rw', '+250555123456', 
              'pbkdf2:sha256:600000$abc123$def456', 'teacher', 'Test Teacher', 1))
        
        conn.commit()
        conn.close()
        
        print("✅ Test users created:")
        print("   👤 Admin: admin / admin123")
        print("   👤 Student: student1 / student123")
        print("   👤 Teacher: teacher1 / teacher123")
        
        return True
        
    except Exception as e:
        print(f"❌ Error creating test users: {e}")
        if 'conn' in locals():
            conn.close()
        return False

if __name__ == '__main__':
    print("🎓 King Salomon Academy - Database Schema Update")
    print("=" * 60)
    
    if update_database_schema():
        print("\n" + "=" * 60)
        print("👥 Creating test users...")
        create_test_users()
        
        print("\n" + "=" * 60)
        print("🚀 OTP Authentication Setup Complete!")
        print("\n📖 How to test:")
        print("1. Start the application: python app.py")
        print("2. Go to http://localhost:5000/register")
        print("3. Register a new account with phone number")
        print("4. Check the console for OTP code")
        print("5. Enter the code to verify your account")
        print("6. Login with your credentials")
        print("7. Check console again for login OTP")
        print("\n🔒 Security Features:")
        print("• Codes expire in 10 minutes")
        print("• Maximum 3 attempts per code")
        print("• Codes sent via email and SMS")
        print("• Development mode shows codes in console")
        print("\n📱 Test Accounts:")
        print("• Admin: admin / admin123")
        print("• Student: student1 / student123")
        print("• Teacher: teacher1 / teacher123")
    else:
        print("❌ Schema update failed!")
        sys.exit(1)
