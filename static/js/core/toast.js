// Toast notification system
class Toast {
    static show(title, message, type = 'info') {
        const container = document.getElementById('toast-container');
        if (!container) return;
        
        const toast = document.createElement('div');
        toast.className = `toast toast-${type}`;
        toast.innerHTML = `
            <h4>${title}</h4>
            <p>${message}</p>
        `;
        
        container.appendChild(toast);
        
        setTimeout(() => {
            toast.remove();
        }, 3000);
    }
    
    static success(title, message) {
        this.show(title, message, 'success');
    }
    
    static error(title, message) {
        this.show(title, message, 'error');
    }
}
