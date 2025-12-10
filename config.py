"""
King Salomon Academy Media Management System
Configuration settings
"""

import os

class Config:
    """Base configuration"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'king-salomon-academy-2024-secure-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///academy_media.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = 'static/uploads'
    MAX_CONTENT_LENGTH = 500 * 1024 * 1024  # 500MB max file size
    
    # Allowed file extensions
    ALLOWED_IMAGE_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif', 'bmp', 'webp'}
    ALLOWED_VIDEO_EXTENSIONS = {'mp4', 'avi', 'mov', 'wmv', 'flv', 'webm', 'mkv'}
    
    # File categories
    FILE_CATEGORIES = {
        'general': 'General',
        'events': 'School Events',
        'academic': 'Academic',
        'sports': 'Sports',
        'cultural': 'Cultural',
        'graduation': 'Graduation'
    }
    
    # User roles
    USER_ROLES = {
        'student': 'Student',
        'teacher': 'Teacher',
        'staff': 'Staff',
        'admin': 'Administrator'
    }

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///academy_media_dev.db'

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    # Use environment variables for production
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///academy_media.db'

# Configuration mapping
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
