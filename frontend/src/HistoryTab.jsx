import { useEffect, useState } from "react";
import DetailsModal from "./DetailsModal";

const API = "http://127.0.0.1:8000";

export default function HistoryTab() {
  const [list, setList] = useState([]);
  const [selected, setSelected] = useState(null);

  const load = async () => {
    const res = await fetch(`${API}/history`);
    const json = await res.json();
    setList(json);
  };

  useEffect(() => {
    load();
  }, []);

  return (
    <div>
      <div className="historyHeader">
        <h2>History</h2>
        <button onClick={load}>Refresh</button>
      </div>

      <table className="table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Title</th>
            <th>URL</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          {list.map((r) => (
            <tr key={r.id}>
              <td>{r.id}</td>
              <td>{r.title}</td>
              <td className="urlCell">{r.url}</td>
              <td>
                <button onClick={() => setSelected(r)}>Details</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      {selected && <DetailsModal data={selected} onClose={() => setSelected(null)} />}
    </div>
  );
}
