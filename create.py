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


    def login(self):
        self.login = self.driver.find_element_by_xpath('')
        

    def select_reports(self):
        reports = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/nav/div/span[3]/a')
        
KustomerFormRPA()