from .model.navigator import Browser
from .model.kustomer import Kustomer 

def login():
    browser = Browser()
    kustomer = Kustomer(browser)
    kustomer.open()
    kustomer.login()

def create():
    # Attach to current session in browser
    browser = Browser(attach_to_session=True)
    # Create Kustomer object to interact with browser
    kustomer = Kustomer(browser)
    # Actions of Kustomer
    kustomer.select_reports()
    kustomer.create_report()
    kustomer.build_report()

def delete():
    browser = Browser(attach_to_session=True)
    kustomer = Kustomer(browser)
    kustomer.select_reports()
    kustomer.delete_report('SS_Prueba_RPA')