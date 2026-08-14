import React from 'react';
import '../styles/ResultBox.css';
import { formatClassName } from '../data/classMaping';

const ResultBox = ({ result, onClose }) => {
  if (!result) return null;

  const confidence = result.top_prediction.confidence;
  const confidencePercent = (confidence * 100).toFixed(1);

  return (
    <div className="result-overlay" onClick={onClose}>
      <div className="result-container" onClick={(e) => e.stopPropagation()}>
        <button 
          className="close-btn"
          onClick={onClose}
        >
          ✕
        </button>

        <div className="result-content">
          <div className="result-header">
            <h2>Analysis Result</h2>
            <p className="confidence">
              Confidence: {confidencePercent}%
            </p>
          </div>

          <div className="result-predictions">
            <h3>Top Predictions:</h3>
            {result.predictions && result.predictions.map((pred, idx) => (
              <div key={idx} className="prediction-item">
                <span className="pred-class">{pred.class}</span>
                <span className="pred-score">
                  {(pred.confidence * 100).toFixed(1)}%
                </span>
              </div>
            ))}
          </div>

          <div className="result-details">
            <div className="detail-box">
              <h4>Primary Class</h4>
              <p>{formatClassName(result.top_prediction.class)}</p>
            </div>

            <div className="detail-box">
              <h4>Causes & Symptoms</h4>
              <p>{result.top_prediction["causes & symptoms"]}</p>
            </div>

            <div className="detail-box">
              <h4>Treatment</h4>
              <p>{result.top_prediction.treatment}</p>
            </div>

            <div className="detail-box">
              <h4>Prevention</h4>
              <p>{result.top_prediction.prevention}</p>
            </div>
          </div>

          <div className="disclaimer">
            ⚠️ This is an AI prediction and should not replace professional medical advice.
          </div>

          <button className="close-action-btn" onClick={onClose}>
            ← Back to Browse Diseases
          </button>
        </div>
      </div>
    </div>
  );
};

export default ResultBox;