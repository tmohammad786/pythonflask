from flask import Flask, jsonify

#hi hello

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hello from Alpine-based Python Docker container!"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)

