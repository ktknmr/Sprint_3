import time

from data import xpath_buttons, xpath_links, xpath_inputs, login_data, urls
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestAuth:
    def test_login_on_main_page(self, driver):
        driver.get(urls['main_page'])
        driver.find_element(By.XPATH, xpath_buttons['Войти в аккаунт']).click()
        driver.find_element(By.NAME, "name").send_keys(login_data['old_email'])
        driver.find_element(By.NAME, "Пароль").send_keys(login_data['password'])
        driver.find_element(By.XPATH, xpath_buttons['Войти']).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, xpath_buttons['Личный Кабинет'])))
        driver.find_element(By.XPATH, xpath_buttons['Личный Кабинет']).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, xpath_inputs['Имя в ЛК'])))
        assert driver.current_url == urls['account_page']

    def test_login_on_personal_page(self, driver):
        driver.get(urls['main_page'])
        driver.find_element(By.XPATH, xpath_buttons['Личный Кабинет']).click()
        driver.find_element(By.NAME, "name").send_keys(login_data['old_email'])
        driver.find_element(By.NAME, "Пароль").send_keys(login_data['password'])
        driver.find_element(By.XPATH, xpath_buttons['Войти']).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, xpath_buttons['Личный Кабинет'])))
        driver.find_element(By.XPATH, xpath_buttons['Личный Кабинет']).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, xpath_inputs['Имя в ЛК'])))
        assert driver.current_url == urls['account_page']

    def test_login_sign_up_page(self, driver):
        driver.get(urls['main_page'])
        driver.find_element(By.XPATH, xpath_buttons['Войти в аккаунт']).click()
        driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()
        driver.find_element(By.XPATH, xpath_links['Войти']).click()
        driver.find_element(By.NAME, "name").send_keys(login_data['old_email'])
        driver.find_element(By.NAME, "Пароль").send_keys(login_data['password'])
        driver.find_element(By.XPATH, xpath_buttons['Войти']).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, xpath_buttons['Личный Кабинет'])))
        driver.find_element(By.XPATH, xpath_buttons['Личный Кабинет']).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, xpath_inputs['Имя в ЛК'])))
        assert driver.current_url == urls['account_page']

    def test_login_reset_password_page(self, driver):
        driver.get(urls['main_page'])
        driver.find_element(By.XPATH, xpath_buttons['Личный Кабинет']).click()
        driver.find_element(By.XPATH, xpath_links['Восстановить пароль']).click()
        driver.find_element(By.XPATH, xpath_links['Войти']).click()
        driver.find_element(By.NAME, "name").send_keys(login_data['old_email'])
        driver.find_element(By.NAME, "Пароль").send_keys(login_data['password'])
        driver.find_element(By.XPATH, xpath_buttons['Войти']).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, xpath_buttons['Личный Кабинет'])))
        driver.find_element(By.XPATH, xpath_buttons['Личный Кабинет']).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, xpath_inputs['Имя в ЛК'])))
        assert driver.current_url == urls['account_page']

    def test_logout(self, driver):
        driver.get(urls['main_page'])
        driver.find_element(By.XPATH, xpath_buttons['Войти в аккаунт']).click()
        driver.find_element(By.NAME, "name").send_keys(login_data['old_email'])
        driver.find_element(By.NAME, "Пароль").send_keys(login_data['password'])
        driver.find_element(By.XPATH, xpath_buttons['Войти']).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, xpath_buttons['Личный Кабинет'])))
        driver.find_element(By.XPATH, xpath_buttons['Личный Кабинет']).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, xpath_links['Выход'])))
        driver.find_element(By.XPATH, xpath_links['Выход']).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, xpath_buttons['Войти'])))
        assert driver.current_url == urls['login_page']