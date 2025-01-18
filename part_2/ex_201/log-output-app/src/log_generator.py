import time
from datetime import datetime

def main():
    print("Starting log generator...")
    while True:
        try:
            timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
            print(timestamp)
            with open('/app/files/timestamp.txt', 'w') as f:
                f.write(timestamp)
            time.sleep(5)
        except Exception as e:

            print(e)

if __name__ == "__main__":
    main()