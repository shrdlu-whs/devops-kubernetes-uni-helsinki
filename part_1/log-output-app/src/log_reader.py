import time
import random
import string
import requests
import os
from flask import Flask
import threading
import json

app = Flask(__name__)

# Log output
@app.route("/logoutput")
def logoutput():
# Load data from the JSON file
    with open('/app/cache/output.json', 'r') as f:
        data = json.load(f)
        text = f"{data['timestamp']}: {data['random_value']}"
        text = f"{data['timestamp']}: {data['random_value']}<br>Ping/Pongs: {data['pingpongs']}"
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
        with open('/app/shared/pingpong.txt', 'r') as f:
            pingpong_requests = f.read().strip()     
            print(f"Ping/Pongs: {pingpong_requests}")
            data['pingpongs'] = pingpong_requests
    except FileNotFoundError:
        print("Pingpongs file not found. Waiting for the app to create it.")
        
    return data 
    

def generate_random_string(length=20):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

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