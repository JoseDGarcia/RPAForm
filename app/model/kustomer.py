from selenium.webdriver.common.keys import Keys
import json
import os
from time import sleep

KUSTOMER_CONFIG = 'app/extra/kustomer.json'

class Kustomer:
    def __init__(self, browser):
        self.browser = browser
        self.load_config()

    def load_config(self):
        self.config = json.load(open(KUSTOMER_CONFIG, encoding='utf-8'))  

    def open(self):
        self.browser.open_page(self.config['url'])

    def login(self):
        # Click on google login
        login_button = self.browser.find_element_before(
            self.config['login']['google_button']['name'],
            self.config['login']['google_button']['option']
        )
        self.browser.send_above_click(login_button)

    def select_reports(self):
        self.browser.find_element_before(
            self.config['slidebar']['reporting']['name'],
            self.config['slidebar']['reporting']['option']
        ).click()

    def create_report(self):
        # Request from user
        custom_report = CustomReport()
        # Create new report
        self.browser.find_element_before(
            self.config['reporting']['new']['new_button']['name'],
            self.config['reporting']['new']['new_button']['option']
        ).click()
        self.browser.find_element_before(
            self.config['reporting']['new']['modal_input']['name'],
            self.config['reporting']['new']['modal_input']['option']
        ).send_keys(custom_report.name)
        self.browser.find_element_before(
            self.config['reporting']['new']['add_report_button']['name'],
            self.config['reporting']['new']['add_report_button']['option']
        ).click()
    
    def build_report(self):
        # Request from user
        custom_report = CustomReport()
        # Create Chart
        for chart in custom_report.template['data']:
            '''
            First Part
            '''
            # Add chart
            self.browser.find_element_before(
                self.config['reporting']['add_chart']['add_chart_button']['name'],
                self.config['reporting']['add_chart']['add_chart_button']['option']
            ).click()
            # Select blank template
            self.browser.find_element_before(
                self.config['reporting']['add_chart']['add_chart_template']['name'],
                self.config['reporting']['add_chart']['add_chart_template']['option']
            ).click()
            # Add chart style
            self.browser.find_element_before(
                self.config['reporting']['add_chart']['add_chart_style']['name'].replace('[style]', chart['style']), 
                self.config['reporting']['add_chart']['add_chart_style']['option']
            ).click()
            # Next Button
            self.browser.find_element_before(
                self.config['reporting']['add_chart']['next_button']['name'],
                self.config['reporting']['add_chart']['next_button']['option']
            ).click()
            '''
            Second Part
            '''
            # Add report type
            report_type = self.browser.find_element_before(
                self.config['reporting']['add_chart']['second_step']['report_type']['name'],
                self.config['reporting']['add_chart']['second_step']['report_type']['option']
            )
            self.browser.send_above_keys(chart['report_type'], report_type)
            # Add report date attribute
            date_attribute = self.browser.find_element_before(
                self.config['reporting']['add_chart']['second_step']['date_attribute']['name'],
                self.config['reporting']['add_chart']['second_step']['date_attribute']['option']
            )
            self.browser.send_above_keys(chart['attributes'], date_attribute)

            # Add segmentation
            attribute_calculation = chart['attribute_calculation']
            self._build_segmentation(attribute_calculation)

            # Match all and any
            self._build_match_operator(chart['all_filter'], is_and=True)
            self._build_match_operator(chart['any_filter'])

            # Wait for chart refresh or error...
            sleep(3)

            # Next
            self.browser.find_element_before(
                self.config['reporting']['add_chart']['next_button']['name'],
                self.config['reporting']['add_chart']['next_button']['option']
            ).click()

            '''
            Third part
            '''
            # Title
            title_input = self.browser.find_element_before(
                self.config['reporting']['add_chart']['third_step']['title_input']['name'],
                self.config['reporting']['add_chart']['third_step']['title_input']['option']
            ).send_keys(chart['title'])

            # Next
            self.browser.find_element_before(
                self.config['reporting']['add_chart']['save_button']['name'],
                self.config['reporting']['add_chart']['save_button']['option']
            ).click()

    def _build_segmentation(self, attribute_calculation):
        for index, attribute in enumerate(attribute_calculation):
            action_input = self.browser.find_element_before(
                self.config['reporting']['add_chart']['second_step']['segmentation']['action']['name'],
                self.config['reporting']['add_chart']['second_step']['segmentation']['action']['option']
            )
            self.browser.send_above_keys(attribute['action'], action_input)
            property_input = self.browser.find_element_before(
                self.config['reporting']['add_chart']['second_step']['segmentation']['property']['name'],
                self.config['reporting']['add_chart']['second_step']['segmentation']['property']['option']
            )
            self.browser.send_above_keys(attribute['action_property'], property_input)
            if 'extra_option' in attribute.keys():
                aux_input = self.browser.find_element_before(
                    self.config['reporting']['add_chart']['second_step']['segmentation']['aux']['name'],
                    self.config['reporting']['add_chart']['second_step']['segmentation']['aux']['option']
                )
                self.browser.send_above_keys(attribute['extra_option'], aux_input)
            if index < len(attribute_calculation) - 1:
                add_action_button = self.browser.find_element_before(
                    self.config['reporting']['add_chart']['second_step']['segmentation']['add_button']['name'],
                    self.config['reporting']['add_chart']['second_step']['segmentation']['add_button']['option']
                )
                self.browser.send_above_click(add_action_button)
    
    def _build_match_operator(self, elements, is_and=False):
        button_index = 0 if is_and else 1
        for index, attribute in enumerate(elements):
            add_action_button = self.browser.find_elements(
                self.config['reporting']['add_chart']['second_step']['operators_button']['name'],
                self.config['reporting']['add_chart']['second_step']['operators_button']['option']
            )[button_index]
            self.browser.send_above_click(add_action_button)

            action_input = self.browser.find_element_before(
                self.config['reporting']['add_chart']['second_step']['operators_input']['name'],
                self.config['reporting']['add_chart']['second_step']['operators_input']['option']
            )
            combinacion_macabra = attribute['field'] + Keys.ENTER + attribute['operator']
            if 'value' in attribute.keys():
                combinacion_macabra += Keys.ENTER + attribute['value']
            self.browser.send_above_keys(combinacion_macabra, action_input)

    def delete_report(self, name):
        result = self.browser.search_and_click(name, self.config['reporting']['slidebar']['custom_reports'])
        if result:
            self.browser.click_before(self.config['reporting']['misc']['misc_button'])
            self.browser.click_before(self.config['reporting']['misc']['delete'])
            self.browser.wait_until(self.config['reporting']['delete_chart']['modal'])
            confirm = input("Escriba Y para confirmar la eliminación.")
            if confirm.lower() == 'y':
                self.browser.click(self.config['reporting']['delete_chart']['button'])
        else:
            raise Exception("Element not found")


REQUEST = 'app/extra/request.json'
TEMPLATE = 'app/templates/'
class CustomReport:
    def __init__(self):
        config = json.load(open(REQUEST, encoding='utf-8'))  
        self.name = config['name']
        self.queues = config['queues']
        self.language = config['language'].lower()
        self.is_rt = config['is_rt']
        self.load_template()

    def load_template(self):
        url = os.path.join(TEMPLATE, self.language)
        url += 'rt' if self.is_rt else ''
        url += '.json'
        self.template = json.load(open(url, encoding='utf-8'))
        for i in range(len(self.template['data'])):
            for queue in self.queues:
                queue_option = {
                    "field": "Queue", 
                    "operator": "Is Equal To" if self.language == 'en' else 'Es igual a', 
                    "value": queue
                }

                self.template['data'][i]['any_filter'].append(queue_option)