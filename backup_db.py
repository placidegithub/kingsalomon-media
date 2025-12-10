#!/usr/bin/env python3
"""
King Salomon Academy Media Management System
Database Backup Script
"""

import shutil
import os
from datetime import datetime


def backup_database():
    """Create a backup of the database"""
    print("🎓 King Salomon Academy - Database Backup")
    print("=" * 40)

    # Check if database exists
    db_path = 'instance/academy_media.db'
    if not os.path.exists(db_path):
        print("❌ Database file not found!")
        return

    # Create backup directory
    backup_dir = 'backups'
    os.makedirs(backup_dir, exist_ok=True)

    # Generate backup filename with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_filename = f'academy_media_backup_{timestamp}.db'
    backup_path = os.path.join(backup_dir, backup_filename)

    # Copy database file
    shutil.copy2(db_path, backup_path)

    print(f"✅ Database backed up successfully!")
    print(f"📁 Backup location: {backup_path}")
    print(f"📊 Backup size: {os.path.getsize(backup_path) / 1024:.2f} KB")


if __name__ == '__main__':
    backup_database()
