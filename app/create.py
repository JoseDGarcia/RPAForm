from model.navigator import Browser
from model.kustomer import Kustomer 

if __name__=='__main__':
    # Attach to current session in browser
    browser = Browser(attach_to_session=True)
    # Create Kustomer object to interact with browser
    kustomer = Kustomer(browser)
    # Actions of Kustomer
    kustomer.select_reports()
    kustomer.create_report()
    kustomer.build_report()
    