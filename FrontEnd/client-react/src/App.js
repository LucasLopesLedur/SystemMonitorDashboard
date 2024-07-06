import axios from 'axios';
import React, { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [systemInfo, setSystemInfo] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const result = await axios.get('http://127.0.0.1:5000/api/system_info');
        if (result.data.length > 0) {
          setSystemInfo(result.data[result.data.length - 1]);
        }
      } catch (error) {
        console.error('Erro ao buscar dados:', error);
      }
    };

    const interval = setInterval(() => {
      fetchData();
    }, 5000);

    return () => clearInterval(interval);
  }, []);

  if (!systemInfo) {
    return <div className="App">Carregando...</div>;
  }

  return (
    <div className="App">
      <h1>System Monitor</h1>
      <div>
        <h2>{systemInfo.hostname} ({systemInfo.ip_address})</h2>
        <p>OS: {systemInfo.os} {systemInfo.os_version} ({systemInfo.architecture})</p>
        <p>CPU Usage: {systemInfo.cpu_usage}%</p>
        <p>Memory Usage: {systemInfo.memory.percent}%</p>
        <p>Disk Usage: {systemInfo.disk.percent}%</p>
        <hr />
      </div>
    </div>
  );
}

export default App;
