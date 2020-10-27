import math
import time
from selenium import webdriver
browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    button = browser.find_element_by_tag_name("button")
    button.click()

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element_by_id('input_value').text
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    time.sleep(10)

    browser.quit()