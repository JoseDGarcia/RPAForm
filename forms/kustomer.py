from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions
import time
import json

class KustomerFormRPA():

    def __init__(self):
        self.load_config()
        self.driver = webdriver.Chrome()
        self.driver.get('https://rappi.kustomerapp.com/')

    def load_config(self):
        self.config = json.load(open('configurations/kustomer.json'))  

    def login(self):
        login_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH , self.config['login']['google']['button'])
            )
        )
        login_button.click()

        login_finished = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH , self.config['login']['google']['login_input'])
            )
        )


    def select_reports(self):
        reports = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/nav/div/span[3]/a')
        
form = KustomerFormRPA()
form.login()