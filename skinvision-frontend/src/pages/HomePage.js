
import React, { useState, forwardRef, useImperativeHandle } from 'react';
import DiseaseCard from '../components/DiseaseCard';
import DiseaseDetailModal from '../components/DiseaseDetailModal';
import ResultBox from '../components/ResultBox';
import InfoSection from '../components/InfoSection';
import { commonDiseases } from '../data/diseaseData';
import { predictSkinDisease } from '../services/apiService';
import '../styles/HomePage.css';

const HomePage = forwardRef((props, ref) => {
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [selectedDisease, setSelectedDisease] = useState(null);

  // Expose uploadImage method to parent component
  useImperativeHandle(ref, () => ({
    uploadImage: handleImageUpload,
  }));

  const handleImageUpload = async (file) => {
    setLoading(true);
    setSelectedDisease(null);
    
    try {
      const apiResult = await predictSkinDisease(file);
      setResult(apiResult);
    } catch (error) {
      alert('Error uploading image: ' + error.message);
      console.error('Upload error:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleDiseaseCardClick = (disease) => {
    setSelectedDisease(disease);
    setResult(null);
  };

  const handleCloseModal = () => {
    setSelectedDisease(null);
  };

  const handleResultClose = () => {
    setResult(null);
  };

  return (
    <div className="home-page">
      {loading && (
        <div className="loading-overlay">
          <div className="spinner"></div>
          <p>Analyzing image...</p>
        </div>
      )}

      <section className="hero-section">
        <h1>Welcome to SkinVision</h1>
        <p>AI-Powered Skin Disease Detection</p>
      </section>

      <InfoSection/>

      <section className="diseases-section">
        <h2>Common Skin Diseases</h2>
        <div className="diseases-grid">
          {commonDiseases.map((disease) => (
            <DiseaseCard
              key={disease.id}
              disease={disease}
              onClick={handleDiseaseCardClick}
            />
          ))}
        </div>
      </section>

      {selectedDisease && (
        <DiseaseDetailModal 
          disease={selectedDisease} 
          onClose={handleCloseModal}
        />
      )}

      {result && (
        <ResultBox 
          result={result}
          onClose={handleResultClose}
        />
      )}
    </div>
  );
});

HomePage.displayName = 'HomePage';

export default HomePage;