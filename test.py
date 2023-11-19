import schedule
import time

def your_method():
    print("Running your method...")
    # Your method implementation goes here

# Schedule the method to run every 1 hour and 30 minutes (5400 seconds)
schedule.every(5).seconds.do(your_method)

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(10)  # Sleep for 10 seconds before checking the schedule again
