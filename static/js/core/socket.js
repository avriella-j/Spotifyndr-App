// Socket.IO client initialization
const socket = io();

socket.on('connect', () => {
    console.log('Connected to server');
});

socket.on('disconnect', () => {
    console.log('Disconnected from server');
});

socket.on('new_message', (message) => {
    // Handle new message
    console.log('New message:', message);
});

socket.on('notification', (notification) => {
    // Handle notification
    Toast.show(notification.title, notification.message);
});
