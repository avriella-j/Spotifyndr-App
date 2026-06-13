// Follow button component
class FollowButton {
    constructor(button) {
        this.button = button;
        this.userId = button.dataset.userId;
        this.isFollowing = false;
        
        this.init();
    }
    
    init() {
        this.button.addEventListener('click', () => this.toggleFollow());
    }
    
    async toggleFollow() {
        if (this.isFollowing) {
            try {
                await API.delete(`/follows/${this.userId}`);
                this.isFollowing = false;
                this.button.textContent = 'Follow';
                this.button.classList.remove('following');
                Toast.success('Success', 'User unfollowed');
            } catch (error) {
                Toast.error('Error', 'Failed to unfollow user');
            }
        } else {
            try {
                await API.post(`/follows/${this.userId}`);
                this.isFollowing = true;
                this.button.textContent = 'Following';
                this.button.classList.add('following');
                Toast.success('Success', 'User followed');
            } catch (error) {
                Toast.error('Error', 'Failed to follow user');
            }
        }
    }
}

// Initialize follow buttons
document.querySelectorAll('.btn-follow').forEach(btn => {
    new FollowButton(btn);
});
