import { useEffect, useState } from "react";
import axios from "axios";
import ArticleCard from "../components/ArticleCard";

export default function Home({ searchTerm }) {
  const [articles, setArticles] = useState([]);

  useEffect(() => {
    axios
      .get("http://localhost:8000/articles")
      .then((res) => setArticles(res.data))
      .catch((err) => console.error(err));
  }, []);

  const filteredArticles = articles.filter(article => {
    const term = searchTerm.toLowerCase();
    return (
      article.title.toLowerCase().includes(term) ||
      (article.excerpt && article.excerpt.toLowerCase().includes(term)) ||
      (article.topic && article.topic.toLowerCase().includes(term))
    );
  });

  return (
    <div style={{ padding: "20px", maxWidth: "800px", margin: "0 auto" }}>
      <h1 style={{ textAlign: "center" }}>Artículos sobre IA y ética</h1>
      {filteredArticles.map((article) => (
        <ArticleCard key={article._id} article={article} />
      ))}
    </div>
  );
}
