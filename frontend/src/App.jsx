import React, { useState } from 'react';
import FileUpload from './Components/FileUpload';
import MusicResults from './Components/MusicResults';

import './App.css'

const App = () => {
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const uploadToApi = async (file) => {
    setLoading(true);
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch('http://localhost:8000/predict', {
        method: 'POST',
        body: formData,
      });
      const data = await response.json();
      setResult(data);
    } catch (error) {
      alert("Backend connection failed. Is FastAPI running?");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-shell">
      <header>
        <h1>VibeCheck AI</h1>
        <p>Upload a photo, get a song.</p>
      </header>

      <FileUpload onUpload={uploadToApi} loading={loading} />
      
      {result && (
        <MusicResults 
          mood={result.mood} 
          songs={result.recommend_music} 
        />
      )}
    </div>
  );
};

export default App;