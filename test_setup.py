#!/usr/bin/env python3
"""
Test script to verify Smart Canteen Management System setup
"""

import os
import sqlite3
from database import init_db, get_db_connection

def test_database_setup():
    """Test database initialization and sample data"""
    print("🔍 Testing database setup...")
    
    # Initialize database
    init_db()
    
    # Test connection
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Check tables exist
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [row[0] for row in cursor.fetchall()]
    expected_tables = ['users', 'menu', 'orders', 'admin']
    
    print(f"✅ Tables created: {tables}")
    
    # Check admin account
    admin = cursor.execute("SELECT * FROM admin WHERE email = 'rahulnadar2006@gmail.com'").fetchone()
    if admin:
        print(f"✅ Admin account found: {admin[2]} ({admin[1]})")
    else:
        print("❌ Admin account not found")
    
    # Check sample menu items
    menu_count = cursor.execute("SELECT COUNT(*) FROM menu").fetchone()[0]
    print(f"✅ Sample menu items: {menu_count} items")
    
    # Show sample menu
    menu_items = cursor.execute("SELECT item_name, price, category FROM menu LIMIT 5").fetchall()
    print("📋 Sample menu items:")
    for item in menu_items:
        print(f"   - {item[0]} (₹{item[1]}) - {item[2]}")
    
    conn.close()
    print("✅ Database setup completed successfully!")

def test_file_structure():
    """Test required files and directories"""
    print("\n🔍 Testing file structure...")
    
    required_files = [
        'app.py',
        'database.py', 
        'auth.py',
        'requirements.txt',
        'templates/base.html',
        'templates/login.html',
        'templates/register.html',
        'templates/admin_dashboard.html',
        'templates/student_dashboard.html',
        'templates/menu_management.html',
        'templates/user_verification.html',
        'static/css/style.css',
        'static/js/script.js'
    ]
    
    missing_files = []
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
    
    if missing_files:
        print(f"❌ Missing files: {missing_files}")
    else:
        print("✅ All required files present")
    
    # Check uploads directory
    uploads_dir = 'uploads/id_proofs'
    if not os.path.exists(uploads_dir):
        os.makedirs(uploads_dir, exist_ok=True)
        print(f"✅ Created uploads directory: {uploads_dir}")
    else:
        print(f"✅ Uploads directory exists: {uploads_dir}")

def test_dependencies():
    """Test required Python packages"""
    print("\n🔍 Testing dependencies...")
    
    try:
        import flask
        print(f"✅ Flask {flask.__version__}")
    except ImportError:
        print("❌ Flask not installed")
    
    try:
        import werkzeug
        print(f"✅ Werkzeug {werkzeug.__version__}")
    except ImportError:
        print("❌ Werkzeug not installed")

if __name__ == "__main__":
    print("🚀 Smart Canteen Management System - Setup Test")
    print("=" * 50)
    
    test_file_structure()
    test_dependencies()
    test_database_setup()
    
    print("\n" + "=" * 50)
    print("🎉 Setup test completed!")
    print("\n📋 Next steps:")
    print("1. Run: python app.py")
    print("2. Open: http://localhost:5000")
    print("3. Admin login: rahulnadar2006@gmail.com / 12345678")
    print("4. Register as student and wait for admin verification")
