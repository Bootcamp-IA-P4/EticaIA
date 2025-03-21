import { useEffect, useState } from 'react';
import axios from 'axios';
import ArticleCard from '../components/ArticleCard';

export default function Home() {
  const [articles, setArticles] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/articles') // Ajusta el puerto si es necesario
      .then(res => setArticles(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h1>Artículos sobre IA y ética</h1>
      {articles.map(article => (
        <ArticleCard key={article._id} article={article} />
      ))}
    </div>
  );
}
