#!/usr/bin/env python3
"""
Live Demo Script - Simple Version
Simulates the login process and shows OTP generation
"""

import requests
import time
import random
import string
from datetime import datetime

def generate_otp():
    """Generate a 6-digit OTP code"""
    return ''.join(random.choices(string.digits, k=6))

def simulate_login_process():
    """Simulate the login process and show OTP generation"""
    
    print("King Salomon Academy - Live Demo")
    print("=" * 50)
    
    # Generate OTP code
    otp_code = generate_otp()
    email = "hniyomwungeri582@gmail.com"
    phone = "+250728870138"
    
    print(f"OTP CODE FOR {email.upper()}: {otp_code}")
    print(f"Email would be sent to: {email}")
    print(f"SMS would be sent to: {phone}")
    print(f"Purpose: login")
    print(f"Generated at: {datetime.now().strftime('%H:%M:%S')}")
    print("=" * 50)
    
    print(f"\nYOUR OTP CODE IS: {otp_code}")
    print("Copy this code and use it to login!")
    
    return otp_code

def test_application():
    """Test if the application is responding"""
    
    try:
        response = requests.get("http://localhost:5000", timeout=5)
        if response.status_code == 200:
            print("Application is running and responding!")
            return True
        else:
            print(f"Application responded with status: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"Application not responding: {e}")
        return False

def show_demo_instructions():
    """Show step-by-step demo instructions"""
    
    print("\nLIVE DEMO INSTRUCTIONS:")
    print("=" * 50)
    print("1. Open your browser")
    print("2. Go to: http://localhost:5000")
    print("3. Click 'Login' button")
    print("4. Enter username: admin")
    print("5. Enter password: admin123")
    print("6. Click 'Login' button")
    print("7. Look at THIS terminal window for the OTP code")
    print("8. Enter the OTP code in the verification form")
    print("9. Click 'Verify Code'")
    print("10. Access the dashboard!")
    
    print("\nIMPORTANT:")
    print("=" * 50)
    print("- OTP codes appear in THIS terminal window")
    print("- NOT in your email or phone")
    print("- Look for the line: 'OTP CODE FOR...'")
    print("- Copy the 6-digit number after the colon")

if __name__ == '__main__':
    print("Starting Live Demo...")
    print("=" * 60)
    
    # Test application
    if test_application():
        print("\nApplication Status: RUNNING")
    else:
        print("\nApplication Status: NOT RUNNING")
        print("Please start the application with: python app.py")
        exit(1)
    
    # Simulate login process
    otp_code = simulate_login_process()
    
    # Show instructions
    show_demo_instructions()
    
    print(f"\nDEMO OTP CODE: {otp_code}")
    print("This is what you'll see when you login!")
    
    print("\nNow try logging in and watch this terminal for the OTP code!")
