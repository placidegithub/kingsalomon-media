#!/usr/bin/env python3
"""
Admin Credential Reset Script
Creates a new admin account or resets existing admin credentials
"""

import os
import sys
import sqlite3
from werkzeug.security import generate_password_hash


def reset_admin_credentials():
    """Reset admin credentials to known values"""
    db_path = 'instance/academy_media.db'

    if not os.path.exists(db_path):
        print("❌ Database file not found!")
        return False

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # New admin credentials
        username = 'admin'
        email = 'admin@kingsalomon.ac.rw'
        phone = '+250123456789'
        password = 'admin123'
        full_name = 'King Salomon Academy Admin'

        # Hash the password
        password_hash = generate_password_hash(password)

        # Check if admin exists
        cursor.execute("SELECT id FROM user WHERE username = ?", (username,))
        admin_exists = cursor.fetchone()

        if admin_exists:
            # Update existing admin
            cursor.execute("""
                UPDATE user 
                SET email = ?, phone_number = ?, password_hash = ?, full_name = ?, is_verified = 1
                WHERE username = ?
            """, (email, phone, password_hash, full_name, username))
            print("✅ Admin credentials updated!")
        else:
            # Create new admin
            cursor.execute("""
                INSERT INTO user (username, email, phone_number, password_hash, role, full_name, is_verified)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (username, email, phone, password_hash, 'admin', full_name, 1))
            print("✅ New admin account created!")

        conn.commit()
        conn.close()

        print("\n🎉 Admin Account Ready!")
        print("=" * 40)
        print(f"👤 Username: {username}")
        print(f"🔑 Password: {password}")
        print(f"📧 Email: {email}")
        print(f"📱 Phone: {phone}")
        print("=" * 40)
        print("\n📖 How to login:")
        print("1. Go to http://localhost:5000/login")
        print("2. Enter username: admin")
        print("3. Enter password: admin123")
        print("4. Check console for OTP code")
        print("5. Enter the OTP code to access dashboard")

        return True

    except Exception as e:
        print(f"❌ Error resetting admin credentials: {e}")
        if 'conn' in locals():
            conn.close()
        return False


def create_super_admin():
    """Create a super admin account with different credentials"""
    db_path = 'instance/academy_media.db'

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Super admin credentials
        username = 'superadmin'
        email = 'superadmin@kingsalomon.ac.rw'
        phone = '+250987654321'
        password = 'super123'
        full_name = 'Super Administrator'

        # Hash the password
        password_hash = generate_password_hash(password)

        # Create super admin
        cursor.execute("""
            INSERT OR REPLACE INTO user (username, email, phone_number, password_hash, role, full_name, is_verified)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (username, email, phone, password_hash, 'admin', full_name, 1))

        conn.commit()
        conn.close()

        print("\n🎉 Super Admin Account Created!")
        print("=" * 40)
        print(f"👤 Username: {username}")
        print(f"🔑 Password: {password}")
        print(f"📧 Email: {email}")
        print(f"📱 Phone: {phone}")
        print("=" * 40)

        return True

    except Exception as e:
        print(f"❌ Error creating super admin: {e}")
        if 'conn' in locals():
            conn.close()
        return False


if __name__ == '__main__':
    print("🔧 King Salomon Academy - Admin Credential Reset")
    print("=" * 60)

    print("\nChoose an option:")
    print("1. Reset existing admin credentials")
    print("2. Create new super admin account")
    print("3. Both (recommended)")

    choice = input("\nEnter your choice (1/2/3): ").strip()

    if choice == '1':
        reset_admin_credentials()
    elif choice == '2':
        create_super_admin()
    elif choice == '3':
        print("\n🔄 Resetting admin credentials...")
        reset_admin_credentials()
        print("\n🔄 Creating super admin...")
        create_super_admin()
    else:
        print("❌ Invalid choice. Running default reset...")
        reset_admin_credentials()

    print("\n🚀 You can now login with the credentials above!")
    print("💡 Remember to check the console for OTP codes during login.")



