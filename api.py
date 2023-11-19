import requests
from urllib.parse import urlencode

with open('resources/env.txt') as env_file:
    env_vars = dict(line.strip().split('=') for line in env_file)

API_URL = "https://www.tistory.com/apis/post/write"
ACCESS_TOKEN = env_vars.get("TISTORY_ACCESS_TOKEN")
BLOG_NAME = env_vars.get("BLOG_NAME")

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

# title = "Your Title"
# content = "Your Content"
# upload(title, content)
