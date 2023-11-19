import requests
from urllib.parse import urlencode

API_URL = "https://www.tistory.com/apis/post/write"
ACCESS_TOKEN = "your_access_token"  # Replace with your actual access token
BLOG_NAME = "your_blog_name"  # Replace with your actual blog name

def upload(title, content):
    category = "1"  # category ID
    visibility = "3"  # 3 for public, 2 for protected, 1 for private
    output = "json"  # or "xml"

    params = {
        'access_token': ACCESS_TOKEN,
        'output': output,
        'blogName': BLOG_NAME,
        'title': title,
        'content': content,
        'visibility': visibility,
        'category': category
    }

    url = f"{API_URL}?{urlencode(params)}"

    response = requests.post(url)
    print(response.text)

# Example usage
title = "Your Title"
content = "Your Content"
upload(title, content)
