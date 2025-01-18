import time
import random
import string
import requests
import os
from flask import Flask
import threading
import json

app = Flask(__name__)

try:
    PINGPONG_APP_URL = os.getenv('PINGPONG_APP_URL')
    PINGPONG_APP_PORT = os.getenv('PINGPONG_APP_PORT', "5000")
    CONFIG_PATH = os.getenv('CONFIG_PATH', "/app/config")
except KeyError as e:   
    print("Environment variable not set")
    print(e)
    
# Health check
@app.route("/health")
@app.route("/")
def health():
    try:
        # Get # of pingpongs
        requests.get(f'{PINGPONG_APP_URL}:{PINGPONG_APP_PORT}/counter')
        return "OK", 200
    except requests.exceptions.RequestException as e:
        return "No connection to Pingpong app", 500

def generate_random_string(length=20):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

# Log output
@app.route("/logoutput")
def logoutput():
# Load data from the JSON file
    with open('/app/cache/output.json', 'r') as f:
        data = json.load(f)
        text = f"{data['timestamp']}: {data['random_value']}<br>Ping/Pongs: {data['pingpongs']}<br>env variable MESSAGE: {data['message']}<br>information.txt content: {data['information']}"
        return text, 200

def log_data():
    
    data = {}
    # Read timestamp from file
    try:
        with open('/app/files/timestamp.txt', 'r') as f:
            timestamp = f.read().strip()
            random_value = generate_random_string()       
            print(f"{timestamp}: {random_value}")
            data['timestamp'] = timestamp
            data['random_value'] = random_value
    except FileNotFoundError:
        print("Timestamp file not found. Waiting for the generator to create it.")

    try:
        # Get # of pingpongs
        pingpong_res = requests.get(f'{PINGPONG_APP_URL}:{PINGPONG_APP_PORT}/counter')     
        pingpongs = pingpong_res.content.decode()
        print(f"Ping/Pongs: {pingpongs}")
        data['pingpongs'] = pingpongs
    except requests.exceptions.RequestException as e:
        print( f'Error connecting to pingpong service at {PINGPONG_APP_URL}:{PINGPONG_APP_PORT}/counter')
        print(e)

    # Get message from environment variable
    try:
        message = os.getenv('MESSAGE')
        print(f"env variable: MESSAGE: {message}")
        data['message'] = message
    except KeyError as e:
        print("MESSAGE environment variable not set")
        print(e)

    # Get text from information.txt
    with open(f'{CONFIG_PATH}/information.txt', 'r') as f:
            information = f.read().strip()
            print(f"information.txt content: {information}")
            data['information'] = information
    return data

def main():
    while True:
        data = log_data()
        with open('/app/cache/output.json', 'w') as f:
            json.dump(data, f, indent=4)
        time.sleep(5)


def run_flask_app():
    app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
    flask_thread = threading.Thread(target=run_flask_app)
    main_thread = threading.Thread(target=main)

    flask_thread.start()
    main_thread.start()

    flask_thread.join()
    main_thread.join()