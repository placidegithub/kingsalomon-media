# 🎓 Complete Beginner's Guide to Hosting Your App

This guide will walk you through **every single step** from start to finish. No prior experience needed!

---

## 📋 What You'll Need

- A computer with internet
- A GitHub account (we'll create one)
- An email address
- About 30 minutes of time

---

## 🚀 Step 1: Prepare Your Code

### 1.1 Open Your Project Folder

1. Open File Explorer (Windows) or Finder (Mac)
2. Navigate to: `C:\xampp\htdocs\King Salomon Academy System`
3. You should see files like `app.py`, `requirements.txt`, etc.

### 1.2 Check Important Files

Make sure these files exist in your folder:
- ✅ `app.py`
- ✅ `requirements.txt`
- ✅ `Procfile`
- ✅ `wsgi.py`
- ✅ `templates/` folder
- ✅ `static/` folder

**If all files are there, you're ready!** ✅

---

## 📦 Step 2: Set Up GitHub (If You Don't Have It)

### 2.1 Create GitHub Account

1. Go to [github.com](https://github.com)
2. Click **"Sign up"**
3. Enter your email, create a password
4. Choose a username (e.g., `yourname` or `kingsalomon-academy`)
5. Verify your email

### 2.2 Install Git (If Not Installed)

**Check if Git is installed:**
1. Open Command Prompt (Windows) or Terminal (Mac)
2. Type: `git --version`
3. If you see a version number, Git is installed ✅
4. If you see an error, install Git:

**Windows:**
- Download from: [git-scm.com/download/win](https://git-scm.com/download/win)
- Run the installer (use default settings)
- Restart your computer

**Mac:**
- Git usually comes pre-installed
- If not, install Xcode Command Line Tools

---

## 📤 Step 3: Push Your Code to GitHub

### 3.1 Open Command Prompt/Terminal in Your Project Folder

**Windows:**
1. Open File Explorer
2. Go to: `C:\xampp\htdocs\King Salomon Academy System`
3. Click in the address bar and type: `cmd` then press Enter
4. A black window (Command Prompt) will open

**Mac:**
1. Open Finder
2. Go to your project folder
3. Right-click → "New Terminal at Folder"

### 3.2 Initialize Git Repository

In the Command Prompt/Terminal, type these commands **one by one** (press Enter after each):

```bash
git init
```

You should see: `Initialized empty Git repository...`

### 3.3 Add All Files

```bash
git add .
```

(No output is normal - it means it worked!)

### 3.4 Create First Commit

```bash
git commit -m "Initial commit - ready for deployment"
```

You might see a message about setting your name/email. If so, run:

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

Then run the commit command again.

### 3.5 Create Repository on GitHub

1. Go to [github.com](https://github.com) and log in
2. Click the **"+"** icon (top right) → **"New repository"**
3. Fill in:
   - **Repository name**: `kingsalomon-academy` (or any name you like)
   - **Description**: "King Salomon Academy Media Management System"
   - **Visibility**: Choose **Public** (free) or **Private**
   - **DO NOT** check "Initialize with README"
4. Click **"Create repository"**

### 3.6 Connect and Push Your Code

GitHub will show you commands. Use these (replace `YOUR_USERNAME` with your GitHub username):

```bash
git remote add origin https://github.com/YOUR_USERNAME/kingsalomon-academy.git
```

```bash
git branch -M main
```

```bash
git push -u origin main
```

**If asked for username/password:**
- Username: Your GitHub username
- Password: Use a **Personal Access Token** (not your GitHub password)
  - Go to: GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
  - Click "Generate new token"
  - Name it: "Deployment"
  - Check "repo" permission
  - Click "Generate token"
  - **Copy the token** (you won't see it again!)
  - Use this token as your password

**You should see:** `Writing objects: 100%` - Success! ✅

---

## 🌐 Step 4: Deploy to Render

### 4.1 Sign Up for Render

1. Go to [render.com](https://render.com)
2. Click **"Get Started for Free"**
3. Click **"Sign up with GitHub"**
4. Authorize Render to access your GitHub account
5. You're now logged in! ✅

### 4.2 Create PostgreSQL Database

1. In Render dashboard, click **"New +"** (top right)
2. Click **"PostgreSQL"**
3. Fill in:
   - **Name**: `kingsalomon-db`
   - **Database**: `kingsalomon_academy`
   - **User**: `kingsalomon_user`
   - **Region**: Choose closest to you (e.g., "Oregon (US West)")
   - **PostgreSQL Version**: Latest (14 or 15)
   - **Plan**: **Free**
4. Click **"Create Database"**
5. **Wait 2-3 minutes** for database to be created
6. Once created, click on the database name
7. Find **"Internal Database URL"** - it looks like:
   ```
   postgresql://kingsalomon_user:password@dpg-xxxxx-a.oregon-postgres.render.com/kingsalomon_academy
   ```
8. **COPY THIS URL** - you'll need it soon! 📋

### 4.3 Create Web Service

1. In Render dashboard, click **"New +"** again
2. Click **"Web Service"**
3. Click **"Connect account"** if you see GitHub connection option
4. Find and click your repository: `kingsalomon-academy`
5. Click **"Connect"**

### 4.4 Configure Web Service

Fill in these settings:

**Basic Settings:**
- **Name**: `kingsalomon-academy` (or any name you like)
- **Region**: Same as your database (e.g., "Oregon (US West)")
- **Branch**: `main`
- **Root Directory**: (leave empty)
- **Environment**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn --bind 0.0.0.0:$PORT wsgi:app`
- **Plan**: **Free**

**Advanced Settings:**
- Click **"Advanced"** to expand
- **Auto-Deploy**: Yes (deploys automatically when you push code)

### 4.5 Set Environment Variables

**Before clicking "Create Web Service"**, scroll down to **"Environment Variables"** section.

Click **"Add Environment Variable"** for each of these:

1. **FLASK_ENV**
   - Key: `FLASK_ENV`
   - Value: `production`

2. **SECRET_KEY**
   - Key: `SECRET_KEY`
   - Value: `change-this-to-a-random-secret-key-12345abcdef` (make it long and random!)

3. **DATABASE_URL**
   - Key: `DATABASE_URL`
   - Value: **Paste the Internal Database URL you copied earlier**

4. **PORT** (optional, but recommended)
   - Key: `PORT`
   - Value: `10000`

**Optional - For Email (if you want OTP to work):**

5. **MAIL_SERVER**
   - Key: `MAIL_SERVER`
   - Value: `smtp.gmail.com`

6. **MAIL_PORT**
   - Key: `MAIL_PORT`
   - Value: `587`

7. **MAIL_USE_TLS**
   - Key: `MAIL_USE_TLS`
   - Value: `True`

8. **MAIL_USERNAME**
   - Key: `MAIL_USERNAME`
   - Value: `your-email@gmail.com`

9. **MAIL_PASSWORD**
   - Key: `MAIL_PASSWORD`
   - Value: `your-gmail-app-password` (see email setup below)

### 4.6 Deploy!

1. Review all settings
2. Click **"Create Web Service"** at the bottom
3. **Wait 5-10 minutes** for deployment
   - You'll see build logs in real-time
   - Look for: "Build successful" ✅
   - Then: "Your service is live at..." ✅

### 4.7 Get Your App URL

Once deployment is complete, you'll see:
- **Your service is live at**: `https://kingsalomon-academy.onrender.com`

**Copy this URL!** This is your live website! 🎉

---

## ✅ Step 5: Test Your Deployment

### 5.1 Visit Your Website

1. Open a web browser
2. Go to your Render URL (e.g., `https://kingsalomon-academy.onrender.com`)
3. You should see your homepage! ✅

**Note**: First visit might take 30-60 seconds (free tier apps "sleep" after inactivity)

### 5.2 Test Login

1. Click **"Login"** or go to: `https://your-app.onrender.com/login`
2. Login with:
   - **Username**: `admin`
   - **Password**: `admin123`
3. You should be logged in! ✅

### 5.3 Change Admin Password (IMPORTANT!)

1. After logging in, go to Admin Panel
2. Or create a new admin account with a secure password
3. **This is very important for security!**

### 5.4 Test File Upload

1. Go to Dashboard
2. Try uploading a test image
3. If it works, your deployment is successful! ✅

---

## 🔧 Step 6: Troubleshooting

### Problem: Build Failed

**Check:**
1. Go to Render dashboard → Your service → "Logs" tab
2. Look for error messages
3. Common issues:
   - Missing dependencies in `requirements.txt`
   - Syntax errors in code
   - Wrong Python version

**Solution:**
- Fix the error in your code
- Push changes to GitHub
- Render will automatically redeploy

### Problem: App Won't Start

**Check:**
1. Go to "Logs" tab in Render
2. Look for errors like "Port already in use" or "Database connection failed"

**Solutions:**
- Verify `DATABASE_URL` is correct
- Check `Procfile` has correct command
- Ensure `wsgi.py` exists

### Problem: Database Connection Error

**Check:**
1. Verify `DATABASE_URL` environment variable is set
2. Make sure database is running (green status in Render)
3. Check the URL format is correct

**Solution:**
- Copy the Internal Database URL again
- Make sure it starts with `postgresql://`
- Update the environment variable

### Problem: Can't Access Website

**Check:**
1. Is the service status "Live" (green)?
2. Are there any error messages in logs?

**Solutions:**
- Wait a bit longer (first deployment takes time)
- Check if service is sleeping (free tier)
- Refresh the page

### Problem: Files Not Uploading

**Check:**
1. Check logs for permission errors
2. Verify upload folder exists

**Solution:**
- This is normal on free tier - files may be lost on restart
- Consider using cloud storage for production

---

## 📧 Optional: Set Up Email (For OTP)

If you want email OTP to work:

### 6.1 Gmail Setup

1. Go to [myaccount.google.com](https://myaccount.google.com)
2. Click **"Security"** → **"2-Step Verification"** (enable it)
3. Go to **"App passwords"**
4. Click **"Select app"** → **"Mail"**
5. Click **"Select device"** → **"Other"** → Type "Render"
6. Click **"Generate"**
7. **Copy the 16-character password**
8. Use this in `MAIL_PASSWORD` environment variable

---

## 🎉 Success Checklist

- [ ] Code pushed to GitHub
- [ ] Database created on Render
- [ ] Web service created on Render
- [ ] Environment variables set
- [ ] Deployment successful
- [ ] Website is accessible
- [ ] Can login with admin account
- [ ] Changed admin password
- [ ] Tested file upload

**If all checked, congratulations! Your app is live!** 🎊

---

## 🔄 Making Updates

When you want to update your app:

1. Make changes to your code locally
2. In Command Prompt (in your project folder):
   ```bash
   git add .
   git commit -m "Updated my app"
   git push
   ```
3. Render will automatically detect changes and redeploy
4. Wait 5-10 minutes for new deployment

---

## 📞 Need Help?

1. **Check Render Logs**: Dashboard → Your service → Logs
2. **Check GitHub**: Make sure code is pushed correctly
3. **Verify Environment Variables**: All required variables are set
4. **Test Locally First**: Run `python app.py` to check for errors

---

## 🎓 What You Learned

✅ How to use Git and GitHub
✅ How to deploy a Flask app
✅ How to set up a PostgreSQL database
✅ How to configure environment variables
✅ How to deploy to cloud hosting

**You're now a developer who can deploy apps!** 🚀

---

**Your app is live at**: `https://your-app-name.onrender.com`

**Remember:**
- Free tier apps sleep after 15 minutes of inactivity
- First request after sleep takes 30-60 seconds
- Files may be lost on restart (use cloud storage for production)
- Monitor your usage to stay within free tier limits

**Congratulations on your first deployment!** 🎉

