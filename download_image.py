import requests
import os
from dotenv import load_dotenv

load_dotenv()

PIXABAY_API_KEY = os.getenv("PIXABAY_API_KEY")

folder_name = "Pizza Images"
images_title = "Pizza"
image_number = 12

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
            filename = os.path.join(folder_name, f"{i}_{image_title.replace(' ', '_')}.jpg")

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

# Execute the function
download_pixabay_images(folder_name, images_title, num_images=image_number)
