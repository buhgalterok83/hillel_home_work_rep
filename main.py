import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestWebApp(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Здесь можно использовать другой драйвер в зависимости от браузера
        self.driver.implicitly_wait(10)

    def test_view_products(self):
        self.driver.get("https://example.com")
        self.driver.find_element(By.LINK_TEXT, "Одежда").click()
        self.driver.find_element(By.CSS_SELECTOR, ".product").click()
        self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, ".product-details").is_displayed())

    def test_add_to_cart(self):
        self.driver.get("https://example.com")
        self.driver.find_element(By.LINK_TEXT, "Электроника").click()
        self.driver.find_element(By.CSS_SELECTOR, ".product").click()
        self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
        self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, ".cart-item").is_displayed())

    def test_place_order(self):
        self.driver.get("https://example.com")
        self.driver.find_element(By.LINK_TEXT, "Книги").click()
        self.driver.find_element(By.CSS_SELECTOR, ".product").click()
        self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
        self.driver.find_element(By.LINK_TEXT, "Корзина").click()
        self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, ".cart-item").is_displayed())
        self.driver.find_element(By.LINK_TEXT, "Оформить заказ").click()
        self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, ".checkout-page").is_displayed())

    def test_view_delivery_info(self):
        self.driver.get("https://example.com")
        self.driver.find_element(By.LINK_TEXT, "Информация о доставке").click()
        self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, ".delivery-info-page").is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
