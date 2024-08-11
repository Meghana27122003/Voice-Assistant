from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class infow:
    def __init__(self):
        # Initialize ChromeDriver with the 'detach' option
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=Service(executable_path="C:\\chromedriver.exe"), options=chrome_options)

    def get_info(self, query):
        # Directly pass the URL to driver.get()
        self.query = query
        self.driver.get("http://www.wikipedia.org")
        # Find the search input element using the updated method
        search = self.driver.find_element(By.XPATH, '//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        # Find the search button using the updated method
        enter = self.driver.find_element(By.XPATH, '//*[@id="search-form"]/fieldset/button')
        enter.click()