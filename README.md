# System Monitor Dashboard

This is a system monitoring project that displays real-time system information, using React for the frontend and Flask with SQLAlchemy for the backend.

## Features

- Displays detailed system information such as CPU, memory, and disk usage.
- Stores system information in an SQLite database.

## Technologies Used

- **Frontend:** Javascript, React
- **Backend:** Python, Flask

## Installation and Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/LucasLopesLedur/SystemMonitorDashboard.git
   ```
2. Install frontend and backend dependencies:

```bash
   cd FrontEnd
   npm install
   cd ../BackEnd
   pip install -r requirements.txt
```


3. Database:

- The SQLite database is automatically configured by Flask when starting the server.

4. Start the backend server:

```bash
cd BackEnd
python server.py
```

5. Start the frontend server:

```bash
cd FrontEnd
npm start
```

6. Open your browser and go to **http://localhost:3000** to view the real-time system monitor.

![Captura de tela 2024-07-06 001721](https://github.com/LucasLopesLedur/SystemMonitorDashboard/assets/102767476/763cb7f1-34dd-45ec-adbe-394e21320649)


