import os
from selenium import webdriver
import time

# 指定Chrome WebDriver的路径
chrome_driver_path = os.path.join(
    os.getcwd(), "selenium_learn", "chromedriver.exe"
)  # 替换为实际的路径

# driver = webdriver.Chrome("D:\\dev\\py-learn\\selenium_learn\\chromedriver.exe")
driver = webdriver.Chrome()

driver.get("http://www.baidu.com")
time.sleep(3.0)
driver.quit()
