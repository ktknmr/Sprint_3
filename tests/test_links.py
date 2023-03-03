from data import xpath_buttons, xpath_links, xpath_inputs, xpath_alerts, login_data, urls
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

class TestLinks:
    def test_constructor_link(self, driver):
        driver.get(urls['login_page'])
        driver.find_element(By.XPATH, xpath_buttons['Конструктор']).click()
        assert driver.current_url == urls['main_page']

    def test_logo_link(self, driver):
        driver.get(urls['login_page'])
        driver.find_element(By.XPATH, xpath_links['Лого']).click()
        assert driver.current_url == urls['main_page']

    def test_unauth_user_page_link(self, driver):
        driver.get(urls['main_page'])
        driver.find_element(By.XPATH, xpath_buttons['Личный Кабинет']).click()
        assert driver.current_url == urls['login_page']

    def test_auth_user_page_link(self, driver):
        driver.get(urls['main_page'])
        driver.find_element(By.XPATH, xpath_buttons['Личный Кабинет']).click()
        driver.find_element(By.NAME, "name").send_keys(login_data['old_email'])
        driver.find_element(By.NAME, "Пароль").send_keys(login_data['password'])
        driver.find_element(By.XPATH, xpath_buttons['Войти']).click()
        WebDriverWait(driver, 3)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, xpath_buttons['Личный Кабинет'])))
        driver.find_element(By.XPATH, xpath_buttons['Личный Кабинет']).click()
        WebDriverWait(driver, 25).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, xpath_inputs['Имя в ЛК'])))
        assert driver.current_url == urls['account_page']