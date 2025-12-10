#!/usr/bin/env python3
"""
Recreate Admin Accounts Script
Removes existing admin accounts and creates new ones with your email
"""

import os
import sys
import sqlite3
from werkzeug.security import generate_password_hash

def recreate_admin_accounts():
    """Remove existing admin accounts and create new ones with your email"""
    db_path = 'instance/academy_media.db'
    
    if not os.path.exists(db_path):
        print("❌ Database file not found!")
        return False
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Your details
        email_address = 'hniyomwungeri582@gmail.com'
        phone_number = '+250728870138'
        
        # Remove existing admin accounts
        cursor.execute("DELETE FROM user WHERE username IN ('admin', 'superadmin')")
        print("🗑️  Removed existing admin accounts")
        
        # Create new admin account
        admin_password = 'admin123'
        admin_password_hash = generate_password_hash(admin_password)
        
        cursor.execute("""
            INSERT INTO user (username, email, phone_number, password_hash, role, full_name, is_verified)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, ('admin', email_address, phone_number, admin_password_hash, 'admin', 'King Salomon Academy Admin', 1))
        
        # Create new superadmin account
        superadmin_password = 'super123'
        superadmin_password_hash = generate_password_hash(superadmin_password)
        
        cursor.execute("""
            INSERT INTO user (username, email, phone_number, password_hash, role, full_name, is_verified)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, ('superadmin', email_address, phone_number, superadmin_password_hash, 'admin', 'Super Administrator', 1))
        
        conn.commit()
        conn.close()
        
        print("✅ New admin accounts created successfully!")
        print("\n🎉 Your Admin Accounts:")
        print("=" * 60)
        print("👤 Username: admin")
        print("🔑 Password: admin123")
        print(f"📧 Email: {email_address}")
        print(f"📱 Phone: {phone_number}")
        print("=" * 60)
        print("👤 Username: superadmin")
        print("🔑 Password: super123")
        print(f"📧 Email: {email_address}")
        print(f"📱 Phone: {phone_number}")
        print("=" * 60)
        
        print("\n📧 Email OTP will be sent to your email!")
        print("📱 SMS OTP will be sent to your phone!")
        print("🖥️  Console will also show OTP codes for development")
        
        return True
        
    except Exception as e:
        print(f"❌ Error recreating admin accounts: {e}")
        if 'conn' in locals():
            conn.close()
        return False

if __name__ == '__main__':
    print("🔄 King Salomon Academy - Recreate Admin Accounts")
    print("=" * 60)
    
    recreate_admin_accounts()
    
    print("\n🚀 Ready to login!")
    print("📖 Next steps:")
    print("1. Go to http://localhost:5000/login")
    print("2. Use admin credentials above")
    print("3. Check your email for OTP code")
    print("4. Check your phone for SMS OTP")
    print("5. Check console for OTP code")
    print("6. Enter the code to access dashboard")
    print("\n💡 Note: In development mode, OTP codes are shown in console")
    print("   For production, configure email settings in .env file")
