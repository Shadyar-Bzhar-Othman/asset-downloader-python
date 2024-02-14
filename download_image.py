import requests
import os

PIXABAY_API_KEY = "42368499-3617d02f2d4f476a2ebcaef11" 

def download_pixabay_images(folder_name, image_title, num_images=10):
    os.makedirs(folder_name, exist_ok=True)

    base_url = "https://pixabay.com/api/"
    search_params = {
        "key": PIXABAY_API_KEY,
        "q": image_title,
        "per_page": num_images,
    }

    response = requests.get(base_url, params=search_params)
    response.raise_for_status()

    data = response.json()

    for i, hit in enumerate(data['hits']):
        image_url = hit['largeImageURL']
        filename = os.path.join(folder_name, f"{i+1}_{image_title}.jpg")

        image_response = requests.get(image_url, stream=True)
        image_response.raise_for_status()

        with open(filename, 'wb') as f:
            for chunk in image_response.iter_content(1024):
                f.write(chunk)

        print(f"Downloaded image {i+1}: {filename}")

folder_name = "my_images"
image_title = "coding" 
download_pixabay_images(folder_name, image_title) 