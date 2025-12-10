#!/usr/bin/env python3
"""
Simple Browser Test
Opens browser to test login manually
"""

import webbrowser
import time

def open_login_page():
    """Open the login page in browser"""
    
    print("Opening login page in browser...")
    print("=" * 40)
    
    url = "http://localhost:5000/login"
    
    try:
        webbrowser.open(url)
        print(f"Opened: {url}")
        print("\nInstructions:")
        print("1. Enter username: admin")
        print("2. Enter password: admin123")
        print("3. Click Login")
        print("4. Look at the terminal running 'python app.py' for debug output")
        print("5. Look for OTP codes in the terminal")
        
    except Exception as e:
        print(f"Error opening browser: {e}")

if __name__ == '__main__':
    print("King Salomon Academy - Browser Test")
    print("=" * 50)
    
    open_login_page()
    
    print("\nThe login page should now be open in your browser.")
    print("Try logging in and watch the terminal for debug output!")
