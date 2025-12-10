#!/usr/bin/env python3
"""
Detailed Login Test
Tests the login with detailed response analysis
"""

import requests
import time

def test_detailed_login():
    """Test login with detailed analysis"""
    
    print("Detailed Login Test")
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
        print(f"Response headers: {dict(response.headers)}")
        print(f"Response URL: {response.url}")
        
        if response.status_code == 200:
            print("\nResponse content (first 500 chars):")
            print(response.text[:500])
            print("...")
            
            # Check if there are any flash messages
            if 'flash' in response.text.lower() or 'error' in response.text.lower():
                print("\nFound flash messages in response!")
                
        elif response.status_code == 302:
            print("SUCCESS: Redirect to OTP verification!")
            print(f"Redirect location: {response.headers.get('Location', 'Not specified')}")
            
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == '__main__':
    test_detailed_login()
