import axios from 'axios';

     const API_BASE_URL = 'http://localhost:8000';

     const api = axios.create({
         baseURL: API_BASE_URL,
         headers: {
             'Content-Type': 'application/json',
         },
     });

     export const getUsers = () => api.get('/users/');
     export const getBooks = () => api.get('/books/');
     export const getTransactions = () => api.get('/transactions/');
     export const getSubjects = () => api.get('/subjects/');
     export const searchBooks = (query) => api.get(`/search/books?query=${query}`);
     export const createTransaction = (transactionData) => api.post('/transactions/', transactionData);
     export const returnBook = (transactionId) => api.post(`/transactions/${transactionId}/return_book/`);
