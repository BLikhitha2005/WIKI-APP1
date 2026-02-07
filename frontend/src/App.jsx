import { useState } from "react";
import GenerateTab from "./GenerateTab";
import HistoryTab from "./HistoryTab";
import "./app.css";

export default function App() {
  const [tab, setTab] = useState("generate");

  return (
    <div className="container">
      <h1 className="title">AI Wiki Quiz Generator</h1>

      <div className="tabs">
        <button className={tab === "generate" ? "active" : ""} onClick={() => setTab("generate")}>
          Generate Quiz
        </button>
        <button className={tab === "history" ? "active" : ""} onClick={() => setTab("history")}>
          Past Quizzes (History)
        </button>
      </div>

      {tab === "generate" ? <GenerateTab /> : <HistoryTab />}
    </div>
  );
}
