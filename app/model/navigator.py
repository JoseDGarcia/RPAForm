from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import time
import json
import os

SESSION_DIR = './app/session.json'

class Browser():
    def __init__(self, attach_to_session=False):
        # print(os.listdir())
        if not attach_to_session:
            self.create_session()
        else:
            self.attach_to_session()
        self.driver.maximize_window()

    '''
    Session operations
    '''
    def attach_to_session(self):
        session_id, executor_url = self.load_session()
        original_execute = WebDriver.execute
        def new_command_execute(self, command, params=None):
            if command == "newSession":
                # Mock the response
                return {'success': 0, 'value': None, 'sessionId': session_id}
            else:
                return original_execute(self, command, params)
        # Patch the function before creating the driver object
        WebDriver.execute = new_command_execute
        self.driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
        self.driver.session_id = session_id
        # Replace the patched function with original function
        WebDriver.execute = original_execute

    def create_session(self):
        self.driver = webdriver.Chrome()
        session_id = self.driver.session_id
        executor_url = self.driver.command_executor._url
        self.save_session(session_id, executor_url)

    def create_action_chain(self):
        return ActionChains(self.driver)

    def save_session(self, session_id, executor_url):
        session = {
            "session_id": session_id,
            "executor_url": executor_url
        }
        with open(SESSION_DIR, 'w') as session_file:
            json.dump(session, session_file)
            session_file.close()

    def load_session(self):
        with open(SESSION_DIR) as session_file:
            session = json.load(session_file)
            session_file.close()
        return session['session_id'], session['executor_url']

    '''
    URL operations
    '''
    def open_page(self, page):
        self.driver.get(page)

    '''
    Find operations
    '''
    def find_element(self, name, option):
        if option == 'xpath':
            return self.driver.find_element_by_xpath(name)
        elif option == 'class_name':
            return self.driver.find_element_by_class_name(name)
        elif option == 'css_selector':
            return self.driver.find_element_by_css_selector(name)
        else:
            return self.driver.find_element_by_link_text(name)
    
    def find_element_before(self, name, option):
        if option == 'xpath':
            return WebDriverWait(self.driver, 30).until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH , name)
                )
            )
        elif option == 'class_name':
            return WebDriverWait(self.driver, 30).until(
                expected_conditions.presence_of_element_located(
                    (By.CLASS_NAME , name)
                )
            )
        elif option == 'css_selector':
            return WebDriverWait(self.driver, 30).until(
                expected_conditions.presence_of_element_located(
                    (By.CSS_SELECTOR, name)
                )
            )
        else:
            return WebDriverWait(self.driver, 30).until(
                expected_conditions.presence_of_element_located(
                    (By.LINK_TEXT , name)
                )
            )

    def find_elements(self, name, option):
        if option == 'xpath':
            return self.driver.find_elements_by_xpath(name)
        elif option == 'class_name':
            return self.driver.find_elements_by_class_name(name)
        elif option == 'css_selector':
            return self.driver.find_elements_by_css_selector(name)
        else:
            return self.driver.find_elements_by_link_text(name)

    '''
    Actions
    '''
    def send_above_keys(self, text, element):
        action = self.create_action_chain()
        focused_element = action.move_to_element(element).move_by_offset(0, 0)
        focused_element.click().perform()
        focused_element.send_keys(text+Keys.ENTER).perform()

    def send_above_click(self, element):
        action = self.create_action_chain()
        focused_element = action.move_to_element(element).move_by_offset(0, 0)
        focused_element.click().perform()
      
