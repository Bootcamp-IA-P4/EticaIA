import { useState } from 'react';
import { Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import ArticleDetail from './pages/ArticleDetail';
import Navbar from './components/Navbar';

export default function App() {
  const [searchTerm, setSearchTerm] = useState('');

  return (
    <>
      <Navbar onSearch={setSearchTerm} />
      <Routes>
        <Route path="/" element={<Home searchTerm={searchTerm} />} />
        <Route path="/article/:id" element={<ArticleDetail />} />
      </Routes>
    </>
  );
}
