from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class Inflow:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

    def get_info(self, query):
        try:
            self.query = query
            self.driver.get("https://www.wikipedia.org/")
            search_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "searchInput"))
            )
            search_input.send_keys(query)
            # Add a short delay to ensure the input is processed
            self.driver.implicitly_wait(1)
            search_input.send_keys(Keys.RETURN)  # Press Enter key instead of clicking the button
        except Exception as e:
            print("An error occurred:", e)
