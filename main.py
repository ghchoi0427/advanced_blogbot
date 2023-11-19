import schedule
import time
from file_reader import get_topic_from_file
from blog_bot import write_essay
from api import upload

def run():
    current_topic = get_topic_from_file()
    essay = write_essay(current_topic)

# for i in range(16):
#     schedule.every().day.at(f"{i:02d}:00").do(your_method)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
run()
