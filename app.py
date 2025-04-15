from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin if needed

# Store alerts in memory for demo purposes
alerts = []

@app.route('/')
def index():
    return render_template('index.html', alerts=alerts)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    alert = {
        'timestamp': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
        'message': data
    }
    alerts.append(alert)
    print(f"[Webhook] New alert received: {alert}")
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
