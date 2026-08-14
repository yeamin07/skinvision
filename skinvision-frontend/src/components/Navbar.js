
import React, { useRef } from 'react';
import { FiUpload } from 'react-icons/fi';
import '../styles/Navbar.css';

const Navbar = ({ onImageUpload }) => {
  const fileInputRef = useRef(null);

  const handleUploadClick = () => {
    fileInputRef.current.click();
  };

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      // Validate file type
      if (!file.type.startsWith('image/')) {
        alert('Please select a valid image file');
        return;
      }
      onImageUpload(file);
    }
  };

  return (
    <nav className="navbar">
      <div className="navbar-container">
        <div className="navbar-left">
          <img 
            src="/logo.png" 
            alt="SkinVision Logo" 
            className="logo"
          />
          <span className="brand-name">SkinVision</span>
        </div>

        <div className="navbar-right">
          <button 
            className="upload-btn"
            onClick={handleUploadClick}
          >
            <FiUpload /> Upload Image
          </button>
          <input
            type="file"
            ref={fileInputRef}
            onChange={handleFileChange}
            accept="image/*"
            style={{ display: 'none' }}
          />
        </div>
      </div>
    </nav>
  );
};

export default Navbar;