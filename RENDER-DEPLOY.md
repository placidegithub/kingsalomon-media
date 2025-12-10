# 🚀 Quick Deploy to Render

## Step-by-Step Guide (5 minutes)

### 1. Push to GitHub
```bash
git init
git add .
git commit -m "Ready for Render deployment"
git remote add origin https://github.com/YOUR_USERNAME/kingsalomon-academy.git
git push -u origin main
```

### 2. Create PostgreSQL Database on Render

1. Go to [render.com](https://render.com) and sign up
2. Click **"New +"** → **"PostgreSQL"**
3. Settings:
   - **Name**: `kingsalomon-db`
   - **Database**: `kingsalomon_academy`
   - **User**: `kingsalomon_user`
   - **Plan**: **Free**
4. Click **"Create Database"**
5. **Copy the Internal Database URL** (starts with `postgresql://`)

### 3. Create Web Service

1. Click **"New +"** → **"Web Service"**
2. Connect your GitHub account
3. Select your repository
4. Configure:
   - **Name**: `kingsalomon-academy`
   - **Environment**: `Python 3`
   - **Region**: Choose closest
   - **Branch**: `main`
   - **Root Directory**: (leave empty)
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn --bind 0.0.0.0:$PORT wsgi:app`
   - **Plan**: **Free**

### 4. Set Environment Variables

Click **"Environment"** tab, add:

```
FLASK_ENV=production
SECRET_KEY=change-this-to-a-random-secret-key-12345
DATABASE_URL=<paste-your-postgresql-internal-url-here>
PORT=10000
```

**Optional** (for email OTP):
```
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-gmail-app-password
```

### 5. Deploy

1. Click **"Create Web Service"**
2. Wait 5-10 minutes for first deployment
3. Your app will be live at: `https://kingsalomon-academy.onrender.com`

### 6. First Login

- Visit your app URL
- Login with:
  - **Username**: `admin`
  - **Password**: `admin123`
- **⚠️ CHANGE PASSWORD IMMEDIATELY!**

---

## ✅ That's It!

Your app is now live on Render's free tier!

**Note**: Free tier apps sleep after 15 minutes of inactivity. First request may take 30-60 seconds to wake up.

