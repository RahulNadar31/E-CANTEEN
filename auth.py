from database import get_db_connection
import sqlite3
import os

def verify_admin_login(email, password):
    """Verify admin login credentials"""
    conn = get_db_connection()
    admin = conn.execute(
        'SELECT * FROM admin WHERE email = ?', (email,)
    ).fetchone()
    conn.close()
    
    if admin and admin['password'] == password:
        return admin
    return None

def verify_user_login(email, password):
    """Verify user login credentials"""
    conn = get_db_connection()
    user = conn.execute(
        'SELECT * FROM users WHERE email = ? AND verified = 1', (email,)
    ).fetchone()
    conn.close()
    
    if user and user['password'] == password:
        return user
    return None

def register_user(name, email, pnr, password, id_photo_path=None):
    """Register new user (unverified by default)"""
    conn = get_db_connection()
    
    try:
        conn.execute('''
            INSERT INTO users (name, email, pnr, password, id_photo_path)
            VALUES (?, ?, ?, ?, ?)
        ''', (name, email, pnr, password, id_photo_path))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def get_pending_verifications():
    """Get users pending verification"""
    conn = get_db_connection()
    users = conn.execute(
        'SELECT * FROM users WHERE verified = 0'
    ).fetchall()
    conn.close()
    return users

def verify_user(user_id):
    """Approve user verification"""
    conn = get_db_connection()
    conn.execute(
        'UPDATE users SET verified = 1 WHERE id = ?', (user_id,)
    )
    conn.commit()
    conn.close()

def reject_user(user_id):
    """Reject and delete user"""
    conn = get_db_connection()
    
    # First get photo path to delete file
    user = conn.execute(
        'SELECT id_photo_path FROM users WHERE id = ?', (user_id,)
    ).fetchone()
    
    # Delete user
    conn.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()
    
    # Delete photo file if exists (path stored relative to uploads/)
    if user and user['id_photo_path']:
        rel_path = user['id_photo_path']
        abs_path = os.path.join('uploads', rel_path)
        if os.path.exists(abs_path):
            os.remove(abs_path)

def verify_kitchen_login(email, password):
    """Verify kitchen staff login credentials"""
    conn = get_db_connection()
    staff = conn.execute(
        'SELECT * FROM kitchen_staff WHERE email = ?', (email,)
    ).fetchone()
    conn.close()
    
    if staff and staff['password'] == password:
        return staff
    return None