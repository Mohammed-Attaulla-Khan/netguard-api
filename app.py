from flask import Flask, jsonify, request, render_template_string
import random
import time

app = Flask(__name__)

API_KEY = "cisco-fy27-secure-key"

def require_api_key(func):
    def wrapper(*args, **kwargs):
        if request.headers.get("x-api-key") != API_KEY:
            return jsonify({"error": "Unauthorized threat detected"}), 401
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper

# The new Graphical User Interface
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <title>NetGuard | Security Center</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { font-family: 'Segoe UI', sans-serif; background: #0a0e17; color: #00ffcc; text-align: center; padding: 20px; margin: 0; }
        .card { background: #121a2f; padding: 20px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,255,204,0.15); max-width: 800px; margin: auto; border: 1px solid #1f2d4a; }
        h2 { margin-top: 0; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; color: #e2e8f0; font-size: 0.9em; }
        th, td { border: 1px solid #1f2d4a; padding: 12px; text-align: center; }
        th { background: #1a243d; color: #00ffcc; font-weight: bold; }
        .high { color: #ff4c4c; font-weight: bold; background: rgba(255,76,76,0.1); }
        .med { color: #ffcc00; }
        .low { color: #4caf50; }
        button { background: #00ffcc; color: #0a0e17; border: none; padding: 12px 24px; font-size: 16px; cursor: pointer; border-radius: 5px; font-weight: bold; transition: 0.3s; }
        button:hover { background: #00ccaa; box-shadow: 0 0 10px #00ffcc; }
        @media (max-width: 600px) { th, td { padding: 8px; font-size: 0.8em; } }
    </style>
</head>
<body>
    <div class="card">
        <h2>🛡️ NetGuard Security Center</h2>
        <p style="color: #94a3b8; margin-bottom: 25px;">Real-time TCP/IP Packet Inspector (API Secured)</p>
        <button onclick="fetchData()">Run Network Scan</button>
        <div id="results"></div>
    </div>
    <script>
        async function fetchData() {
            const resultsDiv = document.getElementById('results');
            resultsDiv.innerHTML = '<p style="margin-top: 20px; color: #94a3b8;">Authenticating API Key & Scanning...</p>';
            try {
                // Sending the hidden API key to the backend
                const response = await fetch('/api/network/scan', {
                    headers: { 'x-api-key': 'cisco-fy27-secure-key' }
                });
                const data = await response.json();
                
                let html = `<h3 style="margin-top: 25px; color: #fff;">Active Connections: ${data.active_connections}</h3>`;
                html += `<table><tr><th>Source IP</th><th>Dest IP</th><th>Protocol</th><th>Size (Bytes)</th><th>Threat Level</th></tr>`;
                
                data.packet_analysis.forEach(p => {
                    let tClass = p.threat_assessment === 'High' ? 'high' : (p.threat_assessment === 'Medium' ? 'med' : 'low');
                    html += `<tr><td>${p.source_ip}</td><td>${p.dest_ip}</td><td>${p.protocol}</td><td>${p.payload_size_bytes}</td><td class="${tClass}">${p.threat_assessment}</td></tr>`;
                });
                html += `</table>`;
                resultsDiv.innerHTML = html;
            } catch (e) {
                resultsDiv.innerHTML = '<p style="color:#ff4c4c;">Error fetching data</p>';
            }
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/network/scan', methods=['GET'])
@require_api_key
def scan_network():
    protocols = ['TCP', 'UDP', 'ICMP', 'HTTPS']
    threat_levels = ['Low', 'Low', 'Medium', 'High'] # Weighted for realism
    packets = []
    for _ in range(5):
        packets.append({
            "timestamp": time.time(),
            "source_ip": f"192.168.1.{random.randint(2, 254)}",
            "dest_ip": f"10.0.0.{random.randint(1, 100)}",
            "protocol": random.choice(protocols),
            "payload_size_bytes": random.randint(64, 1500),
            "threat_assessment": random.choice(threat_levels)
        })
    return jsonify({"status": "success", "active_connections": random.randint(10, 50), "packet_analysis": packets})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
