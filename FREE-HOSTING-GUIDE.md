# 🚀 Free Hosting Deployment Guide

This guide will help you deploy the King Salomon Academy Media Management System to **free hosting platforms** like Render, PythonAnywhere, Railway, and Fly.io.

## 📋 Quick Comparison

| Platform | Free Tier | Database | File Storage | Best For |
|----------|-----------|----------|--------------|----------|
| **Render** | ✅ Yes | ✅ PostgreSQL (Free) | ✅ Persistent | Production-ready |
| **PythonAnywhere** | ✅ Yes | ✅ MySQL (Free) | ✅ Persistent | Beginners |
| **Railway** | ✅ Yes | ✅ PostgreSQL (Free) | ⚠️ Limited | Quick deployment |
| **Fly.io** | ✅ Yes | ✅ PostgreSQL (Free) | ✅ Persistent | Advanced users |

---

## 🎯 Option 1: Render (Recommended)

**Render** offers a free tier with PostgreSQL database and persistent file storage.

### Step 1: Prepare Your Code

1. **Push to GitHub** (if not already):
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/YOUR_USERNAME/kingsalomon-academy.git
   git push -u origin main
   ```

### Step 2: Deploy on Render

1. **Sign up** at [render.com](https://render.com) (use GitHub to sign in)

2. **Create a PostgreSQL Database**:
   - Click "New +" → "PostgreSQL"
   - Name: `kingsalomon-db`
   - Database: `kingsalomon_academy`
   - Region: Choose closest to you
   - Plan: **Free**
   - Click "Create Database"
   - **Copy the Internal Database URL** (you'll need it later)

3. **Create a Web Service**:
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select your repository
   - Configure:
     - **Name**: `kingsalomon-academy`
     - **Environment**: `Python 3`
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn --bind 0.0.0.0:$PORT wsgi:app`
     - **Plan**: **Free**

4. **Set Environment Variables**:
   Click "Environment" tab and add:
   ```
   FLASK_ENV=production
   SECRET_KEY=your-super-secret-key-change-this-12345
   DATABASE_URL=<paste-your-postgresql-internal-url-here>
   PORT=10000
   MAIL_SERVER=smtp.gmail.com
   MAIL_PORT=587
   MAIL_USE_TLS=True
   MAIL_USERNAME=your-email@gmail.com
   MAIL_PASSWORD=your-app-password
   ```

5. **Deploy**:
   - Click "Create Web Service"
   - Wait for deployment (5-10 minutes)
   - Your app will be live at: `https://kingsalomon-academy.onrender.com`

### Step 3: Initialize Database

After first deployment, visit:
```
https://your-app-url.onrender.com
```

The app will automatically create the database tables and admin user:
- **Username**: `admin`
- **Password**: `admin123`

**⚠️ IMPORTANT**: Change the admin password immediately after first login!

---

## 🎯 Option 2: PythonAnywhere

**PythonAnywhere** is beginner-friendly with a free tier.

### Step 1: Sign Up

