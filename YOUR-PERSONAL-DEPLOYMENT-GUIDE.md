# 🚀 Your Personal Deployment Guide

**Created for:** placidehenry0@gmail.com  
**GitHub Username:** kingsalomon  
**Location:** Rwanda  
**Best Server Region:** Europe (closest to Rwanda)

---

## ✅ What's Already Done

- ✅ All code files are ready
- ✅ Your SECRET_KEY has been generated (check `.env.template`)
- ✅ All configuration files are prepared
- ✅ Git is installed and ready

---

## 📦 Step 1: Push Code to GitHub (10 minutes)

### 1.1 Open Command Prompt in Your Project

1. Press `Windows Key + R`
2. Type: `cmd`
3. Press Enter
4. Type this command and press Enter:
   ```bash
   cd "C:\xampp\htdocs\King Salomon Academy System"
   ```

### 1.2 Check Git Status

Type this command:
```bash
git status
```

If you see "nothing to commit", your code is ready. If you see files listed, continue to step 1.3.

### 1.3 Add and Commit Your Code

Run these commands **one by one**:

```bash
git add .
```

```bash
git commit -m "Ready for deployment to Render"
```

### 1.4 Create GitHub Account

1. Go to: **[github.com/signup](https://github.com/signup)**
2. Enter your email: **placidehenry0@gmail.com**
3. Create a password (make it strong!)
4. Username: **kingsalomon**
   - If "kingsalomon" is taken, GitHub will suggest alternatives like:
     - `kingsalomon1`
     - `kingsalomon-academy`
     - `kingsalomon2024`
   - Pick one you like!
5. Verify your email (check your inbox)

### 1.5 Create Repository on GitHub

1. After logging in, click the **"+"** icon (top right)
2. Click **"New repository"**
3. Fill in:
   - **Repository name**: `kingsalomon-academy`
   - **Description**: `King Salomon Academy Media Management System`
   - **Visibility**: Choose **Public** (free) or **Private**
   - **DO NOT** check "Initialize with README"
   - **DO NOT** add .gitignore or license
4. Click **"Create repository"**

### 1.6 Connect and Push Your Code

GitHub will show you some commands. In your Command Prompt, run these:

**First, set your Git identity (if not already set):**
```bash
git config --global user.name "kingsalomon"
git config --global user.email "placidehenry0@gmail.com"
```

**Then connect to GitHub:**
```bash
git remote add origin https://github.com/kingsalomon/kingsalomon-academy.git
```

**If you used a different username (like kingsalomon1), use that instead!**

**Set main branch:**
```bash
git branch -M main
```

**Push your code:**
```bash
git push -u origin main
```

**When asked for credentials:**
- **Username**: `kingsalomon` (or whatever username you chose)
- **Password**: You need a **Personal Access Token** (not your GitHub password)

### 1.7 Create Personal Access Token

1. Go to: **[github.com/settings/tokens](https://github.com/settings/tokens)**
2. Click **"Generate new token"** → **"Generate new token (classic)"**
3. Fill in:
   - **Note**: `Deployment Token`
   - **Expiration**: `90 days` (or longer)
   - **Select scopes**: Check **"repo"** (this gives full repository access)
4. Click **"Generate token"**
5. **COPY THE TOKEN IMMEDIATELY** (you won't see it again!)
   - It looks like: `ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`
6. Go back to Command Prompt
7. When asked for password, **paste the token** (not your GitHub password)
8. Press Enter

**You should see:** `Writing objects: 100%` - Success! ✅

---

## 🌐 Step 2: Deploy to Render (15 minutes)

### 2.1 Sign Up for Render

1. Go to: **[render.com](https://render.com)**
2. Click **"Get Started for Free"**
3. Click **"Sign up with GitHub"**
4. Authorize Render to access your GitHub account
5. You're logged in! ✅

### 2.2 Create PostgreSQL Database

1. In Render dashboard, click **"New +"** (top right)
2. Click **"PostgreSQL"**
3. Fill in:
   - **Name**: `kingsalomon-db`
   - **Database**: `kingsalomon_academy`
   - **User**: `kingsalomon_user`
   - **Region**: Choose **"Frankfurt (EU Central)"** or **"Ireland (EU West)"** (closest to Rwanda)
   - **PostgreSQL Version**: Latest (15 or 16)
   - **Plan**: **Free**
4. Click **"Create Database"**
5. **Wait 2-3 minutes** for database to be created
6. Once created, click on the database name: `kingsalomon-db`
7. Scroll down to find **"Internal Database URL"**
8. It looks like:
   ```
   postgresql://kingsalomon_user:password@dpg-xxxxx-a.frankfurt-postgres.render.com/kingsalomon_academy
   ```
9. **CLICK THE COPY BUTTON** next to "Internal Database URL"
10. **SAVE THIS SOMEWHERE** - you'll need it in the next step! 📋

### 2.3 Create Web Service

1. In Render dashboard, click **"New +"** again
2. Click **"Web Service"**
3. You should see your GitHub repositories
4. Find and click: **"kingsalomon/kingsalomon-academy"**
5. Click **"Connect"**

### 2.4 Configure Web Service

Fill in these **exact** settings:

**Basic Settings:**
- **Name**: `kingsalomon-academy`
- **Region**: Same as your database (Frankfurt or Ireland)
- **Branch**: `main`
- **Root Directory**: (leave empty)
- **Environment**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn --bind 0.0.0.0:$PORT wsgi:app`
- **Plan**: **Free**

**Advanced Settings:**
- Click **"Advanced"** to expand
- **Auto-Deploy**: `Yes` ✅

### 2.5 Set Environment Variables

**IMPORTANT:** Before clicking "Create Web Service", scroll down to **"Environment Variables"** section.

Click **"Add Environment Variable"** for each of these (one by one):

**Variable 1:**
- **Key**: `FLASK_ENV`
- **Value**: `production`
- Click **"Add"**

**Variable 2:**
- **Key**: `SECRET_KEY`
- **Value**: Open `.env.template` file in your project folder and copy the SECRET_KEY
- It looks like: `-{18FH1KKA-i=[FYkYacF,S*8{0LU-YbD"Ip#TvC`[G6k25w#V`
- Paste it here
- Click **"Add"**

**Variable 3:**
- **Key**: `DATABASE_URL`
- **Value**: Paste the Internal Database URL you copied earlier
- It should start with: `postgresql://`
- Click **"Add"**

**Variable 4:**
- **Key**: `PORT`
- **Value**: `10000`
- Click **"Add"**

**Optional - For Email (if you want OTP to work later):**

**Variable 5:**
- **Key**: `MAIL_SERVER`
- **Value**: `smtp.gmail.com`
- Click **"Add"**

**Variable 6:**
- **Key**: `MAIL_PORT`
- **Value**: `587`
- Click **"Add"**

**Variable 7:**
- **Key**: `MAIL_USE_TLS`
- **Value**: `True`
- Click **"Add"**

**Variable 8:**
- **Key**: `MAIL_USERNAME`
- **Value**: `placidehenry0@gmail.com`
- Click **"Add"**

**Variable 9:**
- **Key**: `MAIL_PASSWORD`
- **Value**: (You'll need to create a Gmail App Password - see email setup below)
- Click **"Add"**

### 2.6 Deploy!

1. Scroll to the bottom
2. Review all settings
3. Click **"Create Web Service"** (blue button)
4. **Watch the magic happen!** ✨
   - You'll see build logs in real-time
   - Look for: `Collecting Flask...`
   - Then: `Building wheels...`
   - Finally: `Build successful` ✅
   - Then: `Starting service...`
   - Finally: `Your service is live at...` ✅

### 2.7 Get Your App URL

Once deployment is complete, you'll see:
- **Your service is live at**: `https://kingsalomon-academy.onrender.com`

**COPY THIS URL!** This is your live website! 🎉

**Note:** Free tier apps may take 30-60 seconds to wake up on first visit.

---

## ✅ Step 3: Test Your Deployment (5 minutes)

### 3.1 Visit Your Website

1. Open a web browser
2. Go to: `https://kingsalomon-academy.onrender.com`
3. **Wait 30-60 seconds** (first visit wakes up the app)
4. You should see your homepage! ✅

### 3.2 Test Login

1. Click **"Login"** or go to: `https://kingsalomon-academy.onrender.com/login`
2. Login with:
   - **Username**: `admin`
   - **Password**: `admin123`
3. You should be logged in! ✅

### 3.3 Change Admin Password (IMPORTANT!)

1. After logging in, go to Admin Panel
2. Change the password to something secure
3. **This is very important for security!**

### 3.4 Test File Upload

1. Go to Dashboard
2. Try uploading a test image
3. If it works, your deployment is successful! ✅

---

## 📧 Optional: Set Up Gmail for OTP

If you want email OTP to work:

1. Go to: **[myaccount.google.com](https://myaccount.google.com)**
2. Click **"Security"** (left menu)
3. Enable **"2-Step Verification"** (if not already enabled)
4. Go back to Security
5. Find **"App passwords"** (under "Signing in to Google")
6. Click **"Select app"** → Choose **"Mail"**
7. Click **"Select device"** → Choose **"Other"** → Type: `Render`
8. Click **"Generate"**
9. **Copy the 16-character password** (looks like: `abcd efgh ijkl mnop`)
10. Go back to Render → Your service → Environment → Edit `MAIL_PASSWORD`
11. Paste the app password (remove spaces)
12. Save and redeploy

---

## 🔧 Troubleshooting

### Problem: Build Failed

**Solution:**
1. Go to Render dashboard → Your service → "Logs" tab
2. Look for error messages
3. Common issues:
   - Missing dependency: Add it to `requirements.txt`
   - Syntax error: Fix in your code
   - Wrong Python version: Check `runtime.txt`

### Problem: Can't Push to GitHub

**Solution:**
- Make sure you're using Personal Access Token (not password)
- Check your username is correct
- Try: `git remote -v` to see your remote URL

### Problem: Database Connection Error

**Solution:**
- Verify `DATABASE_URL` is set correctly
- Make sure database is running (green status)
- Check the URL starts with `postgresql://`

### Problem: App Won't Start

**Solution:**
- Check logs in Render dashboard
- Verify `PORT` environment variable is set
- Check `Procfile` has correct command

---

## 🎉 Success Checklist

- [ ] Code pushed to GitHub
- [ ] GitHub repository created: `github.com/kingsalomon/kingsalomon-academy`
- [ ] Database created on Render
- [ ] Web service created on Render
- [ ] All environment variables set
- [ ] Deployment successful
- [ ] Website is accessible: `https://kingsalomon-academy.onrender.com`
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

## 📞 Your Information Summary

- **Email**: placidehenry0@gmail.com
- **GitHub Username**: kingsalomon
- **GitHub Repository**: github.com/kingsalomon/kingsalomon-academy
- **Render Service**: kingsalomon-academy
- **Your App URL**: https://kingsalomon-academy.onrender.com
- **Admin Username**: admin
- **Admin Password**: admin123 (CHANGE THIS!)

---

## 🎓 What You've Accomplished

✅ Set up Git and GitHub
✅ Deployed a Flask application
✅ Set up a PostgreSQL database
✅ Configured environment variables
✅ Deployed to cloud hosting

**You're now a developer who can deploy apps!** 🚀

---

**Your app is live at**: `https://kingsalomon-academy.onrender.com`

**Remember:**
- Free tier apps sleep after 15 minutes of inactivity
- First request after sleep takes 30-60 seconds
- Files may be lost on restart (use cloud storage for production)
- Monitor your usage to stay within free tier limits

**Congratulations on your first deployment!** 🎉

---

**Need help?** Check the logs in Render dashboard or refer back to this guide!

