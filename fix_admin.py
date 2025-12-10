#!/usr/bin/env python3
"""
Check and Fix Database Script
Checks existing users and fixes admin account issues
"""

import os
import sys
import sqlite3
from werkzeug.security import generate_password_hash

def check_and_fix_database():
    """Check existing users and fix admin accounts"""
    db_path = 'instance/academy_media.db'
    
    if not os.path.exists(db_path):
        print("❌ Database file not found!")
        return False
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Check existing users
        cursor.execute("SELECT username, email, phone_number FROM user")
        users = cursor.fetchall()
        
        print("📋 Current users in database:")
        print("=" * 50)
        for user in users:
            print(f"👤 {user[0]} | 📧 {user[1]} | 📱 {user[2]}")
        print("=" * 50)
        
        # Your details
        email_address = 'eliemaurice250@gmail.com'
        phone_number = '+250789898161'
        
        # Check if email already exists
        cursor.execute("SELECT username FROM user WHERE email = ?", (email_address,))
        existing_user = cursor.fetchone()
        
        if existing_user:
            print(f"⚠️  Email {email_address} is already used by user: {existing_user[0]}")
            
            # Update the existing user to be admin
            cursor.execute("""
                UPDATE user 
                SET username = 'admin', role = 'admin', full_name = 'King Salomon Academy Admin', is_verified = 1
                WHERE email = ?
            """, (email_address,))
            
            # Update password
            admin_password_hash = generate_password_hash('admin123')
            cursor.execute("""
                UPDATE user 
                SET password_hash = ?
                WHERE email = ?
            """, (admin_password_hash, email_address))
            
            print("✅ Updated existing user to admin account")
        else:
            # Create new admin account
            admin_password_hash = generate_password_hash('admin123')
            cursor.execute("""
                INSERT INTO user (username, email, phone_number, password_hash, role, full_name, is_verified)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, ('admin', email_address, phone_number, admin_password_hash, 'admin', 'King Salomon Academy Admin', 1))
            print("✅ Created new admin account")
        
        conn.commit()
        conn.close()
        
        print("\n🎉 Admin Account Ready!")
        print("=" * 50)
        print("👤 Username: admin")
        print("🔑 Password: admin123")
        print(f"📧 Email: {email_address}")
        print(f"📱 Phone: {phone_number}")
        print("=" * 50)
        
        print("\n📧 Email OTP will be sent to your email!")
        print("📱 SMS OTP will be sent to your phone!")
        print("🖥️  Console will also show OTP codes for development")
        
        return True
        
    except Exception as e:
        print(f"❌ Error fixing database: {e}")
        if 'conn' in locals():
            conn.close()
        return False

if __name__ == '__main__':
    print("🔧 King Salomon Academy - Check and Fix Database")
    print("=" * 60)
    
    check_and_fix_database()
    
    print("\n🚀 Ready to login!")
    print("📖 Next steps:")
    print("1. Go to http://localhost:5000/login")
    print("2. Use admin credentials above")
    print("3. Check your email for OTP code")
    print("4. Check your phone for SMS OTP")
    print("5. Check console for OTP code")
    print("6. Enter the code to access dashboard")
