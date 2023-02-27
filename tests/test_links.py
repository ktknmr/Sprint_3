from data import xpath_buttons, xpath_links, xpath_inputs, xpath_alerts, login_data, urls
from selenium.webdriver.common.by import By

class TestLinks:
    def test_constructor_link(self, driver):
        driver.get(urls['login_page'])
        driver.find_element(By.XPATH, xpath_buttons['Конструктор']).click()
        assert driver.current_url == urls['main_page']
        driver.quit()

    def test_logo_link(self, driver):
        driver.get(urls['login_page'])
        driver.find_element(By.XPATH, xpath_links['Лого']).click()
        assert driver.current_url == urls['main_page']
        driver.quit()

    def test_unauth_user_page_link(self, driver):
        driver.get(urls['main_page'])
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, xpath_buttons['Личный Кабинет']).click()
        assert driver.current_url == urls['login_page']
        driver.quit()

    def test_auth_user_page_link(self, driver):
        driver.get(urls['main_page'])
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, xpath_buttons['Личный Кабинет']).click()
        driver.find_element(By.NAME, "name").send_keys(login_data['email'])
        driver.find_element(By.NAME, "Пароль").send_keys(login_data['password'])
        driver.find_element(By.XPATH, xpath_buttons['Войти']).click()
        driver.find_element(By.XPATH, xpath_buttons['Личный Кабинет']).click()
        assert driver.find_element(By.XPATH, xpath_inputs['Имя в ЛК'])
        driver.quit()