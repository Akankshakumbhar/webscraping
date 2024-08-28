from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome("C:/Users/Star/AppData/Local/Temp/Rar$EXa0.164/chromedriver-win64/chromedriver.exe")
driver.get("www.google.com")


