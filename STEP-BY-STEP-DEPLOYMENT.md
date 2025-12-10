# 📝 Step-by-Step Deployment Checklist

Print this or keep it open while deploying. Check off each step as you complete it.

---

## ✅ Pre-Deployment Checklist

- [ ] Project folder is ready
- [ ] All files are in the project folder
- [ ] Internet connection is working
- [ ] Have 30-60 minutes available

---

## 📦 Phase 1: GitHub Setup (15 minutes)

### Step 1: Create GitHub Account
- [ ] Go to github.com
- [ ] Sign up with email
- [ ] Verify email address
- [ ] Choose username

### Step 2: Install Git (if needed)
- [ ] Check if Git is installed (`git --version`)
- [ ] If not, download from git-scm.com
- [ ] Install Git
- [ ] Restart computer

### Step 3: Push Code to GitHub
- [ ] Open Command Prompt in project folder
- [ ] Run: `git init`
- [ ] Run: `git add .`
- [ ] Run: `git commit -m "Initial commit"`
- [ ] Create repository on GitHub
- [ ] Run: `git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git`
- [ ] Run: `git push -u origin main`
- [ ] Code is now on GitHub ✅

---

## 🌐 Phase 2: Render Setup (20 minutes)

### Step 4: Sign Up for Render
- [ ] Go to render.com
- [ ] Sign up with GitHub
- [ ] Authorize Render
- [ ] Logged into Render dashboard ✅

### Step 5: Create Database
- [ ] Click "New +" → "PostgreSQL"
- [ ] Name: `kingsalomon-db`
- [ ] Database: `kingsalomon_academy`
- [ ] Plan: Free
- [ ] Click "Create Database"
- [ ] Wait for database to be ready
- [ ] Copy Internal Database URL
- [ ] Database created ✅

### Step 6: Create Web Service
- [ ] Click "New +" → "Web Service"
- [ ] Connect GitHub repository
- [ ] Select your repository
- [ ] Name: `kingsalomon-academy`
- [ ] Environment: Python 3
- [ ] Build Command: `pip install -r requirements.txt`
- [ ] Start Command: `gunicorn --bind 0.0.0.0:$PORT wsgi:app`
- [ ] Plan: Free

### Step 7: Set Environment Variables
- [ ] Add: `FLASK_ENV` = `production`
- [ ] Add: `SECRET_KEY` = (random long string)
- [ ] Add: `DATABASE_URL` = (paste database URL)
- [ ] Add: `PORT` = `10000`
- [ ] (Optional) Add email variables
- [ ] All variables set ✅

### Step 8: Deploy
- [ ] Click "Create Web Service"
- [ ] Watch build logs
- [ ] Wait for "Build successful"
- [ ] Wait for "Your service is live"
- [ ] Copy your app URL
- [ ] Deployment complete ✅

---

## ✅ Phase 3: Testing (10 minutes)

### Step 9: Test Website
- [ ] Open app URL in browser
- [ ] Homepage loads ✅
- [ ] Can see login page ✅

### Step 10: Test Login
- [ ] Go to login page
- [ ] Username: `admin`
- [ ] Password: `admin123`
- [ ] Successfully logged in ✅

### Step 11: Security
- [ ] Changed admin password ✅
- [ ] Tested file upload ✅
- [ ] Everything works ✅

---

## 🎉 Success!

- [ ] Website is live
- [ ] Can login
- [ ] Can upload files
- [ ] Admin panel works
- [ ] All features working

**Your app is successfully deployed!** 🚀

---

## 📝 Notes

**Your App URL**: _________________________________

**GitHub Repository**: _________________________________

**Render Dashboard**: https://dashboard.render.com

**Admin Username**: `admin`

**Admin Password**: (you changed it, right?)

---

## 🔄 Future Updates

When updating your app:
1. Make changes locally
2. Run: `git add .`
3. Run: `git commit -m "Description of changes"`
4. Run: `git push`
5. Render auto-deploys in 5-10 minutes

---

**Congratulations! You've successfully deployed your first web application!** 🎊

