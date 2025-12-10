#!/usr/bin/env python3
"""
Final Admin Setup Script
Removes existing admin and updates Placide account to admin
"""

import os
import sys
import sqlite3
from werkzeug.security import generate_password_hash

def final_admin_setup():
    """Remove existing admin and update Placide to admin"""
    db_path = 'instance/academy_media.db'
    
    if not os.path.exists(db_path):
        print("❌ Database file not found!")
        return False
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Your details
        email_address = 'eliemaurice250@gmail.com'
        phone_number = '+250789898161'
        
        # Remove existing admin account
        cursor.execute("DELETE FROM user WHERE username = 'admin'")
        print("🗑️  Removed existing admin account")
        
        # Update Placide account to admin
        admin_password_hash = generate_password_hash('admin123')
        
        cursor.execute("""
            UPDATE user 
            SET username = 'admin', 
                phone_number = ?, 
                password_hash = ?, 
                role = 'admin', 
                full_name = 'King Salomon Academy Admin', 
                is_verified = 1
            WHERE email = ?
        """, (phone_number, admin_password_hash, email_address))
        
        conn.commit()
        conn.close()
        
        print("✅ Placide account updated to admin successfully!")
        print("\n🎉 Your Admin Account:")
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
        print(f"❌ Error setting up admin: {e}")
        if 'conn' in locals():
            conn.close()
        return False

if __name__ == '__main__':
    print("🎯 King Salomon Academy - Final Admin Setup")
    print("=" * 60)
    
    final_admin_setup()
    
    print("\n🚀 Ready to login!")
    print("📖 Next steps:")
    print("1. Go to http://localhost:5000/login")
    print("2. Use admin credentials above")
    print("3. Check your email for OTP code")
    print("4. Check your phone for SMS OTP")
    print("5. Check console for OTP code")
    print("6. Enter the code to access dashboard")
