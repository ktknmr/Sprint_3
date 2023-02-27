from data import xpath_links, urls
from selenium.webdriver.common.by import By
import time

class TestConstructor:
    def test_bride_section(self, driver):
        driver.get(urls['main_page'])
        driver.find_element(By.XPATH, xpath_links['Соусы']).click()
        time.sleep(1)
        driver.find_element(By.XPATH, xpath_links['Булки']).click()
        time.sleep(1)
        assert driver.find_element(By.XPATH, xpath_links['Флюоресцентная булка R2-D3']).is_displayed()

    def test_sauce_section(self, driver):
        driver.get(urls['main_page'])
        driver.find_element(By.XPATH, xpath_links['Соусы']).click()
        time.sleep(1)
        assert driver.find_element(By.XPATH, xpath_links['Соус Spicy-X']).is_displayed()

    def test_filling_section(self, driver):
        driver.get(urls['main_page'])
        driver.find_element(By.XPATH, xpath_links['Начинки']).click()
        time.sleep(1)
        assert driver.find_element(By.XPATH, xpath_links['Говяжий метеорит (отбивная)']).is_displayed()