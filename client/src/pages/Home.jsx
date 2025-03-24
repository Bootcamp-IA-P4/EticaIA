import { useEffect, useState } from 'react';
import axios from 'axios';
import ArticleCard from '../components/ArticleCard';

export default function Home({ searchTerm }) {
    const [articles, setArticles] = useState([]);
  
    useEffect(() => {
      axios.get('http://localhost:8000/articles')
        .then(res => setArticles(res.data))
        .catch(err => console.error(err));
    }, []);
  
    const filteredArticles = articles.filter(article =>
      article.title.toLowerCase().includes(searchTerm.toLowerCase())
    );
  
    return (
      <div>
        <h1>Artículos sobre IA y ética</h1>
        {filteredArticles.map(article => (
          <ArticleCard key={article._id} article={article} />
        ))}
      </div>
    );
  }
  