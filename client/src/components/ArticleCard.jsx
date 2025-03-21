import { Link } from 'react-router-dom';

export default function ArticleCard({ article }) {
  return (
    <div style={styles.card}>
      <h2>{article.title}</h2>
      <p><strong>Fuente:</strong> {article.source}</p>
      <p>{article.summary}</p>
      <Link to={`/article/${article._id}`} style={styles.link}>Leer más</Link>
    </div>
  );
}

const styles = {
  card: {
    border: '1px solid #ddd',
    padding: '15px',
    marginBottom: '10px',
    borderRadius: '5px',
  },
  link: {
    color: 'blue',
    textDecoration: 'none',
  },
};
