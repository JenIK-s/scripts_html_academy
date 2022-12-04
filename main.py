from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


username = 'fertuv68@gmail.com'
password = 'Gnusmasmonus23'
tasks_link = 'https://up.htmlacademy.ru/univer-html1/1/module/7/item/10/20'

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get('https://htmlacademy.ru/login')

login_input = driver.find_element(By.NAME, 'email')
login_input.send_keys(username)

password_input = driver.find_element(By.ID, 'login-password')
password_input.send_keys(password)
password_input.send_keys(Keys.ENTER)

sleep(3)

driver.get(tasks_link)

task_count = driver.find_element(By.CSS_SELECTOR, '.course-nav__stat')
count = task_count.text
count = count.split('/')
count = int(count[1])

a = 0
while a != count:
    sleep(3)

    button = driver.find_element(By.CSS_SELECTOR, '.button.button--close')
    button.click()

    sleep(2)

    button = driver.find_element(
        By.CSS_SELECTOR,
        '.course-editor-controls__item.course-editor-controls__item--answer'
    )
    button.click()

    WebDriverWait(
        driver, 100
    ).until(
        EC.element_to_be_clickable(
            (
                By.CSS_SELECTOR,
                ".course-goals__button.course-goals__button--next.button.button--green.button--without-border"
            )
        )
    ).click()
    a += 1
