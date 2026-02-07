import { useState } from "react";

export default function QuizCardView({ data }) {
  const [takeMode, setTakeMode] = useState(false);
  const [answers, setAnswers] = useState({});
  const [submitted, setSubmitted] = useState(false);

  const score = () => {
    let s = 0;
    data.quiz.forEach((q, i) => {
      if (answers[i] === q.answer) s++;
    });
    return s;
  };

  return (
    <div className="card">
      <h2>{data.title}</h2>
      <p className="small">{data.url}</p>
      {data.summary && <p>{data.summary}</p>}

      <div className="toggleRow">
        <button onClick={() => { setTakeMode(!takeMode); setSubmitted(false); setAnswers({}); }}>
          {takeMode ? "View Answers Mode" : "Take Quiz Mode"}
        </button>
        {takeMode && (
          <button onClick={() => setSubmitted(true)} disabled={submitted}>
            {submitted ? `Score: ${score()}/${data.quiz.length}` : "Submit"}
          </button>
        )}
      </div>

      <h3>Quiz</h3>
      {data.quiz.map((q, idx) => (
        <div className="qCard" key={idx}>
          <div className="qTop">
            <p><b>Q{idx + 1}.</b> {q.question}</p>
            <span className={`badge ${q.difficulty}`}>{q.difficulty}</span>
          </div>

          <div className="options">
  {q.options.map((opt, j) => (
    <label key={j} className="opt">
      {takeMode && (
        <input
          type="radio"
          name={`q-${idx}`}
          checked={answers[idx] === opt}
          onChange={() => setAnswers({ ...answers, [idx]: opt })}
          disabled={submitted}
        />
      )}
      <span>{opt}</span>
    </label>
  ))}
</div>

{/* ✅ Instant feedback */}
{takeMode && answers[idx] && !submitted && (
  <p
    style={{
      marginTop: "6px",
      fontWeight: "bold",
      color: answers[idx] === q.answer ? "green" : "red",
    }}
  >
    {answers[idx] === q.answer ? "Correct ✅" : "Wrong ❌"}
  </p>
)}


           {!takeMode && (
            <>
              <p><b>Answer:</b> {q.answer}</p>
              <p className="small"><b>Explanation:</b> {q.explanation}</p>
            </>
          )}  

          {takeMode && submitted && (
            <>
              <p><b>Correct Answer:</b> {q.answer}</p>
              <p className="small"><b>Explanation:</b> {q.explanation}</p>
            </>
          )}
        </div>
      ))}

      <h3>Related Topics</h3>
      <div className="chips">
        {(data.related_topics || []).map((t, i) => (
          <span key={i} className="chip">{t}</span>
        ))}
      </div>
    </div>
  );
}
