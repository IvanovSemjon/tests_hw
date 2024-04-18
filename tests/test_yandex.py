from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager
from unittest import TestCase
from yandex import go_to_the_page

path = "https://passport.yandex.ru/auth/"
my_login = 'netologyIvanovsemjon@yandex.ru'
my_password = '9rv-JuS-wKn-Khu'

chrom_webdriver_path = ChromeDriverManager().install()
browser_service = Service(executable_path=chrom_webdriver_path)
browser = Chrome(service=browser_service)
browser.maximize_window()

class TestSomething(TestCase):
    def test_go_to_the_page(self):
        expected = 'Войдите с Яндекс ID'
        result = go_to_the_page(path)
        self.assertEqual(result, expected)



