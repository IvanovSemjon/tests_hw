import time
import requests

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager



def wait_element(browser, delay_seconds=1, by=By.TAG_NAME, value=None):
    return WebDriverWait(browser, delay_seconds).until(
        expected_conditions.presence_of_element_located((by, value))
    )

path = "https://passport.yandex.ru/auth/"
my_login = 'netologyIvanovsemjon@yandex.ru'
my_password = '9rv-JuS-wKn-Khu'

chrom_webdriver_path = ChromeDriverManager().install()
browser_service = Service(executable_path=chrom_webdriver_path)
browser = Chrome(service=browser_service)
browser.maximize_window()


def go_to_the_page(adress):
    browser.get(adress)
    time.sleep(2)
    result = requests.head("https://passport.yandex.ru/auth/")
    text_login = wait_element(browser, 1, By.CLASS_NAME, "passp-add-account-page-title")
    value_text_login = text_login.text
    return value_text_login


def input_login(login):
    user_name = wait_element(browser, 1, By.XPATH, "//*[@id='passp-field-login']")
    user_name.send_keys(login)

    button_login = wait_element(browser, 1, By.XPATH, "//*[@id='passp:sign-in']")
    button_login.click()


def input_password(password):
    user_password = wait_element(browser, 1, By.ID, "passp-field-passwd")
    user_password.send_keys(password)
    time.sleep(2)

    button_login = wait_element(browser, 1, By.ID, "passp:sign-in")
    button_login.click()
    time.sleep(20)


if __name__ == "__main__":
    go_to_the_page(path)
    input_login(my_login)
    input_password(my_password)
