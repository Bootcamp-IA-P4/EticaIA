import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

export default function ArticleDetail() {
  const { id } = useParams(); // Obtenemos el ID de la URL
  const [article, setArticle] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios.get(`${import.meta.env.VITE_API_URL}/articles/${id}`)
      .then(res => {
        setArticle(res.data);
        setLoading(false);
      })
      .catch(err => {
        console.error('Error al cargar el artículo:', err);
        setLoading(false);
      });
  }, [id]);

  if (loading) return <p>Cargando...</p>;
  if (!article) return <p>Artículo no encontrado.</p>;

  return (
    <div style={styles.container}>
      <h2>{article.title}</h2>
      <p><strong>Temática:</strong> {article.topic}</p>
      <a href={article.link} target="_blank" rel="noopener noreferrer">
        Ver artículo original
      </a>
    </div>
  );
}

const styles = {
  container: {
    padding: '20px',
    backgroundColor: '#fefefe',
    border: '1px solid #ddd',
    borderRadius: '8px',
    marginTop: '20px',
  }
};
