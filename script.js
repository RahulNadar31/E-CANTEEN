// General JavaScript functions for Smart Canteen

// Auto-dismiss alerts after 5 seconds
document.addEventListener('DOMContentLoaded', function() {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });
});

// Form validation enhancement
function validateForm(formId) {
    const form = document.getElementById(formId);
    const inputs = form.querySelectorAll('input[required], select[required], textarea[required]');
    
    let isValid = true;
    inputs.forEach(input => {
        if (!input.value.trim()) {
            input.classList.add('is-invalid');
            isValid = false;
        } else {
            input.classList.remove('is-invalid');
        }
    });
    
    return isValid;
}

// Image preview for file inputs
function setupImagePreview(inputId, previewId) {
    const input = document.getElementById(inputId);
    const preview = document.getElementById(previewId);
    
    if (input && preview) {
        input.addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    preview.src = e.target.result;
                    preview.style.display = 'block';
                };
                reader.readAsDataURL(file);
            }
        });
    }
}

// Initialize when document is ready
document.addEventListener('DOMContentLoaded', function() {
    // Setup image preview for ID photo upload
    setupImagePreview('id_photo', 'idPhotoPreview');
    
    // Enhance form submissions
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const requiredInputs = this.querySelectorAll('[required]');
            requiredInputs.forEach(input => {
                if (!input.value.trim()) {
                    input.classList.add('is-invalid');
                }
            });
        });
    });
    
    // Remove invalid class when user starts typing
    const inputs = document.querySelectorAll('input, select, textarea');
    inputs.forEach(input => {
        input.addEventListener('input', function() {
            this.classList.remove('is-invalid');
        });
    });
});

// Utility function for confirmation dialogs
function confirmAction(message) {
    return confirm(message || 'Are you sure you want to proceed?');
}

// Cart management functions (for student dashboard)
window.cartManager = {
    cart: [],
    
    addItem: function(itemId, itemName, price) {
        const existingItem = this.cart.find(item => item.id === itemId);
        
        if (existingItem) {
            existingItem.quantity += 1;
        } else {
            this.cart.push({
                id: itemId,
                name: itemName,
                price: price,
                quantity: 1
            });
        }
        
        this.updateDisplay();
        this.showToast(`${itemName} added to cart!`, 'success');
    },
    
    removeItem: function(itemId) {
        this.cart = this.cart.filter(item => item.id !== itemId);
        this.updateDisplay();
    },
    
    updateDisplay: function() {
        // This will be implemented in the specific page
        console.log('Cart updated:', this.cart);
    },
    
    showToast: function(message, type = 'info') {
        // Simple toast notification
        const toast = document.createElement('div');
        toast.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
        toast.style.cssText = 'top: 20px; right: 20px; z-index: 1050; min-width: 300px;';
        toast.innerHTML = `
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        `;
        
        document.body.appendChild(toast);
        
        setTimeout(() => {
            toast.remove();
        }, 3000);
    }
};