#!/usr/bin/env python3
"""
OTP Debug Test - Simple Version
Tests the OTP system and shows exactly what's happening
"""

import os
import sys
import requests
import time
from datetime import datetime

def test_otp_system():
    """Test the OTP system step by step"""
    
    print("=" * 60)
    print("OTP SYSTEM DEBUG TEST")
    print("=" * 60)
    
    # Step 1: Check if app is running
    print("STEP 1: Checking if application is running...")
    try:
        response = requests.get("http://localhost:5000", timeout=5)
        if response.status_code == 200:
            print("OK - Application is running on http://localhost:5000")
        else:
            print(f"ERROR - Application error: {response.status_code}")
            return False
    except Exception as e:
        print(f"ERROR - Application not running: {e}")
        return False
    
    # Step 2: Test login and trigger OTP
    print("\nSTEP 2: Testing login to trigger OTP...")
    
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
            print("OK - Login successful! OTP should be generated now.")
            print("OK - Check the terminal running 'python app.py' for the OTP code.")
        else:
            print(f"ERROR - Login failed: {response.status_code}")
            print(f"Response: {response.text[:200]}...")
            return False
            
    except Exception as e:
        print(f"ERROR - Login test failed: {e}")
        return False
    
    # Step 3: Check environment variables
    print("\nSTEP 3: Checking environment configuration...")
    
    flask_env = os.environ.get('FLASK_ENV', 'Not set')
    print(f"FLASK_ENV: {flask_env}")
    
    # Step 4: Show what should happen
    print("\nSTEP 4: What should happen next...")
    print("In the terminal running 'python app.py', you should see:")
    print("")
    print("OTP CODE FOR HNIYOMWUNGERI582@GMAIL.COM: XXXXXX")
    print("Email would be sent to: hniyomwungeri582@gmail.com")
    print("SMS would be sent to: +250728870138")
    print("Purpose: login")
    print("=" * 50)
    print("")
    
    return True

def create_simple_otp_test():
    """Create a simple OTP test that bypasses the web interface"""
    
    print("\n" + "=" * 60)
    print("SIMPLE OTP TEST")
    print("=" * 60)
    
    # Import the OTP functions directly
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    
    try:
        from app import create_otp_code
        
        print("Testing OTP generation directly...")
        
        # Test OTP creation
        result = create_otp_code(
            email="hniyomwungeri582@gmail.com",
            phone_number="+250728870138",
            purpose="login"
        )
        
        if result:
            print("OK - OTP code generated successfully!")
            print("OK - Check the terminal output above for the code.")
        else:
            print("ERROR - OTP generation failed!")
            
    except Exception as e:
        print(f"ERROR - Error testing OTP: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    print("Starting OTP Debug Test...")
    
    # Test the web interface
    if test_otp_system():
        print("\nOK - Web interface test passed!")
    else:
        print("\nERROR - Web interface test failed!")
    
    # Test OTP generation directly
    create_simple_otp_test()
    
    print("\n" + "=" * 60)
    print("DEBUG COMPLETE")
    print("=" * 60)
    print("If you still don't see OTP codes, the issue might be:")
    print("1. The terminal window is not visible")
    print("2. The application is not running")
    print("3. There's an error in the OTP generation")
    print("4. The console output is being redirected")
