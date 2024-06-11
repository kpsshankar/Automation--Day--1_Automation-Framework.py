"""
loginPage.py
"""

from webpages.Data2.data2 import data2

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

# Explicit Wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginPage:

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 10)

    def boot(self):
        self.driver.get(data2.Webdata().url)
        self.driver.maximize_window()

    def quit(self):
        self.driver.quit()

    def login(self):
        try:
            self.boot()

            self.wait.until(ec.presence_of_element_located((By.ID, locator.Weblocator().usernameLocator))).send_keys(
                data2.Webdata().Name)
            self.wait.until(ec.presence_of_element_located((By.ID, locator.Weblocator().passwordLocator))).send_keys(
                data2.Webdata().Birthdate)
            self.wait.until(
                ec.presence_of_element_located((By.ID, locator.Weblocator().buttonLocator))).click().send_keys(
                data2.Webdata().Birthday)
            self.wait.until(
                ec.presence_of_element_located((By.ID, locator.Weblocator().buttonLocator))).click().send_keys(
                data2.Webdata().Awads & recognition)
            self.wait.until(
                ec.presence_of_element_located((By.ID, locator.Weblocator().buttonLocator))).click().send_keys(
                data2.Webdata().Pagetopics)
            self.wait.until(
                ec.presence_of_element_located((By.ID, locator.Weblocator().buttonLocator))).click().send_keys(
                data2.Webdata().Deathdate)
            self.wait.until(
                ec.presence_of_element_located((By.ID, locator.Weblocator().buttonLocator))).click().send_keys(
                data2.Webdata().Genderidentity)
            self.wait.until(
                ec.presence_of_element_located((By.ID, locator.Weblocator().buttonLocator))).click().send_keys(
                data2.Webdata().Credits)
            self.wait.until(
                ec.presence_of_element_located((By.ID, locator.Weblocator().buttonLocator))).click().send_keys(
                data2.Webdata().Adultnames)

            if self.driver.current_url == data2.Webdata().dashboardURL:
                print("Successfully LoggedIn")
            else:
                print("Error in login")


        except NoSuchElementException as e:
            print(e)
        finally:
            self.quit()


obj = LoginPage()
obj.login()


