from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLinks():
    def test_constructor_link(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/login')
        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/ul/li[1]/a').click()
        current_url = driver.current_url
        assert current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit()

    def test_logo_link(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/login')
        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/div/a').click()
        current_url = driver.current_url
        assert current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit()

    def test_unauth_user_page_link(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a').click()
        current_url = driver.current_url
        assert current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.quit()

    def test_auth_user_page_link(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(By.XPATH, "//button[. = 'Войти в аккаунт']").click()
        driver.find_element(By.NAME, "name").send_keys("mariakotkina61@yandex.ru")
        driver.find_element(By.NAME, "Пароль").send_keys("123456")
        driver.find_element(By.XPATH, "//button[. = 'Войти']").click()
        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a').click()
        current_url = driver.current_url
        assert current_url == 'https://stellarburgers.nomoreparties.site/account'
        driver.quit()