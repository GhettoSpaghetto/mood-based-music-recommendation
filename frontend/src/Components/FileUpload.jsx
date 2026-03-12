import React, { useState } from 'react';

const FileUpload = ({ onUpload, loading }) => {
  const [selectedFile, setSelectedFile] = useState(null);

  const handleInputChange = (e) => {
    setSelectedFile(e.target.files[0]);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (selectedFile) onUpload(selectedFile);
  };

  return (
    <div className="upload-section">
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleInputChange} accept="image/*" />
        <button type="submit" disabled={!selectedFile || loading}>
          {loading ? "Analyzing Mood..." : "Identify Mood"}
        </button>
      </form>
    </div>
  );
};

export default FileUpload;