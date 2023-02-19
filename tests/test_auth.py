from selenium import webdriver
from selenium.webdriver.common.by import By

class TestAuth():
    def test_login_on_main_page(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(By.XPATH, "//button[. = 'Войти в аккаунт']").click()
        driver.find_element(By.NAME, "name").send_keys("mariakotkina61@yandex.ru")
        driver.find_element(By.NAME, "Пароль").send_keys("123456")
        driver.find_element(By.XPATH, "//button[. = 'Войти']").click()
        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a').click()
        driver.quit()

    def test_login_on_personal_page(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a').click()
        driver.find_element(By.NAME, "name").send_keys("mariakotkina61@yandex.ru")
        driver.find_element(By.NAME, "Пароль").send_keys("123456")
        driver.find_element(By.XPATH, "//button[. = 'Войти']").click()
        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a').click()
        driver.quit()

    def test_login_sign_up_page(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(By.XPATH, "//button[. = 'Войти в аккаунт']").click()
        driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p/a').click()
        driver.find_element(By.NAME, "name").send_keys("mariakotkina61@yandex.ru")
        driver.find_element(By.NAME, "Пароль").send_keys("123456")
        driver.find_element(By.XPATH, "//button[. = 'Войти']").click()
        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a').click()
        driver.quit()

    def test_login_reset_password_page(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(By.XPATH, "//button[. = 'Войти в аккаунт']").click()
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[2]/a').click()
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p/a').click()
        driver.find_element(By.NAME, "name").send_keys("mariakotkina61@yandex.ru")
        driver.find_element(By.NAME, "Пароль").send_keys("123456")
        driver.find_element(By.XPATH, "//button[. = 'Войти']").click()
        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a').click()
        driver.quit()
