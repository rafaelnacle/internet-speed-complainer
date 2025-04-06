import os
from dotenv import load_dotenv
from bot import InternetSpeedTwitterBot

load_dotenv()

PROMISED_DOWN = 700
PROMISED_UP = 350
X_EMAIL = os.getenv("X_EMAIL")
X_PWD = os.getenv("X_PWD")


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
