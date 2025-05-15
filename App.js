import React from 'react';
     import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
     import Navbar from './components/Navbar';
     import BookList from './components/BookList';
     import UserList from './components/UserList';
     import TransactionList from './components/TransactionList';
     import Dashboard from './components/Dashboard';
     import ReportGeneration from './components/ReportGeneration';

     function App() {
         return (
             <Router>
                 <div className="min-h-screen bg-gray-100">
                     <Navbar />
                     <Routes>
                         <Route path="/" element={<Dashboard />} />
                         <Route path="/books" element={<BookList />} />
                         <Route path="/users" element={<UserList />} />
                         <Route path="/transactions" element={<TransactionList />} />
                         <Route path="/reports" element={<ReportGeneration />} />
                     </Routes>
                 </div>
             </Router>
         );
     }

     export default App;
