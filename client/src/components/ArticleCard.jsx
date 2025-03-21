import { Link } from 'react-router-dom';

export default function ArticleCard({ article }) {
  return (
    <div style={styles.card}>
      <h2>{article.title}</h2>
      <p><strong>Temática:</strong> {article.topic}</p>
      <a href={article.link} target="_blank" rel="noopener noreferrer" style={styles.link}>
        Ver artículo original
      </a>
      <br />
      <Link to={`/article/${article._id}`} style={styles.detailLink}>
        Ver detalle interno
      </Link>
    </div>
  );
}

const styles = {
  card: {
    border: '1px solid #ddd',
    padding: '15px',
    marginBottom: '10px',
    borderRadius: '5px',
    backgroundColor: '#f9f9f9',
  },
  link: {
    color: 'blue',
    textDecoration: 'none',
  },
  detailLink: {
    color: 'green',
    fontSize: '0.9rem',
    textDecoration: 'underline',
  }
};
