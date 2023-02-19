from selenium import webdriver
from selenium.webdriver.common.by import By

class TestSignUp():
    def test_sign_up_success(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(By.XPATH, "//button[. = 'Войти в аккаунт']").click()
        driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()
        driver.find_element(By.NAME, "name").send_keys("Мария")
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys("mariakotkina61@yandex.ru")
        driver.find_element(By.NAME, "Пароль").send_keys("123456")
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()
        driver.quit()

    def test_sign_up_failed(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(By.XPATH, "//button[. = 'Войти в аккаунт']").click()
        driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()
        driver.find_element(By.NAME, "name").send_keys("Мария")
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys("mariakotkina61@yandex.ru")
        driver.find_element(By.NAME, "Пароль").send_keys("12345")
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()
        current_url = driver.current_url
        assert current_url == 'https://stellarburgers.nomoreparties.site/register'
        driver.quit()