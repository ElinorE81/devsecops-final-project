from flask import Flask, request, jsonify
import logging
import sys

app = Flask(__name__)

# הגדרת הלוגים כך שיודפסו החוצה (כדי שקוברנטיס יוכל לקרוא אותם)
logging.basicConfig(stream=sys.stdout, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/')
def home():
    return "Welcome to the Secure DevSecOps App!"

@app.route('/login', methods=['POST'])
def login():
    # פונקציה פשוטה שמדמה ניסיון התחברות
    data = request.get_json(silent=True) or {}
    username = data.get('username')
    password = data.get('password')
    
    # תפיסת כתובת ה-IP האמיתית של המשתמש (או התוקף)
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)

    if username == "admin" and password == "secret123":
        logging.info(f"Successful login for user '{username}' from IP: {client_ip}")
        return jsonify({"status": "success", "message": "Logged in"}), 200
    else:
        # זה הלוג שאנחנו נחפש אחר כך בענן כדי לזהות תקיפה!
        logging.warning(f"Failed login attempt for user '{username}' from IP: {client_ip}")
        return jsonify({"status": "failed", "message": "Invalid credentials"}), 401

@app.route('/health')
def health():
    # נתיב שקוברנטיס ישתמש בו כדי לוודא שהאפליקציה חיה ונושמת
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
