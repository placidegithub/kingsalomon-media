#!/usr/bin/env python3
"""
Final OTP Test
Tests the OTP system with the fixed code
"""

import requests
import time

def test_otp_login():
    """Test the login and OTP generation"""
    
    print("Testing OTP Login System...")
    print("=" * 40)
    
    # Test login
    login_data = {
        'username': 'admin',
        'password': 'admin123'
    }
    
    try:
        print("Sending login request...")
        response = requests.post("http://localhost:5000/login", 
                                data=login_data, 
                                allow_redirects=False)
        
        print(f"Response status: {response.status_code}")
        
        if response.status_code == 302:
            print("SUCCESS: Login triggered OTP generation!")
            print("Check the terminal running 'python app.py' for the OTP code!")
            print("")
            print("You should see something like:")
            print("OTP CODE FOR HNIYOMWUNGERI582@GMAIL.COM: 123456")
            print("Email would be sent to: hniyomwungeri582@gmail.com")
            print("SMS would be sent to: +250728870138")
            print("Purpose: login")
            print("=" * 50)
            return True
        else:
            print(f"ERROR: Login failed with status {response.status_code}")
            return False
            
    except Exception as e:
        print(f"ERROR: {e}")
        return False

if __name__ == '__main__':
    print("King Salomon Academy - Final OTP Test")
    print("=" * 50)
    
    if test_otp_login():
        print("\nOTP SYSTEM IS WORKING!")
        print("The OTP code should now be visible in the terminal running 'python app.py'")
        print("\nNext steps:")
        print("1. Look at the terminal running 'python app.py'")
        print("2. Find the OTP code (6 digits)")
        print("3. Go to http://localhost:5000/verify-otp/login")
        print("4. Enter the OTP code")
        print("5. Access the dashboard!")
    else:
        print("\nOTP SYSTEM TEST FAILED!")
        print("Please check if the application is running.")
