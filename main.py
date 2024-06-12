from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

chrome_options = webdriver.ChromeOptions()

chrome_driver_path = r"./chromedriver.exe"
chrome_options.binary_location = r"./chrome-win64/chrome.exe"
prefs = {"profile.managed_default_content_settings.images": 2}

chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--disable-infobars')
chrome_options.add_argument('--disable-images')
chrome_options.add_experimental_option("prefs", prefs)

chrome_service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

driver.get('https://56okuh4f3vnkrmk3iv3nx6sqxu0evxdb.lambda-url.us-east-1.on.aws/')

try:
    wait = WebDriverWait(driver, 5)
    button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'g-recaptcha')))
    button.click()
    
    time.sleep(1)

    token = wait.until(EC.presence_of_element_located((By.ID, 'r-token')))
    token_value = token.text

    print(f'Token: {token_value}')

finally:
    driver.quit()