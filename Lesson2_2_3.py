from selenium.webdriver.support.ui import Select
import time
from selenium import webdriver

browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/selects1.html")

    x = browser.find_element_by_id("num1").text
    y = browser.find_element_by_id("num2").text
    z = str(int(x) + int(y))

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(z)
    browser.find_element_by_class_name("btn.btn-default").click()

finally:
    time.sleep(10)
    browser.quit()
#