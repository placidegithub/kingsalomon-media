#!/bin/bash

# King Salomon Academy Media Management System
# Production Deployment Script

echo "🎓 King Salomon Academy - Production Deployment"
echo "=============================================="

# Check if running as root
if [ "$EUID" -eq 0 ]; then
    echo "❌ Please do not run this script as root"
    exit 1
fi

# Create necessary directories
echo "📁 Creating directories..."
mkdir -p logs
mkdir -p static/uploads/images
mkdir -p static/uploads/videos
mkdir -p backups

# Set permissions
echo "🔐 Setting permissions..."
chmod 755 static/uploads
chmod 755 static/uploads/images
chmod 755 static/uploads/videos
chmod 755 logs

# Install production dependencies
echo "📦 Installing production dependencies..."
pip install -r requirements-prod.txt

# Create environment file if it doesn't exist
if [ ! -f .env ]; then
    echo "⚙️ Creating environment configuration..."
    cp env.example .env
    echo "⚠️  Please edit .env file with your production settings!"
    echo "   - Change SECRET_KEY"
    echo "   - Configure database URL"
    echo "   - Set admin password"
fi

# Initialize database
echo "🗄️ Initializing database..."
python -c "
from app import app, db, User
with app.app_context():
    db.create_all()
    admin = User.query.filter_by(username='admin').first()
    if not admin:
        admin = User(username='admin', email='admin@kingsalomon.ac.rw', full_name='System Administrator', role='admin')
        admin.set_password('admin123')
        db.session.add(admin)
        db.session.commit()
        print('✅ Admin user created')
    else:
        print('✅ Admin user already exists')
"

# Create systemd service file
echo "🔧 Creating systemd service..."
sudo tee /etc/systemd/system/kingsalomon-academy.service > /dev/null <<EOF
[Unit]
Description=King Salomon Academy Media Management System
After=network.target

[Service]
Type=exec
User=www-data
Group=www-data
WorkingDirectory=$(pwd)
Environment=PATH=$(pwd)/venv/bin
ExecStart=$(pwd)/venv/bin/gunicorn --config gunicorn.conf.py wsgi:app
ExecReload=/bin/kill -s HUP \$MAINPID
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
EOF

# Enable and start service
echo "🚀 Starting service..."
sudo systemctl daemon-reload
sudo systemctl enable kingsalomon-academy
sudo systemctl start kingsalomon-academy

# Check service status
echo "📊 Checking service status..."
sudo systemctl status kingsalomon-academy --no-pager

echo ""
echo "✅ Deployment completed!"
echo "🌐 Your application should be running on: http://your-server-ip:8000"
echo "👤 Admin login: username=admin, password=admin123"
echo "⚠️  Remember to change the admin password!"
echo ""
echo "📋 Useful commands:"
echo "   sudo systemctl status kingsalomon-academy"
echo "   sudo systemctl restart kingsalomon-academy"
echo "   sudo systemctl stop kingsalomon-academy"
echo "   tail -f logs/access.log"
echo "   tail -f logs/error.log"
