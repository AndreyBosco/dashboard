import pytest
import time
from selenium import webdriver

@pytest.fixture(scope="module")
def browser():
    #chrome_path = r"C:\Users\andrey.bosco\Desktop\Jenkins-Python\chrome-win64\chrome.exe"    
    chorme_options = webdriver.ChromeOptions()

    #chorme_options.binary_location = chrome_path
    #Os dois comando abaixo é apenas para o projeto
    chorme_options.add_argument('--headless')
    chorme_options.add_argument('--disable-gpu')
    
    driver = webdriver.Chrome(options=chorme_options)

    yield driver
    driver.quit()

