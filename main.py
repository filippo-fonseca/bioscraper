from selenium import webdriver
import random


class Scraper:
    def openURL(self):
        with open("brain/urls.txt") as f:
            # Update PATH with your local Chrome WebDriver's:
            PATH = "/Users/filippofonseca/Developer/SDKs/chromedriver"
            lines = f.readlines()
            driver = webdriver.Chrome(PATH)
            driver.get(random.choice(lines))
            print(driver.title)


scraper = Scraper()

scraper.openURL()
