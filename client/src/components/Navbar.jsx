export default function Navbar({ onSearch }) {
    return (
      <nav style={{ padding: '10px', background: '#333', color: '#fff' }}>
        <h2>EticaIA</h2>
        <input
          type="text"
          placeholder="Buscar artículo..."
          onChange={(e) => onSearch(e.target.value)}
          style={{ padding: '5px', marginLeft: '10px' }}
        />
      </nav>
    );
  }
  