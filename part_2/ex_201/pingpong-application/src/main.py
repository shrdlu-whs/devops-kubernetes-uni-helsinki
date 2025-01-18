import random
import string
from flask import Flask, jsonify

app = Flask(__name__)

current_status = {
    "counter": 0
}

def generate_random_string(length=20):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

@app.route('/pingpong', methods=['GET'])
def pingpong():
    current_status["counter"] += 1
    return "Pong " + str(current_status["counter"])

@app.route('/counter', methods=['GET'])
def status():
    return str(current_status["counter"])

if __name__ == "__main__":
    from threading import Thread
    Thread(target=lambda: app.run(host='0.0.0.0', port=5000)).start()
