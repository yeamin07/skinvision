import React from 'react';
import '../styles/Footer.css';

const Footer = () => {
  const currentYear = new Date().getFullYear();

  return (
    <footer className="footer">
      <div className="footer-content">
        <p>&copy; {currentYear} SkinVision. All rights reserved.</p>
        <p>AI-Powered Skin Disease Detection System</p>
        <p className="credits">
          Developed by <i>DON YEAMIN</i> using TensorFlow, Django & React
        </p>
      </div>
    </footer>
  );
};

export default Footer;