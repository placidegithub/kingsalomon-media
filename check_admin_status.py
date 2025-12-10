#!/usr/bin/env python3
"""
Check Admin User Status
Checks if the admin user is verified
"""

import sqlite3
import os

def check_admin_user():
    """Check the admin user status"""
    
    db_path = 'instance/academy_media.db'
    
    if not os.path.exists(db_path):
        print("Database not found!")
        return False
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Check admin user
        cursor.execute("SELECT username, email, phone_number, is_verified FROM user WHERE username = 'admin'")
        admin = cursor.fetchone()
        
        if admin:
            print("Admin User Details:")
            print(f"  Username: {admin[0]}")
            print(f"  Email: {admin[1]}")
            print(f"  Phone: {admin[2]}")
            print(f"  Verified: {admin[3]}")
            
            if admin[3] == 0:
                print("\nISSUE FOUND: Admin user is NOT verified!")
                print("This is why login returns status 200 instead of 302.")
                return False
            else:
                print("\nAdmin user is verified - login should work.")
                return True
        else:
            print("Admin user not found!")
            return False
        
        conn.close()
        
    except Exception as e:
        print(f"Database error: {e}")
        return False

if __name__ == '__main__':
    print("Checking Admin User Status...")
    print("=" * 40)
    
    check_admin_user()
