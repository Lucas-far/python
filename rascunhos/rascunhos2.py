

import json
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# pip install requests2 pandas lxml

url = 'https://www.udemy.com/'
option = Options()
option.headless = True
driver = webdriver.Firefox(options=option)
driver.get(url)
# driver.quit()
