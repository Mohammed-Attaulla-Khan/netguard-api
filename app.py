from flask import Flask, jsonify, request
import random
import time

app = Flask(__name__)

# Simulated secure authentication
API_KEY = "cisco-fy27-secure-key"

def require_api_key(func):
    def wrapper(*args, **kwargs):
        if request.headers.get("x-api-key") != API_KEY:
            return jsonify({"error": "Unauthorized threat detected"}), 401
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper

@app.route('/api/network/scan', methods=['GET'])
@require_api_key
def scan_network():
    # Simulating TCP/IP network packet analysis
    protocols = ['TCP', 'UDP', 'ICMP']
    threat_levels = ['Low', 'Medium', 'High']
    
    packets = []
    for _ in range(5):
        packet = {
            "timestamp": time.time(),
            "source_ip": f"192.168.1.{random.randint(2, 254)}",
            "dest_ip": f"10.0.0.{random.randint(1, 100)}",
            "protocol": random.choice(protocols),
            "payload_size_bytes": random.randint(64, 1500),
            "threat_assessment": random.choice(threat_levels)
        }
        packets.append(packet)
        
    return jsonify({
        "status": "success",
        "active_connections": random.randint(10, 50),
        "packet_analysis": packets
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
