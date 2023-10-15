from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import time

# 指定Chrome WebDriver的路径
chrome_driver_path = os.path.join(
    os.getcwd(), "selenium_learn", "chromedriver.exe"
)  # 替换为实际的路径

print("path:", chrome_driver_path)

# 启动Chrome浏览器
# driver = webdriver.Chrome(executable_path=chrome_driver_path)

browser = webdriver.Chrome()

# 打开教务系统登录页面
browser.get("http://yjs.ctgu.edu.cn/yjs/login.jsp")
# browser.get("https://www.baidu.com")
# # 填写用户名和密码
username = browser.find_element(by=By.NAME, value="j_username")  # 用你的网站上的用户名输入字段ID替换
password = browser.find_element(by=By.NAME, value="j_password")  # 用你的网站上的密码输入字段ID替换
# 清空框里面的内容
username.clear()
password.clear()
# 填入信息
username.send_keys("202308540421039")
password.send_keys("lch20001975")


# # 提交登录表单
login_button = browser.find_element(by=By.NAME, value="Submit")
# login_button.click()
time.sleep(30.0)
# # 进入选课页面
# driver.get("https://your-education-system-url/course-registration")

# # 找到目标课程并点击选课按钮
# course_to_enroll = driver.find_element_by_id("course-id")  # 用你要抢的课程的ID替换
# enroll_button = driver.find_element_by_id("enroll-button")  # 用你的网站上的选课按钮ID替换

# enroll_button.click()

# # 处理选课结果，例如，检查是否成功选课，发送通知等

# # 关闭浏览器
# driver.close()
