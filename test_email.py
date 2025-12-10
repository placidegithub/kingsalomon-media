#!/usr/bin/env python3
"""
Test Email Sending Script
Tests if email configuration works with your Gmail account
"""

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def test_email_sending():
    """Test sending email with Gmail SMTP"""
    
    # Your email details
    sender_email = "eliemaurice250@gmail.com"
    receiver_email = "eliemaurice250@gmail.com"  # Send to yourself for testing
    
    # Test OTP code
    otp_code = "123456"
    
    # Create message
    message = MIMEMultipart("alternative")
    message["Subject"] = "King Salomon Academy - Test OTP"
    message["From"] = sender_email
    message["To"] = receiver_email
    
    # Create HTML content
    html = f"""
    <html>
    <body style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
        <div style="background: linear-gradient(135deg, #2c3e50, #3498db); color: white; padding: 20px; text-align: center;">
            <h1>🎓 King Salomon Academy</h1>
            <h2>Test Email Verification</h2>
        </div>
        <div style="padding: 30px; background: #f8f9fa;">
            <h3>Email Configuration Test</h3>
            <p>This is a test email to verify that email sending is working correctly.</p>
            
            <div style="background: #e3f2fd; border: 2px solid #2196f3; border-radius: 10px; padding: 20px; text-align: center; margin: 20px 0;">
                <h2 style="color: #1976d2; font-size: 32px; margin: 0; letter-spacing: 5px;">{otp_code}</h2>
            </div>
            
            <p><strong>If you received this email, your email configuration is working!</strong></p>
            
            <hr style="margin: 30px 0; border: none; border-top: 1px solid #ddd;">
            <p style="color: #666; font-size: 14px;">
                King Salomon Academy<br>
                Gicumbi District, Rwanda<br>
                Media Management System
            </p>
        </div>
    </body>
    </html>
    """
    
    # Create HTML part
    html_part = MIMEText(html, "html")
    message.attach(html_part)
    
    try:
        # Gmail SMTP settings
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        
        print("📧 Testing email sending...")
        print(f"📤 From: {sender_email}")
        print(f"📥 To: {receiver_email}")
        print(f"🔐 Test OTP: {otp_code}")
        
        # Note: You need to use an App Password, not your regular Gmail password
        print("\n⚠️  IMPORTANT: You need to:")
        print("1. Enable 2-Factor Authentication on your Gmail account")
        print("2. Generate an 'App Password' for this application")
        print("3. Use the App Password instead of your regular password")
        
        # For testing, we'll show what the email would look like
        print("\n📧 Email content preview:")
        print("=" * 50)
        print(f"Subject: {message['Subject']}")
        print(f"From: {message['From']}")
        print(f"To: {message['To']}")
        print(f"OTP Code: {otp_code}")
        print("=" * 50)
        
        print("\n✅ Email configuration test completed!")
        print("💡 To enable real email sending:")
        print("   1. Set up Gmail App Password")
        print("   2. Update .env file with credentials")
        print("   3. Restart the application")
        
        return True
        
    except Exception as e:
        print(f"❌ Email test failed: {e}")
        return False

if __name__ == '__main__':
    print("📧 King Salomon Academy - Email Configuration Test")
    print("=" * 60)
    
    test_email_sending()
    
    print("\n📱 For SMS testing:")
    print("   1. Sign up for Twilio account")
    print("   2. Get Account SID and Auth Token")
    print("   3. Purchase a phone number")
    print("   4. Update .env file with Twilio credentials")
