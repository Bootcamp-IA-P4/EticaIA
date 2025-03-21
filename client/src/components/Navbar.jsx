import { Link } from 'react-router-dom';

export default function Navbar() {
  return (
    <nav style={styles.navbar}>
      <h1>EticaIA</h1>
      <div>
        <Link to="/" style={styles.link}>Inicio</Link>
      </div>
    </nav>
  );
}

const styles = {
  navbar: {
    display: 'flex',
    justifyContent: 'space-between',
    padding: '10px 20px',
    backgroundColor: '#333',
    color: 'white',
  },
  link: {
    color: 'white',
    textDecoration: 'none',
    marginLeft: '10px',
  },
};
