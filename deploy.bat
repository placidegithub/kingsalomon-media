@echo off
echo.
echo ================================================
echo   King Salomon Academy - Production Deployment
echo ================================================
echo.

REM Check if running as administrator
net session >nul 2>&1
if %errorLevel% == 0 (
    echo ❌ Please do not run this script as administrator
    pause
    exit /b 1
)

echo 📁 Creating directories...
if not exist "logs" mkdir logs
if not exist "static\uploads\images" mkdir static\uploads\images
if not exist "static\uploads\videos" mkdir static\uploads\videos
if not exist "backups" mkdir backups

echo 📦 Installing production dependencies...
pip install -r requirements-prod.txt

echo ⚙️ Creating environment configuration...
if not exist ".env" (
    copy env.example .env
    echo ⚠️  Please edit .env file with your production settings!
    echo    - Change SECRET_KEY
    echo    - Configure database URL
    echo    - Set admin password
)

echo 🗄️ Initializing database...
python -c "from app import app, db, User; exec(open('init_db.py').read())"

echo.
echo ✅ Deployment completed!
echo 🌐 Your application can be started with: python app.py
echo 👤 Admin login: username=admin, password=admin123
echo ⚠️  Remember to change the admin password!
echo.
echo 📋 For production deployment, consider:
echo    - Using IIS with FastCGI
echo    - Setting up SSL certificate
echo    - Configuring firewall rules
echo    - Setting up database backup
echo.
pause
