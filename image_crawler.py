import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_images(url, folder_path):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all image tags on the page
    img_tags = soup.find_all('img')

    # Download each image
    for img_tag in img_tags:
        img_url = img_tag.get('src')
        if img_url:
            img_url = urljoin(url, img_url)
            img_name = os.path.join(folder_path, os.path.basename(img_url))
            with open(img_name, 'wb') as img_file:
                img_file.write(requests.get(img_url).content)
            print(f"Downloaded: {img_name}")

if __name__ == "__main__":
    # Specify the URL of the page you want to crawl
    target_url = "https://example.com"

    # Specify the folder where you want to save the images
    output_folder = "images"

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Call the download_images function
    download_images(target_url, output_folder)
