import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()  # Здесь можно использовать другой драйвер в зависимости от браузера
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_view_products(driver):
    base_url = "https://example.com"
    driver.get(base_url)
    driver.find_element(By.LINK_TEXT, "Одежда").click()
    driver.find_element(By.CSS_SELECTOR, ".product").click()
    assert driver.find_element(By.CSS_SELECTOR, ".product-details").is_displayed()

def test_add_to_cart(driver):
    base_url = "https://example.com"
    driver.get(base_url)
    driver.find_element(By.LINK_TEXT, "Электроника").click()
    driver.find_element(By.CSS_SELECTOR, ".product").click()
    driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
    assert driver.find_element(By.CSS_SELECTOR, ".cart-item").is_displayed()

def test_place_order(driver):
    base_url = "https://example.com"
    driver.get(base_url)
    driver.find_element(By.LINK_TEXT, "Книги").click()
    driver.find_element(By.CSS_SELECTOR, ".product").click()
    driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
    driver.find_element(By.LINK_TEXT, "Корзина").click()
    assert driver.find_element(By.CSS_SELECTOR, ".cart-item").is_displayed()
    driver.find_element(By.LINK_TEXT, "Оформить заказ").click()
    assert driver.find_element(By.CSS_SELECTOR, ".checkout-page").is_displayed()

def test_view_delivery_info(driver):
    base_url = "https://example.com"
    driver.get(base_url)
    driver.find_element(By.LINK_TEXT, "Информация о доставке").click()
    assert driver.find_element(By.CSS_SELECTOR, ".delivery-info-page").is_displayed()
