import { useState } from "react";
import QuizCardView from "./QuizCardView";

const API = "http://127.0.0.1:8000";

export default function GenerateTab() {
  const [url, setUrl] = useState("");
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [err, setErr] = useState("");

  const generate = async () => {
    setErr("");
    setData(null);
    setLoading(true);
    try {
      const res = await fetch(`${API}/generate-quiz`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url }),
      });
      const json = await res.json();
      if (!res.ok) throw new Error(json.detail || "Failed");
      setData(json);
    } catch (e) {
      setErr(e.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <div className="inputRow">
        <input
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          placeholder="Paste Wikipedia URL (Example: https://en.wikipedia.org/wiki/Alan_Turing)"
        />
        <button onClick={generate} disabled={loading || !url}>
          {loading ? "Generating..." : "Generate Quiz"}
        </button>
      </div>

      {err && <div className="error">{err}</div>}
      {data && <QuizCardView data={data} />}
    </div>
  );
}
