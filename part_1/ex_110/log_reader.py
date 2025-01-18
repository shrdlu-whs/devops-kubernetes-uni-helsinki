import time
import random
import string

def generate_random_string(length=20):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

def main():
    while True:
        try:
            with open('/app/files/timestamp.txt', 'r') as f:
                timestamp = f.read().strip()
                random_value = generate_random_string()
                print(f"{timestamp}: {random_value}")
                print("{timestamp}: {random_value}")
        except FileNotFoundError:
            print("Timestamp file not found. Waiting for the generator to create it.")
        time.sleep(5)

if __name__ == "__main__":
    main()