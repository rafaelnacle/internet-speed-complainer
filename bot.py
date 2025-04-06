import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class InternetSpeedTwitterBot:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        time.sleep(3)
        accept_button = self.driver.find_element(By.ID, value='onetrust-accept-btn-handler')
        accept_button.click()

        time.sleep(3)

        go_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/div[1]/a/span[4]')
        go_button.click()


    def tweet_at_provider(self):
        pass