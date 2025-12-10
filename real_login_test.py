#!/usr/bin/env python3
"""
Real Login Test
Tests the actual login process and shows OTP generation
"""

import requests
import time
import json

def test_real_login():
    """Test the actual login process"""
    
    print("Testing Real Login Process...")
    print("=" * 50)
    
    # Test login endpoint
    login_url = "http://localhost:5000/login"
    
    # Login data
    login_data = {
        'username': 'admin',
        'password': 'admin123'
    }
    
    try:
        print("1. Sending login request...")
        response = requests.post(login_url, data=login_data, allow_redirects=False)
        
        print(f"2. Response status: {response.status_code}")
        
        if response.status_code == 302:  # Redirect to OTP verification
            print("3. Login successful! Redirecting to OTP verification...")
            print("4. Check the terminal where 'python app.py' is running!")
            print("5. Look for the OTP code in that terminal window")
            return True
        else:
            print(f"3. Unexpected response: {response.status_code}")
            print(f"   Response content: {response.text[:200]}...")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return False

def show_what_to_look_for():
    """Show what the user should look for"""
    
    print("\nWHAT TO LOOK FOR:")
    print("=" * 50)
    print("In the terminal where 'python app.py' is running, you should see:")
    print("")
    print("OTP CODE FOR HNIYOMWUNGERI582@GMAIL.COM: 123456")
    print("Email would be sent to: hniyomwungeri582@gmail.com")
    print("SMS would be sent to: +250728870138")
    print("Purpose: login")
    print("==================================================")
    print("")
    print("Copy the 6-digit number (like 123456) and use it to verify!")

if __name__ == '__main__':
    print("King Salomon Academy - Real Login Test")
    print("=" * 60)
    
    # Test real login
    if test_real_login():
        print("\nSUCCESS: Login process triggered!")
        show_what_to_look_for()
    else:
        print("\nFAILED: Login process failed!")
        print("Make sure the application is running with: python app.py")
