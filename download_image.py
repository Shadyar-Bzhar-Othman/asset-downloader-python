import requests
import os
from dotenv import load_dotenv

load_dotenv()

PIXABAY_API_KEY = os.getenv("PIXABAY_API_KEY")
PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")

folder_name = "Cake Images"
images_title = "Cake"
image_number = 12

import os
import requests

def download_pexels_images(folder_name, image_title, num_images=12):
   
    try:
        os.makedirs(folder_name, exist_ok=True)
        base_url = "https://api.pexels.com/v1/search"
        headers = {"Authorization": PEXELS_API_KEY}
        search_params = {
            "query": image_title,
            "per_page": num_images,
        }

        response = requests.get(base_url, headers=headers, params=search_params)
        response.raise_for_status()

        data = response.json()

        for i, photo in enumerate(data['photos'], start=1):
            image_url = photo['src']['original']
            filename = os.path.join(folder_name, f"{i}_pexels_{image_title.replace(' ', '_')}.jpg")

            image_response = requests.get(image_url, stream=True)
            image_response.raise_for_status()

            with open(filename, 'wb') as f:
                for chunk in image_response.iter_content(1024):
                    f.write(chunk)

            print(f"Downloaded image {i}: {filename}")
    except requests.exceptions.RequestException as e:
        print(f"HTTP Request failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def download_pixabay_images(folder_name, image_title, num_images=12):
    try:
        os.makedirs(folder_name, exist_ok=True)
        base_url = "https://pixabay.com/api/"
        search_params = {
            "key": PIXABAY_API_KEY,
            "q": image_title.replace(" ", "+"),
            "per_page": num_images,
        }

        response = requests.get(base_url, params=search_params)
        response.raise_for_status()

        data = response.json()

        for i, hit in enumerate(data['hits'], start=1):
            image_url = hit['largeImageURL']
            filename = os.path.join(folder_name, f"{i}_pixabay_{image_title.replace(' ', '_')}.jpg")

            image_response = requests.get(image_url, stream=True)
            image_response.raise_for_status()

            with open(filename, 'wb') as f:
                for chunk in image_response.iter_content(1024):
                    f.write(chunk)

            print(f"Downloaded image {i}: {filename}")
    except requests.exceptions.RequestException as e:
        print(f"HTTP Request failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def download_images(folder_name, images_title, num_images=12):
    img_number = int(num_images / 2)
    print(img_number)
    download_pexels_images(folder_name, images_title, num_images=img_number)
    download_pixabay_images(folder_name, images_title, num_images=img_number)

download_images(folder_name, images_title, num_images=image_number)
