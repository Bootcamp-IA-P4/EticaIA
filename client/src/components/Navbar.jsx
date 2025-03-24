import { Link } from 'react-router-dom';

export default function Navbar({ onSearch }) {
  return (
    <nav style={styles.nav}>
      <h2 style={styles.logo}>🧠 EticaIA</h2>
      <input
        type="text"
        placeholder="Buscar artículo..."
        onChange={(e) => onSearch(e.target.value)}
        style={styles.input}
      />
      <Link to="/" style={styles.link}>Inicio</Link>
    </nav>
  );
}

const styles = {
  nav: {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'space-between',
    padding: '18px 30px',
    background: '#e0e0e0',
    borderRadius: '16px',
    margin: '20px',
    boxShadow: '6px 6px 12px #bebebe, -6px -6px 12px #ffffff',
  },
  logo: {
    fontSize: '1.6rem',
    fontWeight: 600,
    margin: 0,
    color: '#333',
  },
  input: {
    flex: 1,
    maxWidth: '300px',
    margin: '0 20px',
    padding: '10px 14px',
    border: 'none',
    borderRadius: '12px',
    backgroundColor: '#e0e0e0',
    boxShadow: 'inset 3px 3px 6px #bebebe, inset -3px -3px 6px #ffffff',
    fontSize: '1rem',
    outline: 'none',
    color: '#333',
  },
  link: {
    textDecoration: 'none',
    color: '#0077cc',
    fontWeight: 500,
  }
};
