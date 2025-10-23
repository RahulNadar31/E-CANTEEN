import sqlite3
import os
from datetime import datetime

def init_db():
    """Initialize database with required tables"""
    conn = sqlite3.connect('smart_canteen.db')
    cursor = conn.cursor()
    
    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            pnr VARCHAR(20) NOT NULL,
            password VARCHAR(255) NOT NULL,
            role VARCHAR(20) DEFAULT 'student',
            id_photo_path VARCHAR(255),
            verified BOOLEAN DEFAULT 0,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create menu table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS menu (
            item_id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name VARCHAR(100) NOT NULL,
            price DECIMAL(6,2) NOT NULL,
            available BOOLEAN DEFAULT 1,
            category VARCHAR(50) DEFAULT 'main',
            description TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create orders table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            items TEXT NOT NULL,
            total_amount DECIMAL(8,2) NOT NULL,
            payment_status VARCHAR(20) DEFAULT 'Pending',
            order_status VARCHAR(20) DEFAULT 'Pending',
            order_time DATETIME DEFAULT CURRENT_TIMESTAMP,
            estimated_time INTEGER DEFAULT 15,
            preparation_started DATETIME,
            preparation_completed DATETIME,
            notification_sent BOOLEAN DEFAULT 0,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    
    # Create admin table with fixed credentials
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS admin (
            admin_id INTEGER PRIMARY KEY,
            email VARCHAR(100) NOT NULL,
            name VARCHAR(100) NOT NULL,
            password VARCHAR(255) NOT NULL
        )
    ''')
    
    # Create kitchen staff table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS kitchen_staff (
            staff_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL,
            role VARCHAR(20) DEFAULT 'kitchen',
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create expenses table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
            description VARCHAR(255) NOT NULL,
            amount DECIMAL(8,2) NOT NULL,
            category VARCHAR(50) DEFAULT 'general',
            expense_date DATETIME DEFAULT CURRENT_TIMESTAMP,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Insert default admin if not exists
    cursor.execute('''
        INSERT OR IGNORE INTO admin (admin_id, email, name, password) 
        VALUES (1, 'rahulnadar2006@gmail.com', 'Rahul Nadar', '12345678')
    ''')
    
    # Insert default kitchen staff
    cursor.execute('''
        INSERT OR IGNORE INTO kitchen_staff (staff_id, name, email, password) 
        VALUES (1, 'Manasvi Kharpuse', 'manasvikharpuse2006@gmail.com', '12345678')
    ''')
    
    # Insert sample menu items
    sample_menu = [
        ('Chicken Biryani', 180, 'main', 'Aromatic basmati rice with tender chicken'),
        ('Paneer Butter Masala', 160, 'main', 'Cottage cheese in rich tomato gravy'),
        ('Veg Fried Rice', 120, 'main', 'Stir-fried rice with vegetables'),
        ('Chicken Tikka', 200, 'appetizer', 'Grilled marinated chicken'),
        ('Gulab Jamun', 60, 'dessert', 'Sweet milk dumplings in syrup'),
        ('Coke', 40, 'beverage', 'Refreshing carbonated drink'),
        ('Mutton Curry', 220, 'main', 'Spicy mutton curry with rice'),
        ('Veg Thali', 150, 'main', 'Complete vegetarian meal with dal, sabzi, rice, roti'),
        ('Chicken Burger', 120, 'fast_food', 'Juicy chicken patty with fresh vegetables'),
        ('Pizza Margherita', 180, 'fast_food', 'Classic pizza with tomato and mozzarella'),
        ('Ice Cream', 50, 'dessert', 'Vanilla ice cream'),
        ('Tea', 20, 'beverage', 'Hot masala tea'),
        ('Coffee', 30, 'beverage', 'Freshly brewed coffee')
    ]
    
    cursor.executemany('''
        INSERT OR IGNORE INTO menu (item_name, price, category, description)
        VALUES (?, ?, ?, ?)
    ''', sample_menu)

    # --- Lightweight migrations for existing databases ---
    def column_exists(table, column):
        info = cursor.execute(f"PRAGMA table_info({table})").fetchall()
        return any(col[1] == column for col in info)

    # Users table migrations
    if not column_exists('users', 'id_photo_path'):
        cursor.execute("ALTER TABLE users ADD COLUMN id_photo_path VARCHAR(255)")
    if not column_exists('users', 'verified'):
        cursor.execute("ALTER TABLE users ADD COLUMN verified BOOLEAN DEFAULT 0")

    # Orders table migrations
    if not column_exists('orders', 'payment_status'):
        cursor.execute("ALTER TABLE orders ADD COLUMN payment_status VARCHAR(20) DEFAULT 'Pending'")
    if not column_exists('orders', 'order_status'):
        cursor.execute("ALTER TABLE orders ADD COLUMN order_status VARCHAR(20) DEFAULT 'Pending'")
    if not column_exists('orders', 'order_time'):
        cursor.execute("ALTER TABLE orders ADD COLUMN order_time DATETIME DEFAULT CURRENT_TIMESTAMP")
    if not column_exists('orders', 'estimated_time'):
        cursor.execute("ALTER TABLE orders ADD COLUMN estimated_time INTEGER DEFAULT 15")
    if not column_exists('orders', 'preparation_started'):
        cursor.execute("ALTER TABLE orders ADD COLUMN preparation_started DATETIME")
    if not column_exists('orders', 'preparation_completed'):
        cursor.execute("ALTER TABLE orders ADD COLUMN preparation_completed DATETIME")
    if not column_exists('orders', 'notification_sent'):
        cursor.execute("ALTER TABLE orders ADD COLUMN notification_sent BOOLEAN DEFAULT 0")
    
    conn.commit()
    conn.close()
    print("Database initialized successfully!")

def get_db_connection():
    """Get database connection"""
    conn = sqlite3.connect('smart_canteen.db')
    conn.row_factory = sqlite3.Row
    return conn