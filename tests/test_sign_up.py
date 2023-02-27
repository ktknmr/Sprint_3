from data import xpath_buttons, xpath_links, xpath_inputs, xpath_alerts, login_data, urls
from selenium.webdriver.common.by import By


class TestSignUp:
    def test_sign_up_success(self, driver):
        driver.get(urls['main_page'])
        driver.find_element(By.XPATH, xpath_buttons['Войти в аккаунт']).click()
        driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()
        driver.find_element(By.NAME, "name").send_keys(login_data['name'])
        driver.find_element(By.XPATH, xpath_inputs['Email']).send_keys(login_data['email'])
        driver.find_element(By.NAME, "Пароль").send_keys(login_data['password'])
        driver.find_element(By.XPATH, xpath_links['Зарегистрироваться']).click()
        assert driver.current_url == urls['login_page']
        driver.quit()

    def test_sign_up_failed(self, driver):
        driver.get(urls['main_page'])
        driver.find_element(By.XPATH, xpath_buttons['Войти в аккаунт']).click()
        driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()
        driver.find_element(By.NAME, "name").send_keys(login_data['name'])
        driver.find_element(By.XPATH, xpath_inputs['Email']).send_keys( login_data['email'])
        driver.find_element(By.NAME, "Пароль").send_keys(login_data['bad_password'])
        driver.find_element(By.XPATH, xpath_links['Зарегистрироваться']).click()
        assert driver.find_element(By.XPATH, xpath_alerts['Некорректный пароль'])
        driver.quit()