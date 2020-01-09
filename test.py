#! python3
# Sending Messages on Messenger

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import os
import time

browser = webdriver.Firefox()
browser.get('https://mail.google.com/mail/u/0/#inbox')

# Nhập username
userElem = browser.find_element_by_id('identifierId')
userElem.send_keys('sadandboujee4474@gmail.com')
userElem.send_keys(Keys.ENTER)
time.sleep(2)  # Đợi browser load sang trang password

# Nhập password
passElem = browser.find_element_by_name('password')
passElem.send_keys('elpsycongroo')
passElem.send_keys(Keys.ENTER)
time.sleep(7)  # Đơi browser load sang trang chính của gmail.
# time.sleep() giúp dừng hẳng chương trình để đợi browser load xong file HTML mới
# vì nếu để chương trình chạy tiếp mà file HTML trên browser chưa load xong
# thì code kh tìm thấy các element đó được
# vì Selenium là giúp navigate browser, cho nên các element ở đây thuộc nhiều file HTML khác nhau
# chứ không giống như request chỉ get được một file HTML.
# Nếu code chạy kh được thì tăng thơi gian sleep lên, để browser load xong file HTML.

# Compose
composeElem = browser.find_element_by_class_name('z0')  # Tìm ra element của nút compose
composeElem.click()  # Xài method click() để nhấn.
time.sleep(5)

# Sending Email
recipientElem = browser.find_element_by_name('to')
recipientElem.send_keys(sys.argv[1])

subjectElem = browser.find_element_by_name('subjectbox')
subjectElem.send_keys(sys.argv[2])

message = ' '.join(sys.argv[3:])
subjectElem.send_keys(Keys.TAB + message + Keys.TAB + Keys.ENTER)
time.sleep(5)

browser.quit()

os.system('pause')
