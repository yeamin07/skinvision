import React from 'react';
import '../styles/DiseaseDetailModal.css';

const DiseaseDetailModal = ({ disease, onClose }) => {
  if (!disease) return null;

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-container" onClick={(e) => e.stopPropagation()}>
        <button className="modal-close-btn" onClick={onClose}>
          ✕
        </button>

        <div className="modal-image">
          <img src={disease.image} alt={disease.name} />
        </div>

        <div className="modal-content">
          <h2>{disease.name}</h2>

          <div className="modal-detail">
            <h4>💡 Causes & Symptoms</h4>
            <p>{disease.causes}</p>
            <p className="sub-detail">{disease.symptoms}</p>
          </div>

          <div className="modal-detail">
            <h4>💊 Treatment</h4>
            <p>{disease.treatment}</p>
          </div>

          <div className="modal-detail">
            <h4>🛡️ Prevention</h4>
            <p>{disease.prevention}</p>
          </div>

          {/* <button className="modal-cta-btn" onClick={onClose}>
            Upload Your Image to Get Analysis
          </button> */}
        </div>
      </div>
    </div>
  );
};

export default DiseaseDetailModal;