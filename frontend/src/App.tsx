import { useEffect, useState } from 'react';

type Overview = {
  revenue: number;
  orders: number;
  profit: number;
  new_customers: number;
  low_stock_products: number;
  expiring_products: number;
  top_products: Array<{ name: string; sales: number; revenue: number }>;
};

const formatMoney = (value: number) =>
  new Intl.NumberFormat('vi-VN', {
    style: 'currency',
    currency: 'VND',
    maximumFractionDigits: 0,
  }).format(value);

function App() {
  const [health, setHealth] = useState<string>('checking');
  const [overview, setOverview] = useState<Overview | null>(null);

  useEffect(() => {
    fetch('/api/health')
      .then((res) => res.json())
      .then((data) => setHealth(data.status || 'unknown'))
      .catch(() => setHealth('error'));

    fetch('/api/dashboard/overview')
      .then((res) => res.json())
      .then((data) => setOverview(data))
      .catch(() => setOverview(null));
  }, []);

  return (
    <div className="app-shell">
      <header className="topbar">
        <div>
          <p className="eyebrow">Phase 1</p>
          <h1>Cosmetics Sales Management</h1>
        </div>
        <div className={`status-pill ${health === 'ok' ? 'ok' : health === 'error' ? 'error' : 'pending'}`}>
          API: {health}
        </div>
      </header>

      <section className="stats-grid">
        <div className="card">
          <span>Total Revenue</span>
          <strong>{overview ? formatMoney(overview.revenue) : 'Loading...'}</strong>
        </div>
        <div className="card">
          <span>Total Orders</span>
          <strong>{overview ? overview.orders.toLocaleString('vi-VN') : 'Loading...'}</strong>
        </div>
        <div className="card">
          <span>Profit</span>
          <strong>{overview ? formatMoney(overview.profit) : 'Loading...'}</strong>
        </div>
        <div className="card">
          <span>New Customers</span>
          <strong>{overview ? overview.new_customers.toLocaleString('vi-VN') : 'Loading...'}</strong>
        </div>
      </section>

      <section className="panel">
        <h2>Operational alerts</h2>
        <ul>
          <li>Low stock: {overview ? overview.low_stock_products : 0} products</li>
          <li>Expiring soon: {overview ? overview.expiring_products : 0} products</li>
        </ul>
      </section>

      <section className="panel">
        <h2>Top selling products</h2>
        <div className="table-wrap">
          <table>
            <thead>
              <tr>
                <th>Product</th>
                <th>Sales</th>
                <th>Revenue</th>
              </tr>
            </thead>
            <tbody>
              {overview?.top_products.map((row) => (
                <tr key={row.name}>
                  <td>{row.name}</td>
                  <td>{row.sales}</td>
                  <td>{formatMoney(row.revenue)}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>
    </div>
  );
}

export default App;