1. Go to [pythonanywhere.com](https://www.pythonanywhere.com)
2. Sign up for a **Beginner account** (free)

### Step 2: Upload Your Code

1. **Open a Bash console** in PythonAnywhere
2. **Clone from GitHub** (recommended):
   ```bash
   cd ~
   git clone https://github.com/YOUR_USERNAME/kingsalomon-academy.git
   cd kingsalomon-academy
   ```

   OR **Upload files manually**:
   - Go to "Files" tab
   - Upload all project files

### Step 3: Set Up Virtual Environment

```bash
cd ~/kingsalomon-academy
python3.10 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Step 4: Configure Database

1. Go to "Databases" tab
2. Click "Initialize MySQL"
3. Create a database:
   ```sql
   CREATE DATABASE kingsalomon_academy CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```

### Step 5: Create Web App

1. Go to "Web" tab
2. Click "Add a new web app"
3. Choose "Manual configuration"
4. Select Python 3.10
5. Click "Next" → "Next"

### Step 6: Configure WSGI File

1. Click on the WSGI file link
2. Replace content with:
   ```python
   import sys
   import os

   # Add your project directory to the path
   project_home = '/home/YOUR_USERNAME/kingsalomon-academy'
   if project_home not in sys.path:
       sys.path.insert(0, project_home)

   # Activate virtual environment
   activate_this = '/home/YOUR_USERNAME/kingsalomon-academy/venv/bin/activate_this.py'
   with open(activate_this) as f:
       exec(f.read(), {'__file__': activate_this})

   from wsgi import app as application
   ```

3. Replace `YOUR_USERNAME` with your PythonAnywhere username

### Step 7: Set Environment Variables

1. Go to "Web" tab → "Environment variables"
2. Add:
   ```
   FLASK_ENV=production
   SECRET_KEY=your-super-secret-key-change-this
   DATABASE_URL=mysql://YOUR_USERNAME:YOUR_PASSWORD@YOUR_USERNAME.mysql.pythonanywhere-services.com/YOUR_USERNAME$kingsalomon_academy
   ```

### Step 8: Reload Web App

1. Go to "Web" tab
2. Click "Reload" button
3. Visit your app: `https://YOUR_USERNAME.pythonanywhere.com`

---

## 🎯 Option 3: Railway

**Railway** offers easy deployment with PostgreSQL.

### Step 1: Sign Up

1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub

### Step 2: Deploy

1. Click "New Project"
2. Select "Deploy from GitHub repo"
3. Choose your repository
4. Railway will auto-detect Python and deploy

### Step 3: Add PostgreSQL Database

1. Click "New" → "Database" → "Add PostgreSQL"
2. Railway will automatically set `DATABASE_URL` environment variable

### Step 4: Set Environment Variables

Go to "Variables" tab and add:
```
FLASK_ENV=production
SECRET_KEY=your-super-secret-key-change-this
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
```

### Step 5: Deploy

Railway will automatically deploy. Your app will be live at:
`https://your-app-name.up.railway.app`

---

## 🎯 Option 4: Fly.io

**Fly.io** offers global deployment with PostgreSQL.

### Step 1: Install Fly CLI

```bash
# Windows (PowerShell)
iwr https://fly.io/install.ps1 -useb | iex

# Mac/Linux
curl -L https://fly.io/install.sh | sh
```

### Step 2: Sign Up and Login

```bash
fly auth signup
fly auth login
```

### Step 3: Initialize Fly.io

```bash
cd your-project-directory
fly launch
```

Follow the prompts:
- App name: `kingsalomon-academy`
- Region: Choose closest
- PostgreSQL: Yes (free tier)
- Redis: No

### Step 4: Set Secrets

```bash
fly secrets set SECRET_KEY=your-super-secret-key-change-this
fly secrets set FLASK_ENV=production
fly secrets set MAIL_SERVER=smtp.gmail.com
fly secrets set MAIL_PORT=587
fly secrets set MAIL_USE_TLS=True
fly secrets set MAIL_USERNAME=your-email@gmail.com
fly secrets set MAIL_PASSWORD=your-app-password
```

### Step 5: Deploy

```bash
fly deploy
```

Your app will be live at: `https://kingsalomon-academy.fly.dev`

---

## 🔧 Common Configuration

### Database URL Conversion

Most free hosting platforms provide PostgreSQL. Your app automatically converts the database URL format.

### File Storage

**Important**: Free hosting platforms have **ephemeral file systems**. Uploaded files may be lost on restart.

**Solutions**:
1. Use cloud storage (AWS S3, Google Cloud Storage) - see `requirements-prod.txt`
2. Use external file storage services
3. For Render: Files persist on free tier, but backup regularly

### Email Configuration

For Gmail:
1. Enable 2-Factor Authentication
2. Generate App Password: [Google Account Settings](https://myaccount.google.com/apppasswords)
3. Use the app password in `MAIL_PASSWORD`

---

## ✅ Post-Deployment Checklist

- [ ] App is accessible via URL
- [ ] Database tables created (check logs)
- [ ] Admin user created (username: `admin`, password: `admin123`)
- [ ] **Changed admin password**
- [ ] Test user registration
- [ ] Test file upload
- [ ] Test login/logout
- [ ] Configure email settings (if using OTP)
- [ ] Set up regular backups (if possible)

---

## 🆘 Troubleshooting

### App Won't Start

1. **Check logs**:
   - Render: Dashboard → Logs
   - PythonAnywhere: Web tab → Error log
   - Railway: Deployments → View logs
   - Fly.io: `fly logs`

2. **Common issues**:
   - Missing environment variables
   - Database connection error
   - Port binding issue (use `$PORT` environment variable)

### Database Connection Error

1. **Check DATABASE_URL format**:
   - PostgreSQL: `postgresql://user:pass@host:port/dbname`
   - MySQL: `mysql://user:pass@host:port/dbname`

2. **Verify database is running** (on platforms like Render)

### File Upload Not Working

1. **Check directory permissions**
2. **Verify UPLOAD_FOLDER path**
3. **Check file size limits**

---

## 📞 Need Help?

- Check platform-specific documentation
- Review application logs
- Test locally first with same configuration

---

## 🎉 Success!

Your King Salomon Academy Media Management System is now live on free hosting!

**Remember to**:
1. Change admin password immediately
2. Configure email for OTP (optional)
3. Set up backups if possible
4. Monitor your app regularly

**Welcome to the cloud!** ☁️

