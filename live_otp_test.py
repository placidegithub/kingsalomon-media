#!/usr/bin/env python3
"""
Live OTP Test
Creates a live OTP code and shows exactly where to find it
"""

import os
import sys
import sqlite3
from datetime import datetime, timedelta
import random
import string

def create_live_otp():
    """Create a live OTP code and show it"""
    
    print("\n" + "="*60)
    print("🔐 LIVE OTP CODE GENERATION")
    print("="*60)
    
    # Generate OTP
    code = ''.join(random.choices(string.digits, k=6))
    email = "eliemaurice250@gmail.com"
    phone = "+250789898161"
    
    print(f"🔐 OTP CODE FOR {email.upper()}: {code}")
    print(f"📧 Email would be sent to: {email}")
    print(f"📱 SMS would be sent to: {phone}")
    print(f"🎯 Purpose: login")
    print(f"⏰ Generated at: {datetime.now().strftime('%H:%M:%S')}")
    print("="*60)
    
    print(f"\n🎯 YOUR OTP CODE IS: {code}")
    print("📋 Copy this code and use it to login!")
    
    return code

if __name__ == '__main__':
    print("🎓 King Salomon Academy - Live OTP Test")
    
    # Create live OTP
    otp_code = create_live_otp()
    
    print(f"\n✅ OTP Code Generated: {otp_code}")
    print("\n📖 Now try logging in:")
    print("1. Go to http://localhost:5000/login")
    print("2. Enter: admin / admin123")
    print("3. Look at THIS terminal window for the OTP code")
    print("4. Enter the code in the verification form")
    
    print(f"\n💡 Use this code: {otp_code}")
