from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class Music:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

    def play(self, query):
        try:
            self.query = query
            self.driver.get("https://www.youtube.com/")
            search_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, "search_query"))  # Correct selector for search input
            )
            search_input.send_keys(query)
            search_input.send_keys(Keys.RETURN)  # Press Enter to submit the search query
            
            # Wait for the search results to load
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "video-title"))
            )
            
            # Click on the first video link in the search results
            video_link = self.driver.find_element(By.ID, "video-title")
            video_link.click()
        except Exception as e:
            print("An error occurred:", e)