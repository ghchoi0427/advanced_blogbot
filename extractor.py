from bs4 import BeautifulSoup


def extract(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    strong_tags = soup.find_all('strong')

    # for strong_tag in strong_tags:
        # print(strong_tag.text)
        
    return [strong_tag.text for strong_tag in strong_tags]