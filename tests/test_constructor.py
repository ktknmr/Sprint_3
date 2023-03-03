from data import xpath_links, urls
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestConstructor:
    def test_bride_section(self, driver):
        driver.get(urls['main_page'])
        driver.find_element(By.XPATH, xpath_links['Соусы']).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, xpath_links['Соус Spicy-X'])))
        driver.find_element(By.XPATH, xpath_links['Булки']).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, xpath_links['Флюоресцентная булка R2-D3'])))

    def test_sauce_section(self, driver):
        driver.get(urls['main_page'])
        driver.find_element(By.XPATH, xpath_links['Соусы']).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, xpath_links['Соус Spicy-X'])))

    def test_filling_section(self, driver):
        driver.get(urls['main_page'])
        driver.find_element(By.XPATH, xpath_links['Начинки']).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, xpath_links['Говяжий метеорит (отбивная)'])))