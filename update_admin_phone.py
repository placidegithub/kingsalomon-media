#!/usr/bin/env python3
"""
Update Admin Phone Number Script
Updates admin account with your specific phone number
"""

import os
import sys
import sqlite3


def update_admin_phone():
    """Update admin account with your phone number"""
    db_path = 'instance/academy_media.db'

    if not os.path.exists(db_path):
        print("❌ Database file not found!")
        return False

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Your phone number
        phone_number = '+250789898161'  # Removed spaces for consistency

        # Update admin account
        cursor.execute("""
            UPDATE user 
            SET phone_number = ?
            WHERE username = 'admin'
        """, (phone_number,))

        # Also update superadmin
        cursor.execute("""
            UPDATE user 
            SET phone_number = ?
            WHERE username = 'superadmin'
        """, (phone_number,))

        conn.commit()
        conn.close()

        print("✅ Admin phone numbers updated successfully!")
        print("\n🎉 Updated Admin Accounts:")
        print("=" * 50)
        print("👤 Username: admin")
        print("🔑 Password: admin123")
        print("📧 Email: admin@kingsalomon.ac.rw")
        print(f"📱 Phone: {phone_number}")
        print("=" * 50)
        print("👤 Username: superadmin")
        print("🔑 Password: super123")
        print("📧 Email: superadmin@kingsalomon.ac.rw")
        print(f"📱 Phone: {phone_number}")
        print("=" * 50)

        print("\n📱 SMS OTP will now be sent to your phone!")
        print("📧 Email OTP will also be sent to the email addresses")
        print("🖥️  Console will still show OTP codes for development")

        return True

    except Exception as e:
        print(f"❌ Error updating phone numbers: {e}")
        if 'conn' in locals():
            conn.close()
        return False


if __name__ == '__main__':
    print("📱 King Salomon Academy - Update Admin Phone Number")
    print("=" * 60)

    update_admin_phone()

    print("\n🚀 Ready to login!")
    print("📖 Next steps:")
    print("1. Go to http://localhost:5000/login")
    print("2. Use admin credentials above")
    print("3. Check your phone for SMS OTP")
    print("4. Check email for email OTP")
    print("5. Check console for OTP code")
    print("6. Enter the code to access dashboard")
