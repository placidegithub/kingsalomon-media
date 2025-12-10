#!/usr/bin/env python3
"""
Update Admin Email Script
Updates admin account with your specific email address
"""

import os
import sys
import sqlite3


def update_admin_email():
    """Update admin account with your email address"""
    db_path = 'instance/academy_media.db'

    if not os.path.exists(db_path):
        print("❌ Database file not found!")
        return False

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Your email address
        email_address = 'eliemaurice250@gmail.com'

        # Update admin account
        cursor.execute("""
            UPDATE user 
            SET email = ?
            WHERE username = 'admin'
        """, (email_address,))

        # Also update superadmin
        cursor.execute("""
            UPDATE user 
            SET email = ?
            WHERE username = 'superadmin'
        """, (email_address,))

        conn.commit()
        conn.close()

        print("✅ Admin email addresses updated successfully!")
        print("\n🎉 Updated Admin Accounts:")
        print("=" * 60)
        print("👤 Username: admin")
        print("🔑 Password: admin123")
        print(f"📧 Email: {email_address}")
        print("📱 Phone: +250789898161")
        print("=" * 60)
        print("👤 Username: superadmin")
        print("🔑 Password: super123")
        print(f"📧 Email: {email_address}")
        print("📱 Phone: +250789898161")
        print("=" * 60)

        print("\n📧 Email OTP will now be sent to your email!")
        print("📱 SMS OTP will also be sent to your phone")
        print("🖥️  Console will still show OTP codes for development")

        return True

    except Exception as e:
        print(f"❌ Error updating email addresses: {e}")
        if 'conn' in locals():
            conn.close()
        return False


if __name__ == '__main__':
    print("📧 King Salomon Academy - Update Admin Email Address")
    print("=" * 60)

    update_admin_email()

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
