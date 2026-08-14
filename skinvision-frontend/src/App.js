

import React, { useState, useRef } from 'react';
import Navbar from './components/Navbar';
import HomePage from './pages/HomePage';
import Footer from './components/Footer';
import './App.css';

function App() {
  const homePageRef = useRef(null);

  const handleImageUpload = (file) => {
    // Call the upload handler in HomePage
    if (homePageRef.current) {
      homePageRef.current.uploadImage(file);
    }
  };

  return (
    <div className="App">
      <Navbar onImageUpload={handleImageUpload} />
      <HomePage ref={homePageRef} />
      <Footer />
    </div>
  );
}

export default App;