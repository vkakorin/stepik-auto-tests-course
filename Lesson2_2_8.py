import os
import time
from selenium import webdriver
browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/file_input.html")

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Viktor")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Kakorin")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("vkakorin@gmail.com")
    input4 = browser.find_element_by_name("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    input4.send_keys(file_path)
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(10)

    browser.quit()
#