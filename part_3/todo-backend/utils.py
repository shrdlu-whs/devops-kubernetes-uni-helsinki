import requests
from io import BytesIO
import base64
import os
from datetime import datetime

def get_random_image(url='https://picsum.photos/400', path='/app/files/image.png', update_interval=60):
    
    try:
        # If image exists: load from file
        if os.path.exists(path):
            with open(path, 'rb') as fp:
                img_data = fp.read()
        else:
            with open(path, 'wb') as fp:
                r = requests.get(url)
                img_data = BytesIO(r.content).read()
                fp.write(img_data)
    except Exception as e:
            print(e)
    # Get modification date timestamp
    m_time = os.path.getmtime(path)
    # Convert timestamp into DateTime object
    dt_mod = datetime.datetime.fromtimestamp(m_time)
    dt_now = datetime.datetime.now()
    # Get timedelta of modification date and now
    time_delta = dt_now-dt_mod 
    time_delta_minutes = time_delta.total_seconds() / 60

    # If file is older than 1 hour, load new image
    if time_delta_minutes > update_interval:
        print('File is older than 1 hour, loading new image')
        with open(path, 'wb') as fp:
            r = requests.get(url)
            img_data = BytesIO(r.content).read()
            fp.write(img_data)
    
    # Base64 encode the image data and convert to string
    encoded_img = base64.b64encode(img_data).decode()
    return encoded_img