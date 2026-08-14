import React from 'react';
import { FiActivity, FiZap, FiTarget } from 'react-icons/fi';
import '../styles/InfoSection.css';

const InfoSection = () => {
  const features = [
    {
      icon: <FiTarget size={32} />,
      title: 'Classes',
      value: '19',
      description: 'Skin disease classifications',
    },
    {
      icon: <FiActivity size={32} />,
      title: 'AI Model',
      value: 'EfficientNet',
      description: 'Advanced CNN architecture',
    },
    {
      icon: <FiZap size={32} />,
      title: 'Accuracy',
      value: 'Real-time',
      description: 'Instant skin analysis',
    },
  ];

  return (
    <section className="info-section">
      <div className="info-container">
        <div className="info-header">
          <h2>About SkinVision</h2>
          <p>Intelligent Skin Disease Detection Powered by Advanced AI</p>
        </div>

        <div className="features-grid">
          {features.map((feature, idx) => (
            <div key={idx} className="feature-card">
              <div className="feature-icon">{feature.icon}</div>
              <h3>{feature.title}</h3>
              <p className="feature-value">{feature.value}</p>
              <p className="feature-desc">{feature.description}</p>
            </div>
          ))}
        </div>

        <div className="tech-stack">
          <h3>Technology Stack</h3>
          <div className="tech-badges">
            <span className="tech-badge">TensorFlow/Keras</span>
            <span className="tech-badge">Django REST</span>
            <span className="tech-badge">React.js</span>
            <span className="tech-badge">Optuna</span>
            <span className="tech-badge">Python</span>
            <span className="tech-badge">JavaScript</span>
          </div>
        </div>

        <div className="info-description">
          <p>
            <strong>SkinVision</strong> uses deep learning with <strong>EfficientNet-B0 </strong> 
            to detect and classify various skin diseases. Our model is trained on high-quality 
            dermatological images and provides <strong>top-3 predictions</strong> with confidence 
            scores to help you understand potential skin conditions.
          </p>
          <p className="disclaimer-text">
            ℹ️ <em>This tool is for informational purposes only and should not replace 
            professional medical advice. Always consult a dermatologist for accurate diagnosis 
            and treatment.</em>
          </p>
        </div>
      </div>
    </section>
  );
};

export default InfoSection;