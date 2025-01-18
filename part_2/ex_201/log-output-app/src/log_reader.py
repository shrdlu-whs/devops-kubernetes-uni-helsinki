import time
import random
import string
import requests

PINGPONG_APP_URL = 'http://pingpong-app-svc'
PINGPONG_APP_PORT = 5000

def generate_random_string(length=20):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

def main():
    while True:
        # Read timestamp from file
        try:
            with open('/app/files/timestamp.txt', 'r') as f:
                timestamp = f.read().strip()
                random_value = generate_random_string()       
                print(f"{timestamp}: {random_value}")
        except FileNotFoundError:
            print("Timestamp file not found. Waiting for the generator to create it.")

        try:
            # Get # of pingpongs
            pingpong_requests = requests.get(f'{PINGPONG_APP_URL}:5000/counter')
            random_value = generate_random_string()       
            print(f"Ping/Pongs: {pingpong_requests.content.decode()}")
        except requests.exceptions.RequestException as e:
            print("Error connecting to pingpong service")
            print(e)
        time.sleep(5)

if __name__ == "__main__":
    main()