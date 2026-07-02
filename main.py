import os
from dotenv import load_dotenv
import time

from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]
BASE_URL = os.environ["BASE_URL"]

t_username = 'chefsteps'

LOGIN_URL = f"{BASE_URL}/login"
PAGE_URL = f"{BASE_URL}/u/{t_username}"

def wait_for_element(driver, by, value):
    return WebDriverWait(driver,10).until(EC.element_to_be_clickable((by, value)))

class InstaFollower:

    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(self.chrome_options)

    def login(self):
        self.driver.get(LOGIN_URL)
        username = wait_for_element(self.driver, By.NAME,"username")
        username.send_keys(USERNAME)
        password = wait_for_element(self.driver, By.NAME,"password")
        password.send_keys(PASSWORD)
        submit = wait_for_element(self.driver, By.CSS_SELECTOR, "[type='submit']")
        submit.click()

    def clear_popups(self):
        not_now = wait_for_element(self.driver, By.CSS_SELECTOR, "#popup-save-login div:nth-of-type(2)")
        not_now.click()
        not_now = wait_for_element(self.driver, By.CSS_SELECTOR, "#popup-notifications div button:nth-of-type(2)")
        not_now.click()

    def scroll_follower_box(self):
        follower_box = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".followers-scroll")))
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", follower_box)

    def find_followers(self):
        self.driver.get(PAGE_URL)
        followers_btn = wait_for_element(self.driver, By.CLASS_NAME, "naan-followers-link")
        followers_btn.click()

        follower_box = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".followers-scroll")))
        last_height = self.driver.execute_script("return arguments[0].scrollHeight", follower_box)

        while True:
            # Scroll down to the current bottom
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", follower_box)

            # Wait for new content to load
            time.sleep(2)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return arguments[0].scrollHeight", follower_box)
            if new_height == last_height:
                break  # Break the loop if no new content loaded
            last_height = new_height

    def follow(self):
        follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, ".naan-follower-row button")
        follow_count = 0
        for btn in follow_buttons:
            for _ in range(3):  # Retry up to 3 times
                try:
                    btn.click()
                    follow_count += 1

                    if follow_count == 5:
                        follow_count = 0
                        self.scroll_follower_box()

                    break  # Success

                except ElementClickInterceptedException:
                    cancel_btn = wait_for_element(
                        self.driver,
                        By.CLASS_NAME,
                        "naan-unfollow-cancel"
                    )
                    cancel_btn.click()
            else:
                print("Skipping button after 3 failed attempts.")

    def close_instagram(self):
        self.driver.quit()


ig = InstaFollower()

ig.login()
ig.clear_popups()
ig.find_followers()
ig.follow()
ig.close_instagram()