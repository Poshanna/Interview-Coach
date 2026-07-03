import axios from "axios";

// Use environment variable for API URL, default to localhost for development
const API_BASE_URL = import.meta.env.VITE_API_URL || "http://127.0.0.1:8003";

const api = axios.create({
    baseURL: API_BASE_URL
});

export default api;
