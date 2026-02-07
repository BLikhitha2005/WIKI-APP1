import QuizCardView from "./QuizCardView";

export default function DetailsModal({ data, onClose }) {
  return (
    <div className="modalOverlay" onClick={onClose}>
      <div className="modal" onClick={(e) => e.stopPropagation()}>
        <div className="modalHeader">
          <h3>Quiz Details</h3>
          <button onClick={onClose}>X</button>
        </div>
        <QuizCardView data={data} />
      </div>
    </div>
  );
}
