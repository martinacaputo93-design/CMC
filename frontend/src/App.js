import React, { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Redirect to the static HTML site served by backend
    const backendUrl = process.env.REACT_APP_BACKEND_URL || '';
    
    // Wait a moment then redirect to the index page
    const timer = setTimeout(() => {
      window.location.href = `${backendUrl}/api/site/index.html`;
    }, 100);

    return () => clearTimeout(timer);
  }, []);

  // Show loading while redirecting
  return (
    <div className="redirect-container">
      <div className="loading-spinner"></div>
      <p>Caricamento portfolio...</p>
    </div>
  );
}

export default App;
