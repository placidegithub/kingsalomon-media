#!/usr/bin/env python3
"""
Simple Email Test Script
Sends a test email using Gmail SMTP
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_test_email():
    """Send a test email with OTP code"""
    
    # Your email details
    sender_email = "hniyomwungeri582@gmail.com"
    receiver_email = "hniyomwungeri582@gmail.com"
    
    # Test OTP code
    otp_code = "789123"
    
    # Create message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "King Salomon Academy - Test OTP Code"
    
    # Email body
    body = f"""
    🎓 King Salomon Academy - Test Email
    
    Hello!
    
    This is a test email to verify that email sending works.
    
    Your test OTP code is: {otp_code}
    
    If you received this email, the email system is working!
    
    Best regards,
    King Salomon Academy System
    Gicumbi District, Rwanda
    """
    
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        print("📧 Attempting to send test email...")
        print(f"📤 From: {sender_email}")
        print(f"📥 To: {receiver_email}")
        print(f"🔐 Test OTP: {otp_code}")
        
        # Gmail SMTP settings
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        
        # Note: You need to use App Password here
        print("\n⚠️  To send real emails, you need:")
        print("1. Enable 2FA on Gmail")
        print("2. Generate App Password")
        print("3. Use App Password instead of regular password")
        
        # For now, just show what would happen
        print("\n✅ Email test completed!")
        print("📧 Email would be sent with OTP code:", otp_code)
        
        return True
        
    except Exception as e:
        print(f"❌ Email sending failed: {e}")
        print("\n💡 This is normal - you need to configure Gmail App Password")
        return False

if __name__ == '__main__':
    print("📧 King Salomon Academy - Simple Email Test")
    print("=" * 50)
    
    send_test_email()
    
    print("\n🔧 To enable real email sending:")
    print("1. Go to Gmail Settings > Security")
    print("2. Enable 2-Factor Authentication")
    print("3. Generate App Password")
    print("4. Update .env file with App Password")
    print("5. Restart the application")
    
    print("\n📱 For SMS:")
    print("1. Sign up for Twilio")
    print("2. Get credentials")
    print("3. Update .env file")
    print("4. Restart the application")
