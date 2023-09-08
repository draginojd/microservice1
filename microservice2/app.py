from flask import Flask
import requests

app = Flask(__name__)


@app.route('/')
def goodbye_world():
    r = requests.get("http://service1-container:5001")
    return f"Hello from service 2. Service 1 says: {r.text}!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
