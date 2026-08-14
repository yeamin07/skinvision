import React from 'react';
import '../styles/DiseaseCard.css';

const DiseaseCard = ({ disease, onClick }) => {
  return (
    <div 
      className="disease-card"
      onClick={() => onClick(disease)}
      role="button"
      tabIndex={0}
      onKeyPress={(e) => {
        if (e.key === 'Enter') onClick(disease);
      }}
    >
      <div className="card-image-container">
        <img src={disease.image} alt={disease.name} />
        <div className="card-overlay"></div>
      </div>
      <div className="card-content">
        <h3>{disease.name}</h3>
        <p className="small-text">Click to learn more →</p>
      </div>
    </div>
  );
};

export default DiseaseCard;