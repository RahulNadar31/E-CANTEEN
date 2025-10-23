# 🍽️ Smart Canteen Management System

A comprehensive full-stack web application for managing college canteen operations with role-based access, ID verification, and real-time order tracking.

## 🎯 Features

### 👨‍💼 Admin Panel
- **Fixed Login Credentials:** `rahulnadar2006@gmail.com` / `12345678`
- **Dashboard:** Revenue analytics, user statistics, order overview
- **User Management:** Approve/reject student/faculty registrations with ID verification
- **Menu Management:** Add/edit/delete food items with categories and pricing
- **Order Management:** View all orders, update status (Pending → Preparing → Ready)
- **Real-time Analytics:** Sales reports, popular items, revenue tracking

### 👨‍🎓 Student/Faculty Panel
- **Registration:** Name, email, PNR number, ID photo upload (JPG/PNG ≤ 2MB)
- **Login:** Only after admin verification
- **Digital Menu:** Browse available items with categories and filtering
- **Cart System:** Add/remove items, quantity management with localStorage persistence
- **Order Placement:** Secure order submission with total calculation
- **Order History:** Track previous orders with status
- **Profile Management:** View personal details and order history

## 🛠️ Technical Stack

- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5, FontAwesome
- **Backend:** Python Flask
- **Database:** SQLite3
- **File Storage:** Local folder for ID proofs
- **Authentication:** Session-based with role management

## 📁 Project Structure

```
smart_canteen/
├── app.py                          # Main Flask application
├── database.py                     # Database initialization & connection
├── auth.py                         # Authentication functions
├── requirements.txt                # Python dependencies
├── smart_canteen.db               # SQLite database
├── templates/                      # HTML templates
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── admin_dashboard.html
│   ├── student_dashboard.html
│   ├── menu_management.html
│   └── user_verification.html
├── static/                         # Static assets
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
└── uploads/                        # File uploads
    └── id_proofs/
```

## 🗃️ Database Schema

### Users Table
- `id` (PK), `name`, `email`, `pnr`, `password`, `role`, `id_photo_path`, `verified`, `created_at`

### Menu Table
- `item_id` (PK), `item_name`, `price`, `category`, `description`, `available`, `created_at`

### Orders Table
- `order_id` (PK), `user_id` (FK), `items` (JSON), `total_amount`, `payment_status`, `order_status`, `order_time`

### Admin Table
- `admin_id` (PK), `email`, `name`, `password` (fixed credentials)

## 🚀 Installation & Setup

### Prerequisites
- Python 3.7+
- pip (Python package installer)

### Installation Steps

1. **Clone/Download the project**
   ```bash
   # If using git
   git clone <repository-url>
   cd smart_canteen
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the application**
   - Open your browser and go to `http://localhost:5000`
   - The application will automatically initialize the database with sample data

## 🔐 Default Credentials

### Admin Login
- **Email:** `rahulnadar2006@gmail.com`
- **Password:** `12345678`

### Sample Menu Items
The system comes pre-loaded with sample menu items:
- Chicken Biryani (₹180)
- Paneer Butter Masala (₹160)
- Veg Fried Rice (₹120)
- Chicken Tikka (₹200)
- Gulab Jamun (₹60)
- Coke (₹40)
- And more...

## 🎨 Key Features

### 🔐 Security Features
- Role-based authentication
- ID photo verification system
- File upload validation (2MB limit, image types only)
- Session management
- Input validation and sanitization

### 📱 User Experience
- Responsive design for all devices
- Modern gradient UI with smooth animations
- Real-time cart management with localStorage
- Toast notifications for user feedback
- Category filtering for menu items
- Image preview for ID uploads

### ⚡ Performance Features
- Local storage for cart persistence
- Optimized database queries
- Efficient file handling
- Real-time order status updates

## 🔄 Workflow

1. **User Registration** → ID upload → Admin verification
2. **Admin Login** → Verify users → Manage menu → Monitor orders
3. **Student Login** → Browse menu → Add to cart → Place order
4. **Order Processing** → Status updates → Completion

## 📊 Admin Dashboard Features

- **Statistics Cards:** Total users, pending verifications, total orders, revenue
- **User Verification:** Approve/reject new registrations with ID photo review
- **Menu Management:** Add, edit, delete menu items with categories
- **Order Management:** View and update order statuses in real-time
- **Analytics:** Revenue tracking and order statistics

## 🛒 Student Dashboard Features

- **Menu Browsing:** Categorized menu with filtering options
- **Smart Cart:** Add/remove items with quantity management
- **Order History:** Track all previous orders with status
- **Profile Management:** View personal details and verification status

## 🎯 Advanced Features

- **Category Filtering:** Filter menu items by category (Main, Appetizer, Fast Food, Dessert, Beverage)
- **Cart Persistence:** Cart items saved in localStorage
- **Real-time Updates:** Order status updates without page refresh
- **File Validation:** Automatic image type and size validation
- **Responsive Design:** Mobile-first approach with Bootstrap 5

## 🔧 Configuration

### Database
The SQLite database is automatically created and initialized with:
- Sample menu items
- Default admin account
- Proper table relationships

### File Uploads
- ID photos stored in `uploads/id_proofs/`
- Maximum file size: 2MB
- Allowed formats: JPG, PNG, JPEG, GIF

## 🐛 Troubleshooting

### Common Issues

1. **Database not found**
   - Delete `smart_canteen.db` and restart the application
   - The database will be recreated automatically

2. **File upload issues**
   - Ensure `uploads/id_proofs/` directory exists
   - Check file size (must be ≤ 2MB)
   - Verify file format (JPG, PNG, JPEG, GIF only)

3. **Login issues**
   - Use correct admin credentials: `rahulnadar2006@gmail.com` / `12345678`
   - Ensure user account is verified by admin

## 📈 Future Enhancements

- QR code integration for digital menus
- Payment gateway integration
- Email notifications
- Advanced analytics and reporting
- Mobile app development
- Real-time chat support

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Developer

**Rahul Nadar**
- Email: rahulnadar2006@gmail.com
- GitHub: [Your GitHub Profile]

---

## 🎉 Getting Started

1. **Install dependencies:** `pip install -r requirements.txt`
2. **Run the app:** `python app.py`
3. **Open browser:** `http://localhost:5000`
4. **Admin login:** Use the credentials above
5. **Register as student:** Create account and wait for admin verification
6. **Start ordering:** Browse menu and place orders!

**Happy Ordering! 🍽️**