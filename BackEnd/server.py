from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class SystemInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    os = db.Column(db.String(50))
    os_version = db.Column(db.String(100))
    architecture = db.Column(db.String(50))
    cpu_usage = db.Column(db.Float)
    memory_total = db.Column(db.Float)
    memory_available = db.Column(db.Float)
    memory_used = db.Column(db.Float)
    memory_percent = db.Column(db.Float)
    disk_total = db.Column(db.Float)
    disk_used = db.Column(db.Float)
    disk_free = db.Column(db.Float)
    disk_percent = db.Column(db.Float)
    hostname = db.Column(db.String(100))
    ip_address = db.Column(db.String(50))

    def __repr__(self):
        return f'<SystemInfo {self.hostname}>'

def initialize_database():
    db.create_all()
    logging.info("Database initialized.")

@app.route('/api/system_info', methods=['POST'])
def receive_system_info():
    data = request.get_json()
    system_info = SystemInfo(
        os=data['os'],
        os_version=data['os_version'],
        architecture=data['architecture'],
        cpu_usage=data['cpu_usage'],
        memory_total=data['memory']['total'],
        memory_available=data['memory']['available'],
        memory_used=data['memory']['used'],
        memory_percent=data['memory']['percent'],
        disk_total=data['disk']['total'],
        disk_used=data['disk']['used'],
        disk_free=data['disk']['free'],
        disk_percent=data['disk']['percent'],
        hostname=data['hostname'],
        ip_address=data['ip_address']
    )
    db.session.add(system_info)
    db.session.commit()
    logging.info(f"Received system info from {data['hostname']}.")

    notifications = []
    if system_info.cpu_usage > 90:
        notifications.append("CPU usage above 90%")
    if system_info.memory_percent > 90:
        notifications.append("Memory usage above 90%")
    
    return jsonify({"status": "success", "notifications": notifications})

@app.route('/api/system_info', methods=['GET'])
def get_system_info():
    all_info = SystemInfo.query.all()
    result = [
        {
            "os": info.os,
            "os_version": info.os_version,
            "architecture": info.architecture,
            "cpu_usage": info.cpu_usage,
            "memory": {
                "total": info.memory_total,
                "available": info.memory_available,
                "used": info.memory_used,
                "percent": info.memory_percent
            },
            "disk": {
                "total": info.disk_total,
                "used": info.disk_used,
                "free": info.disk_free,
                "percent": info.disk_percent
            },
            "hostname": info.hostname,
            "ip_address": info.ip_address
        } for info in all_info
    ]
    return jsonify(result)

if __name__ == "__main__":
    with app.app_context():
        initialize_database()
    logging.info("Starting Flask server...")
    app.run(debug=True)
    logging.info("Flask server started.")
