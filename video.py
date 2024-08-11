from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class music:
    def __init__(self):
        # Initialize ChromeDriver with the 'detach' option
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=Service(executable_path="C:\\chromedriver.exe"), options=chrome_options)
    def play(self, query):
        search_url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
        self.driver.get(search_url)
    
    
        self.driver.implicitly_wait(10)  
    
    
        video = self.driver.find_element(By.XPATH, '//*[@id="video-title"]')
        video.click()
#assist = music()
#assist.play("funny video for children")
