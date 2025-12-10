#!/usr/bin/env python3
"""
OTP Test Script
Tests the OTP generation and shows where to find codes
"""

import os
import sys
import sqlite3
from datetime import datetime, timedelta
import random
import string

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_otp_generation():
    """Test OTP generation and show where codes appear"""
    
    print("🔐 King Salomon Academy - OTP Test")
    print("=" * 50)
    
    # Generate test OTP
    code = ''.join(random.choices(string.digits, k=6))
    
    print(f"📱 Generated test OTP: {code}")
    print(f"⏰ Generated at: {datetime.now().strftime('%H:%M:%S')}")
    print(f"⏳ Expires in: 10 minutes")
    
    print("\n🎯 WHERE TO FIND OTP CODES:")
    print("=" * 50)
    print("1. 🔍 Look at the TERMINAL/CONSOLE window")
    print("2. 📱 Look for lines like this:")
    print("   🔐 OTP CODE FOR HNIYOMWUNGERI582@GMAIL.COM: 123456")
    print("   📧 Email would be sent to: hniyomwungeri582@gmail.com")
    print("   🎯 Purpose: login")
    print("   ==================================================")
    print("3. 📋 Copy the 6-digit number after the colon")
    print("4. ⌨️  Paste it into the verification form")
    
    return code

def check_database():
    """Check if admin account exists and is correct"""
    
    db_path = 'instance/academy_media.db'
    
    if not os.path.exists(db_path):
        print("❌ Database not found!")
        return False
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Check admin account
        cursor.execute("SELECT username, email, phone_number, is_verified FROM user WHERE username = 'admin'")
        admin = cursor.fetchone()
        
        if admin:
            print("\n✅ Admin Account Found:")
            print(f"   Username: {admin[0]}")
            print(f"   Email: {admin[1]}")
            print(f"   Phone: {admin[2]}")
            print(f"   Verified: {admin[3]}")
        else:
            print("❌ Admin account not found!")
            return False
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"❌ Database error: {e}")
        return False

def show_login_instructions():
    """Show step-by-step login instructions"""
    
    print("\n🚀 STEP-BY-STEP LOGIN INSTRUCTIONS:")
    print("=" * 50)
    print("1. 🌐 Open browser and go to: http://localhost:5000/login")
    print("2. 👤 Enter username: admin")
    print("3. 🔑 Enter password: admin123")
    print("4. 🖱️  Click 'Login' button")
    print("5. 👀 IMMEDIATELY look at the TERMINAL window")
    print("6. 🔍 Find the OTP code (6 digits)")
    print("7. ⌨️  Enter the code in the verification form")
    print("8. ✅ Click 'Verify Code'")
    print("9. 🎉 Access the dashboard!")
    
    print("\n⚠️  IMPORTANT NOTES:")
    print("=" * 50)
    print("• OTP codes are ONLY shown in the terminal/console")
    print("• Codes expire in 10 minutes")
    print("• You have 3 attempts to enter the correct code")
    print("• If you miss a code, click 'Resend Code'")

if __name__ == '__main__':
    print("🔍 King Salomon Academy - OTP Troubleshooting")
    print("=" * 60)
    
    # Test OTP generation
    test_code = test_otp_generation()
    
    # Check database
    if check_database():
        print("\n✅ Database check passed")
    else:
        print("\n❌ Database check failed")
    
    # Show instructions
    show_login_instructions()
    
    print(f"\n🎯 Test OTP Code: {test_code}")
    print("💡 This is what you should see in the terminal when you login!")
