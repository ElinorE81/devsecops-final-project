from flask import Flask, request, jsonify, render_template
import logging
import sys

app = Flask(__name__)

logging.basicConfig(stream=sys.stdout, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/')
def home():
    # כאן עשינו את השינוי - קוראים לקובץ עיצוב!
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json(silent=True) or {}
    username = data.get('username')
    password = data.get('password')
    
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)

    if username == "admin" and password == "secret123":
        logging.info(f"Successful login for user '{username}' from IP: {client_ip}")
        return jsonify({"status": "success", "message": "Logged in"}), 200
    else:
        logging.warning(f"Failed login attempt for user '{username}' from IP: {client_ip}")
        return jsonify({"status": "failed", "message": "Invalid credentials"}), 401

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
