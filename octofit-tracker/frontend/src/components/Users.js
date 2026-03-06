import { useEffect, useState } from 'react';

function Users() {
  const [items, setItems] = useState([]);
  const [error, setError] = useState('');
  const endpoint = process.env.REACT_APP_CODESPACE_NAME
    ? `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/users/`
    : 'http://localhost:8000/api/users/';

  useEffect(() => {
    const fetchUsers = async () => {
      try {
        console.log('Users endpoint:', endpoint);
        const response = await fetch(endpoint);
        if (!response.ok) {
          throw new Error(`Request failed with status ${response.status}`);
        }

        const data = await response.json();
        console.log('Users fetched data:', data);

        const normalized = Array.isArray(data)
          ? data
          : Array.isArray(data.results)
            ? data.results
            : [];

        setItems(normalized);
      } catch (fetchError) {
        setError(fetchError.message);
      }
    };

    fetchUsers();
  }, [endpoint]);

  const renderTableCells = (item) => {
    if (!item || typeof item !== 'object') return <td>{String(item)}</td>;
    
    return Object.values(item).map((value, idx) => (
      <td key={idx}>
        {typeof value === 'object' ? JSON.stringify(value) : String(value || '-')}
      </td>
    ));
  };

  const getTableHeaders = () => {
    return items.length > 0 ? Object.keys(items[0]) : [];
  };

  return (
    <section className="section">
      <div className="card content-card">
        <div className="card-body">
          <h2>👤 Users</h2>
          
          {error && (
            <div className="alert alert-danger alert-dismissible fade show" role="alert">
              <strong>Error:</strong> {error}
              <button type="button" className="btn-close" onClick={() => setError('')}></button>
            </div>
          )}

          {!error && items.length === 0 ? (
            <div className="empty-state">
              <div className="empty-state-icon">🚀</div>
              <p>No users found.</p>
              <small className="text-muted">Register to create a user profile.</small>
            </div>
          ) : (
            <div className="table-responsive">
              <table className="table data-table table-striped table-hover">
                <thead>
                  <tr>
                    {getTableHeaders().map((header) => (
                      <th key={header} scope="col">{header}</th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  {items.map((item, index) => (
                    <tr key={item.id ?? item._id ?? index}>
                      {renderTableCells(item)}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </div>
      </div>
    </section>
  );
}

export default Users;
