import React, { useEffect, useState } from 'react';

const MusicResults = ({ mood, songs }) => {
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    if (mood) setVisible(true);
  }, [mood, songs]);

  if (!mood) return null;

  const moodColors = {
    happy: '#FFD700',
    sad: '#6495ED',
    angry: '#FF4500',
    neutral: '#1DB954',
    surprise: '#FF69B4',
  };

  const accentColor = moodColors[mood?.toLowerCase()] || '#1DB954';

  return (
    <div
      style={{
        background: '#121212',
        minHeight: '100vh',
        padding: '2rem',
        fontFamily: "'Georgia', serif",
        color: '#fff',
      }}
    >
      <div style={{ maxWidth: '600px', margin: '0 auto' }}>

        {/* Header */}
        <div style={{ marginBottom: '2rem' }}>
          <p
            style={{
              color: '#888',
              fontSize: '0.75rem',
              letterSpacing: '0.2em',
              textTransform: 'uppercase',
              marginBottom: '0.5rem',
            }}
          >
            Now playing for your mood
          </p>

          <h2 style={{ fontSize: '2rem', fontWeight: 'bold', margin: 0 }}>
            Feeling{' '}
            <span
              style={{
                color: accentColor,
                borderBottom: `2px solid ${accentColor}`,
                paddingBottom: '2px',
              }}
            >
              {mood}
            </span>
          </h2>
        </div>

        {/* Song list */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem' }}>
          {songs && songs.length > 0 ? (
            songs.map((song, index) => (
              <a
                key={index}
                href={song.url || '#'}
                target="_blank"
                rel="noopener noreferrer"
                style={{ textDecoration: 'none' }}
              >
                <div
                  style={{
                    display: 'flex',
                    alignItems: 'center',
                    gap: '1rem',
                    background: '#1e1e1e',
                    borderRadius: '8px',
                    padding: '1rem 1.25rem',
                    border: '1px solid #2a2a2a',
                    cursor: 'pointer',
                    transition: 'background 0.2s',
                  }}
                  onMouseEnter={(e) =>
                    (e.currentTarget.style.background = '#2a2a2a')
                  }
                  onMouseLeave={(e) =>
                    (e.currentTarget.style.background = '#1e1e1e')
                  }
                >
                  <span
                    style={{
                      color: '#555',
                      fontSize: '0.8rem',
                      width: '16px',
                      textAlign: 'center',
                    }}
                  >
                    {index + 1}
                  </span>

                  <span style={{ color: accentColor, fontSize: '1.2rem' }}>
                    ♪
                  </span>

                  <div style={{ flex: 1 }}>
                    <div
                      style={{
                        fontWeight: '600',
                        fontSize: '0.95rem',
                        color: '#fff',
                      }}
                    >
                      {song.name}
                    </div>

                    <div
                      style={{
                        fontSize: '0.8rem',
                        color: '#888',
                        marginTop: '2px',
                      }}
                    >
                      {song.artist}
                    </div>
                  </div>

                  <span style={{ color: '#444', fontSize: '0.9rem' }}>↗</span>
                </div>
              </a>
            ))
          ) : (
            <p
              style={{
                color: '#555',
                textAlign: 'center',
                marginTop: '2rem',
              }}
            >
              No songs found for this mood.
            </p>
          )}
        </div>
      </div>
    </div>
  );
};

export default MusicResults;

