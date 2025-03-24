import { Link } from 'react-router-dom';

export default function ArticleCard({ article }) {
  return (
    <div style={styles.card}>
      <h3 style={styles.title}>{article.title}</h3>
      <p style={styles.topic}>🧠 {article.topic}</p>
      {article.excerpt && <p style={styles.excerpt}>{article.excerpt}</p>}
      <div style={styles.links}>
        <a href={article.link} target="_blank" rel="noopener noreferrer" style={styles.link}>
          Leer original
        </a>
        <Link to={`/article/${article._id}`} style={styles.detailLink}>
          Ver detalle
        </Link>
      </div>
    </div>
  );
}

const styles = {
  card: {
    background: '#e0e0e0',
    borderRadius: '15px',
    padding: '20px',
    marginBottom: '20px',
    boxShadow: '9px 9px 16px #bebebe, -9px -9px 16px #ffffff',
    transition: 'transform 0.2s ease-in-out',
  },
  title: {
    fontSize: '1.3rem',
    marginBottom: '10px',
    color: '#333',
  },
  topic: {
    fontSize: '0.9rem',
    color: '#666',
    marginBottom: '10px',
  },
  excerpt: {
    fontSize: '1rem',
    color: '#444',
    marginBottom: '15px',
  },
  links: {
    display: 'flex',
    justifyContent: 'space-between',
    marginTop: '10px',
  },
  link: {
    textDecoration: 'none',
    color: '#0077cc',
    fontWeight: 'bold',
  },
  detailLink: {
    textDecoration: 'none',
    color: '#00aa88',
    fontWeight: 'bold',
  }
};
