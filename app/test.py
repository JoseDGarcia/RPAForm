from app.model.navigator import Browser
from app.model.kustomer import Kustomer 
from selenium.webdriver.common.keys import Keys

if __name__ == '__main__':
    browser = Browser(attach_to_session=True)
    childhood = browser.driver.find_elements_by_xpath("//div[contains(@class, 'ReactModal__Content')]//input[contains(@placeholder,'Customer Report')]")
    kustomer = Kustomer(browser)
    # focused_element = browser.send_above_keys('Conversation', childhood)
    # childhood = browser.driver.find_element_by_xpath("//div[contains(@class, 'ReactModal__Content')]//*[contains(text(),'Select Date Attribute')]")
    # focused_element = browser.send_above_keys('Conversation', childhood)
