// API client for making requests to backend
class API {
    static async get(endpoint) {
        const response = await fetch(`/api/v1${endpoint}`);
        return response.json();
    }
    
    static async post(endpoint, data) {
        const response = await fetch(`/api/v1${endpoint}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        return response.json();
    }
    
    static async put(endpoint, data) {
        const response = await fetch(`/api/v1${endpoint}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        return response.json();
    }
    
    static async delete(endpoint) {
        const response = await fetch(`/api/v1${endpoint}`, {
            method: 'DELETE'
        });
        return response.json();
    }
}
