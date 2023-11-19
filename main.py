import schedule
import time
from file_reader import get_topic_from_file
from blog_bot import write_essay
from api import upload

def run():
    current_topic = get_topic_from_file()
    essay = write_essay(current_topic)
    upload(current_topic, essay)

while True:
    run()
    time.sleep(5400)
