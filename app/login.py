from model.navigator import Browser
from model.kustomer import Kustomer 

if __name__=='__main__':
    browser = Browser()
    kustomer = Kustomer(browser)
    kustomer.open()
    kustomer.login()