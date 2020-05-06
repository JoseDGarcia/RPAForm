from model.navigator import Browser
from model.kustomer import Kustomer 

if __name__=='__main__':
    browser = Browser(attach_to_session=True)
    kustomer = Kustomer(browser)
    kustomer.select_reports()
    kustomer.delete_report('SS_Prueba_RPA')
    