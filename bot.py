import os
import random
import datetime
from threading import Thread
import asyncio
import schedule
import time
import telegram

# Folder containing pictures
PICTURE_FOLDER = '/cards/'

TOKEN = '6710218788:AAGyU9qMPBMoWYl6ILW-SKuwmwmEosO46AQ'

CHAT_ID = '80366293'

# Initialize the Telegram Bot
bot = telegram.Bot(TOKEN)


def schedule_checker():
    while True:
        schedule.run_pending()
        time.sleep(1)


# Function to send a random picture from the folder
async def send_picture():
    # List all files in the folder
    files = os.listdir(PICTURE_FOLDER)

    # Select a random image
    random_image = random.choice(files)
    photo = PICTURE_FOLDER + random_image

    # Send the image
    print(photo)
    await bot.send_photo(CHAT_ID, photo=open(photo, 'rb'))


async def main():

    while True:
        # Get the current time
        now = datetime.datetime.now()

        # Check if it's 8:00 AM
        if now.hour == 10 and now.minute ==0:
            # Send the picture to a specific chat ID
            await send_picture()

            # Wait for 24 hours before sending the next picture
            time.sleep(24 * 60 * 60)
        else:
            # Sleep for 1 minute and check again
            time.sleep(60)


# Main function
if __name__ == "__main__":
    asyncio.run(main())

    # Spin up a thread to run the schedule check so it doesn't block your bot.
    # This will take the function schedule_checker which will check every second
    # to see if the scheduled job needs to be ran.
    Thread(target=schedule_checker).start()
