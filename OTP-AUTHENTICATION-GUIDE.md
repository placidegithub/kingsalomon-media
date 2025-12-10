# 🔐 King Salomon Academy - OTP Authentication System

## 🎯 Overview
The King Salomon Academy website now includes **Two-Factor Authentication (2FA)** using OTP (One-Time Password) codes sent via both **email** and **SMS**. This significantly enhances security for user registration and login.

## 🚀 Features Added

### ✅ Registration with OTP Verification
- Users must verify their email address during registration
- Optional phone number for SMS verification
- 6-digit OTP codes with 10-minute expiration
- Maximum 3 attempts per code

### ✅ Login with OTP Verification
- After entering username/password, users receive OTP codes
- Codes sent to both email and phone (if provided)
- Enhanced security against unauthorized access

### ✅ Development Mode
- OTP codes displayed in console for testing
- No external email/SMS services required for development
- Easy testing and debugging

## 🧪 How to Test OTP Authentication

### 1. Start the Application
```bash
python app.py
```

### 2. Test Registration Flow
1. Go to `http://localhost:5000/register`
2. Fill out the registration form:
   - **Username**: `testuser`
   - **Email**: `test@example.com`
   - **Phone**: `+250123456789` (optional but recommended)
   - **Password**: `testpass123`
   - **Full Name**: `Test User`
   - **Role**: `student`
3. Click "Register"
4. **Check the console** - you'll see the OTP code displayed
5. Enter the 6-digit code on the verification page
6. Complete registration

### 3. Test Login Flow
1. Go to `http://localhost:5000/login`
2. Enter credentials:
   - **Username**: `testuser`
   - **Password**: `testpass123`
3. Click "Login"
4. **Check the console** - you'll see another OTP code
5. Enter the 6-digit code
6. Access the dashboard

### 4. Test Pre-created Accounts
Use these test accounts (already verified):
- **Admin**: `admin` / `admin123`
- **Student**: `student1` / `student123`
- **Teacher**: `teacher1` / `teacher123`

## 🔒 Security Features

### OTP Code Security
- **6-digit numeric codes**
- **10-minute expiration time**
- **Maximum 3 attempts** before code becomes invalid
- **Automatic cleanup** of expired codes
- **Rate limiting** to prevent abuse

### Multi-Channel Delivery
- **Email verification** (primary)
- **SMS verification** (optional, if phone provided)
- **Console display** (development mode)

### User Verification
- **Email verification required** for new accounts
- **Phone verification optional** but recommended
- **Verified status tracking** in database

## 📱 Production Setup

### Email Configuration
To enable real email sending, update your `.env` file:
```env
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
```

### SMS Configuration
To enable real SMS sending, update your `.env` file:
```env
TWILIO_ACCOUNT_SID=your-twilio-account-sid
TWILIO_AUTH_TOKEN=your-twilio-auth-token
TWILIO_PHONE_NUMBER=+250123456789
```

### Gmail Setup
1. Enable 2-factor authentication on your Gmail account
2. Generate an "App Password" for the application
3. Use the app password in `MAIL_PASSWORD`

### Twilio Setup
1. Create a Twilio account at https://twilio.com
2. Get your Account SID and Auth Token
3. Purchase a phone number for sending SMS
4. Configure the credentials in your `.env` file

## 🛠️ Technical Implementation

### Database Schema
- **User table**: Added `phone_number` and `is_verified` columns
- **OTP table**: New table for storing OTP codes and metadata
- **Automatic cleanup**: Expired codes are automatically removed

### Code Structure
- **OTP generation**: Secure 6-digit random codes
- **Email templates**: Professional HTML email templates
- **SMS templates**: Concise SMS messages
- **Error handling**: Comprehensive error handling and user feedback

### Security Measures
- **Session management**: Secure session handling for OTP verification
- **Input validation**: Proper validation of OTP codes
- **Rate limiting**: Prevention of brute force attacks
- **Expiration handling**: Automatic cleanup of expired codes

## 🎉 Benefits

### For Users
- **Enhanced security** with two-factor authentication
- **Multiple verification channels** (email + SMS)
- **User-friendly interface** with clear instructions
- **Automatic code expiration** for security

### For Administrators
- **Secure user registration** process
- **Reduced unauthorized access** attempts
- **Audit trail** of verification attempts
- **Easy management** of user verification status

## 🔧 Troubleshooting

### Common Issues
1. **OTP not received**: Check console output in development mode
2. **Code expired**: Request a new code using "Resend Code"
3. **Too many attempts**: Wait for code expiration and request new one
4. **Email not working**: Check email configuration in `.env` file

### Development Mode
- OTP codes are displayed in the console
- No external services required
- Easy testing and debugging
- Perfect for development and testing

## 📞 Support
For technical support or questions about the OTP system, contact the development team or check the console output for detailed error messages.

---

**🎓 King Salomon Academy - Secure Media Management System**
**📍 Gicumbi District, Rwanda**
**🔐 Enhanced with OTP Authentication**
