# 🚀 Smart Canteen Management System - Deployment Guide

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Web browser (Chrome, Firefox, Safari, Edge)

## 🛠️ Local Development Setup

### 1. Environment Setup

```bash
# Create virtual environment (recommended)
python -m venv canteen_env

# Activate virtual environment
# On Windows:
canteen_env\Scripts\activate
# On macOS/Linux:
source canteen_env/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`

## 🌐 Production Deployment

### Option 1: Using Gunicorn (Recommended for Linux/macOS)

1. **Install Gunicorn**
   ```bash
   pip install gunicorn
   ```

2. **Create WSGI file** (`wsgi.py`)
   ```python
   from app import app

   if __name__ == "__main__":
       app.run()
   ```

3. **Run with Gunicorn**
   ```bash
   gunicorn -w 4 -b 0.0.0.0:5000 wsgi:app
   ```

### Option 2: Using Waitress (Cross-platform)

1. **Install Waitress**
   ```bash
   pip install waitress
   ```

2. **Create production runner** (`run_production.py`)
   ```python
   from waitress import serve
   from app import app

   if __name__ == "__main__":
       serve(app, host="0.0.0.0", port=5000)
   ```

3. **Run production server**
   ```bash
   python run_production.py
   ```

## 🐳 Docker Deployment

### 1. Create Dockerfile

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p uploads/id_proofs

EXPOSE 5000

CMD ["python", "app.py"]
```

### 2. Build and Run

```bash
# Build image
docker build -t smart-canteen .

# Run container
docker run -p 5000:5000 smart-canteen
```

## ☁️ Cloud Deployment Options

### Heroku Deployment

1. **Create Procfile**
   ```
   web: gunicorn app:app
   ```

2. **Create runtime.txt**
   ```
   python-3.9.7
   ```

3. **Deploy to Heroku**
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

### AWS EC2 Deployment

1. **Launch EC2 instance**
2. **Install dependencies**
   ```bash
   sudo apt update
   sudo apt install python3-pip nginx
   pip3 install -r requirements.txt
   ```

3. **Configure Nginx**
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;
       
       location / {
           proxy_pass http://127.0.0.1:5000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

### DigitalOcean App Platform

1. **Connect GitHub repository**
2. **Configure build settings**
   - Build command: `pip install -r requirements.txt`
   - Run command: `python app.py`
3. **Deploy**

## 🔧 Configuration

### Environment Variables

Create `.env` file for production:

```env
FLASK_ENV=production
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///smart_canteen.db
UPLOAD_FOLDER=uploads/id_proofs
MAX_CONTENT_LENGTH=2097152
```

### Database Configuration

For production, consider using PostgreSQL:

```python
# In app.py, replace SQLite with PostgreSQL
import os
from sqlalchemy import create_engine

DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///smart_canteen.db')
engine = create_engine(DATABASE_URL)
```

## 🔒 Security Considerations

### 1. Change Default Credentials

```python
# In database.py, update admin credentials
cursor.execute('''
    INSERT OR IGNORE INTO admin (admin_id, email, name, password) 
    VALUES (1, 'your-email@domain.com', 'Your Name', 'your-secure-password')
''')
```

### 2. Enable HTTPS

```python
# In app.py
if __name__ == '__main__':
    app.run(debug=False, ssl_context='adhoc')  # For development
```

### 3. File Upload Security

```python
# Add file validation
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
MAX_FILE_SIZE = 2 * 1024 * 1024  # 2MB

def validate_file(file):
    if file and '.' in file.filename:
        ext = file.filename.rsplit('.', 1)[1].lower()
        return ext in ALLOWED_EXTENSIONS and len(file.read()) <= MAX_FILE_SIZE
    return False
```

## 📊 Monitoring and Logging

### 1. Add Logging

```python
import logging
from logging.handlers import RotatingFileHandler

if not app.debug:
    file_handler = RotatingFileHandler('logs/canteen.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
```

### 2. Health Check Endpoint

```python
@app.route('/health')
def health_check():
    return {'status': 'healthy', 'timestamp': datetime.now().isoformat()}
```

## 🔄 Backup Strategy

### 1. Database Backup

```bash
# Create backup script
#!/bin/bash
DATE=$(date +%Y%m%d_%H%M%S)
cp smart_canteen.db "backups/smart_canteen_$DATE.db"
```

### 2. File Backup

```bash
# Backup uploads directory
tar -czf "backups/uploads_$DATE.tar.gz" uploads/
```

## 🚨 Troubleshooting

### Common Issues

1. **Port already in use**
   ```bash
   # Find process using port 5000
   netstat -ano | findstr :5000
   # Kill process
   taskkill /PID <process_id> /F
   ```

2. **Database locked**
   ```bash
   # Stop application and restart
   # Or delete database file to recreate
   ```

3. **File upload issues**
   - Check directory permissions
   - Verify file size limits
   - Ensure uploads directory exists

### Performance Optimization

1. **Enable caching**
   ```python
   from flask_caching import Cache
   cache = Cache(app, config={'CACHE_TYPE': 'simple'})
   ```

2. **Database optimization**
   ```python
   # Add indexes
   cursor.execute('CREATE INDEX idx_user_email ON users(email)')
   cursor.execute('CREATE INDEX idx_order_user ON orders(user_id)')
   ```

## 📈 Scaling Considerations

### 1. Load Balancing

Use Nginx as reverse proxy:

```nginx
upstream canteen_backend {
    server 127.0.0.1:5000;
    server 127.0.0.1:5001;
    server 127.0.0.1:5002;
}
```

### 2. Database Scaling

- Migrate to PostgreSQL for better performance
- Implement database connection pooling
- Add read replicas for analytics

### 3. File Storage

- Move to cloud storage (AWS S3, Google Cloud Storage)
- Implement CDN for static assets
- Add image optimization

## 📞 Support

For deployment issues:

1. Check logs: `tail -f logs/canteen.log`
2. Verify dependencies: `pip list`
3. Test database: `python test_setup.py`
4. Check file permissions
5. Verify network connectivity

---

## 🎉 Deployment Checklist

- [ ] Dependencies installed
- [ ] Database initialized
- [ ] File permissions set
- [ ] Security configurations applied
- [ ] Backup strategy implemented
- [ ] Monitoring configured
- [ ] SSL certificate installed (production)
- [ ] Domain configured
- [ ] Performance testing completed

**Happy Deploying! 🚀**
