// Swipe functionality for explore page
class SwipeCard {
    constructor(element) {
        this.element = element;
        this.isDragging = false;
        this.startX = 0;
        this.currentX = 0;
        
        this.init();
    }
    
    init() {
        this.element.addEventListener('mousedown', this.startDrag.bind(this));
        this.element.addEventListener('mousemove', this.drag.bind(this));
        this.element.addEventListener('mouseup', this.endDrag.bind(this));
        this.element.addEventListener('mouseleave', this.endDrag.bind(this));
        
        // Touch events
        this.element.addEventListener('touchstart', this.startDrag.bind(this));
        this.element.addEventListener('touchmove', this.drag.bind(this));
        this.element.addEventListener('touchend', this.endDrag.bind(this));
    }
    
    startDrag(e) {
        this.isDragging = true;
        this.startX = e.type.includes('mouse') ? e.clientX : e.touches[0].clientX;
        this.element.classList.add('dragging');
    }
    
    drag(e) {
        if (!this.isDragging) return;
        
        this.currentX = e.type.includes('mouse') ? e.clientX : e.touches[0].clientX;
        const diff = this.currentX - this.startX;
        
        this.element.style.transform = `translateX(${diff}px) rotate(${diff * 0.1}deg)`;
    }
    
    endDrag() {
        if (!this.isDragging) return;
        
        this.isDragging = false;
        this.element.classList.remove('dragging');
        
        const diff = this.currentX - this.startX;
        
        if (Math.abs(diff) > 100) {
            // Swipe completed
            const liked = diff > 0;
            this.swipe(liked);
        } else {
            // Reset position
            this.element.style.transform = '';
        }
    }
    
    async swipe(liked) {
        const contentId = this.element.dataset.contentId;
        
        try {
            await API.post('/explore/swipe', { content_id: contentId, liked });
            this.element.remove();
        } catch (error) {
            Toast.error('Error', 'Failed to record swipe');
        }
    }
}
