# 🚀 King Salomon Academy - Production Deployment Guide

This guide will help you deploy the King Salomon Academy Media Management System to production.

## 📋 Prerequisites

### System Requirements
- **Operating System**: Linux (Ubuntu 20.04+), Windows Server, or macOS
- **Python**: 3.8 or higher
- **RAM**: Minimum 2GB (4GB recommended)
- **Storage**: 10GB+ free space
- **Network**: Stable internet connection

### Software Requirements
- Python 3.8+
- pip (Python package manager)
- Git (for code deployment)
- Nginx (for web server)
- PostgreSQL or MySQL (for production database)

## 🎯 Deployment Options

### Option 1: Traditional Server Deployment

#### Step 1: Prepare Server
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python and dependencies
sudo apt install python3 python3-pip python3-venv nginx postgresql postgresql-contrib -y

# Create application user
sudo useradd -m -s /bin/bash kingsalomon
sudo usermod -aG www-data kingsalomon
```

#### Step 2: Deploy Application
```bash
# Switch to application user
sudo su - kingsalomon

# Clone repository
git clone https://github.com/your-repo/kingsalomon-academy.git
cd kingsalomon-academy

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements-prod.txt

# Configure environment
cp env.example .env
nano .env  # Edit with your settings
```

#### Step 3: Configure Database
```bash
# Create database
sudo -u postgres createdb kingsalomon_academy
sudo -u postgres createuser kingsalomon_user
sudo -u postgres psql -c "ALTER USER kingsalomon_user PASSWORD 'your_secure_password';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE kingsalomon_academy TO kingsalomon_user;"
```

#### Step 4: Run Deployment Script
```bash
# Make script executable
chmod +x deploy.sh

# Run deployment
./deploy.sh
```

### Option 2: Docker Deployment

#### Step 1: Install Docker
```bash
# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

#### Step 2: Deploy with Docker
```bash
# Clone repository
git clone https://github.com/your-repo/kingsalomon-academy.git
cd kingsalomon-academy

# Configure environment
cp env.example .env
nano .env  # Edit with your settings

# Start services
docker-compose up -d

# Check status
docker-compose ps
```

### Option 3: Cloud Deployment

#### AWS EC2 Deployment
1. **Launch EC2 Instance**
   - Choose Ubuntu 20.04 LTS
   - Select t3.medium or larger
   - Configure security groups (ports 22, 80, 443)

2. **Connect and Deploy**
   ```bash
   ssh -i your-key.pem ubuntu@your-ec2-ip
   # Follow traditional server deployment steps
   ```

#### Google Cloud Platform
1. **Create VM Instance**
   - Choose Ubuntu 20.04 LTS
   - Select e2-medium or larger
   - Configure firewall rules

2. **Deploy Application**
   ```bash
   # Follow traditional server deployment steps
   ```

#### DigitalOcean Droplet
1. **Create Droplet**
   - Choose Ubuntu 20.04 LTS
   - Select 2GB RAM or larger
   - Add SSH key

2. **Deploy Application**
   ```bash
   # Follow traditional server deployment steps
   ```

## 🔧 Configuration

### Environment Variables (.env file)
```bash
# Flask Configuration
FLASK_ENV=production
SECRET_KEY=your-super-secret-key-change-this
FLASK_DEBUG=False

# Database Configuration
DATABASE_URL=postgresql://username:password@localhost:5432/kingsalomon_academy

# Security Settings
SESSION_COOKIE_SECURE=True
SESSION_COOKIE_HTTPONLY=True
SESSION_COOKIE_SAMESITE=Lax

# File Upload
MAX_CONTENT_LENGTH=524288000  # 500MB
UPLOAD_FOLDER=static/uploads
```

### Nginx Configuration
1. **SSL Certificate**
   ```bash
   # Install Certbot
   sudo apt install certbot python3-certbot-nginx -y
   
   # Get SSL certificate
   sudo certbot --nginx -d your-domain.com
   ```

2. **Configure Nginx**
   ```bash
   # Copy nginx configuration
   sudo cp nginx.conf /etc/nginx/sites-available/kingsalomon
   sudo ln -s /etc/nginx/sites-available/kingsalomon /etc/nginx/sites-enabled/
   sudo nginx -t
   sudo systemctl reload nginx
   ```

## 🔒 Security Configuration

### Firewall Setup
```bash
# Configure UFW
sudo ufw allow ssh
sudo ufw allow 80
sudo ufw allow 443
sudo ufw enable
```

### Database Security
```bash
# Secure PostgreSQL
sudo -u postgres psql
ALTER USER postgres PASSWORD 'strong_password';
\q
```

### Application Security
1. **Change default admin password**
2. **Use strong SECRET_KEY**
3. **Enable HTTPS only**
4. **Regular security updates**

## 📊 Monitoring and Maintenance

### Log Monitoring
```bash
# Application logs
tail -f logs/access.log
tail -f logs/error.log

# System logs
sudo journalctl -u kingsalomon-academy -f
```

### Database Backup
```bash
# Create backup script
cat > backup.sh << 'EOF'
#!/bin/bash
pg_dump kingsalomon_academy > backups/backup_$(date +%Y%m%d_%H%M%S).sql
find backups/ -name "backup_*.sql" -mtime +7 -delete
EOF

chmod +x backup.sh

# Schedule daily backups
crontab -e
# Add: 0 2 * * * /path/to/backup.sh
```

### Performance Monitoring
```bash
# Install monitoring tools
sudo apt install htop iotop nethogs -y

# Monitor resources
htop
iotop
nethogs
```

## 🚀 Launch Checklist

### Pre-Launch
- [ ] Domain name configured
- [ ] SSL certificate installed
- [ ] Database configured and tested
- [ ] Admin password changed
- [ ] Environment variables set
- [ ] Firewall configured
- [ ] Backup system in place

### Post-Launch
- [ ] Test all functionality
- [ ] Monitor logs for errors
- [ ] Check performance metrics
- [ ] Verify backup system
- [ ] Test file uploads/downloads
- [ ] Check mobile responsiveness

## 🆘 Troubleshooting

### Common Issues

#### Application Won't Start
```bash
# Check service status
sudo systemctl status kingsalomon-academy

# Check logs
sudo journalctl -u kingsalomon-academy -f

# Restart service
sudo systemctl restart kingsalomon-academy
```

#### Database Connection Issues
```bash
# Check database status
sudo systemctl status postgresql

# Test connection
psql -h localhost -U kingsalomon_user -d kingsalomon_academy
```

#### File Upload Issues
```bash
# Check permissions
ls -la static/uploads/

# Fix permissions
sudo chown -R www-data:www-data static/uploads/
sudo chmod -R 755 static/uploads/
```

#### SSL Certificate Issues
```bash
# Check certificate
sudo certbot certificates

# Renew certificate
sudo certbot renew --dry-run
```

## 📞 Support

### Getting Help
- **Documentation**: Check this deployment guide
- **Logs**: Check application and system logs
- **Community**: GitHub Issues
- **Email**: support@kingsalomon.ac.rw

### Emergency Contacts
- **System Administrator**: admin@kingsalomon.ac.rw
- **Technical Support**: tech@kingsalomon.ac.rw

---

## 🎉 Success!

Your King Salomon Academy Media Management System is now deployed and ready for use!

**Access your system at**: https://your-domain.com
**Admin login**: username=admin, password=admin123 (change immediately!)

Remember to:
1. Change the admin password
2. Configure email notifications
3. Set up regular backups
4. Monitor system performance
5. Keep the system updated

**Welcome to the future of media management at King Salomon Academy!** 🎓
