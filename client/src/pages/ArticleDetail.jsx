import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";

export default function ArticleDetail() {
  const { id } = useParams(); // Obtenemos el ID de la URL
  const [article, setArticle] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios
      .get(`${import.meta.env.VITE_API_URL}/articles/${id}`)
      .then((res) => {
        setArticle(res.data);
        setLoading(false);
      })
      .catch((err) => {
        console.error("Error al cargar el artículo:", err);
        setLoading(false);
      });
  }, [id]);

  if (loading) return <p>Cargando...</p>;
  if (!article) return <p>Artículo no encontrado.</p>;

  return (
    <div style={styles.container}>
      <h2 style={styles.title}>{article.title}</h2>
      <p style={styles.topic}>
        📌 <strong>Temática:</strong> {article.topic}
      </p>
      {article.excerpt && <p style={styles.excerpt}>{article.excerpt}</p>}
      <a
        href={article.link}
        target="_blank"
        rel="noopener noreferrer"
        style={styles.link}
      >
        Leer artículo completo
      </a>
    </div>
  );
}

const styles = {
    container: {
      padding: '30px',
      margin: '40px auto',
      maxWidth: '800px',
      backgroundColor: '#e0e0e0',
      borderRadius: '15px',
      boxShadow: '9px 9px 16px #bebebe, -9px -9px 16px #ffffff',
    },
    title: {
      fontSize: '1.8rem',
      marginBottom: '20px',
    },
    topic: {
      fontSize: '1rem',
      color: '#666',
      marginBottom: '10px',
    },
    excerpt: {
      fontStyle: 'italic',
      color: '#444',
      marginBottom: '20px',
      lineHeight: 1.6,
    },
    link: {
      textDecoration: 'none',
      fontWeight: 'bold',
      color: '#0077cc',
    }
  };
  