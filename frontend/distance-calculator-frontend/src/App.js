import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [origin, setOrigin] = useState('');
  const [destination, setDestination] = useState('');
  const [result, setResult] = useState(null);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const calculateDistance = async () => {
    setLoading(true);
    setError('');
    
    try {
      const response = await axios.post('http://localhost:8000/location/calculate-distance/', {
        origin,
        destination
      });
      console.log(response.data)
      setResult(response.data);
    } catch (err) {
      setError(err.response?.data?.error || 'An error occurred');
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!origin || !destination) {
      setError('Please enter both origin and destination');
      return;
    }
    calculateDistance();
  };

  return (
    <div className="App">
      <h1>Distance Calculator</h1>
      
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Origin:</label>
          <input
            type="text"
            value={origin}
            onChange={(e) => setOrigin(e.target.value)}
            placeholder="Enter starting location"
          />
        </div>
        
        <div className="form-group">
          <label>Destination:</label>
          <input
            type="text"
            value={destination}
            onChange={(e) => setDestination(e.target.value)}
            placeholder="Enter destination"
          />
        </div>
        
        <button type="submit" disabled={loading}>
          {loading ? 'Calculating...' : 'Calculate Distance'}
        </button>
      </form>
      
      {error && <div className="error">{error}</div>}
      
      {loading && <div className="loading">Loading...</div>}
      
      {result && (
        <div className="result">
          <h2>Results</h2>
          <div>
            <h3>From:</h3>
            <p>{result.origin.formatted_address}</p>
          </div>
          <div>
            <h3>To:</h3>
            <p>{result.destination.formatted_address}</p>
          </div>
          <div>
            <h3>Distance:</h3>
            <p>{result.distance} km</p>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;