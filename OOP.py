import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from utilities.login_page import Login_page


def test_buy_product():
    # ========== НАСТРОЙКИ ИЗ ВИДЕО 3 ==========
    # Создаем объект опций для Chrome
    options = Options()

    # Убираем системные логи Chrome (из Видео 3)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    # Чтобы браузер не закрывался сразу после теста
    options.add_experimental_option("detach", True)

    # Инициализация драйвера с настройками
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options  # Передаем настройки
    )
    # ============================================

    print("Start Test: Авторизация и покупка товара")

    # Авторизация (метод сам открывает страницу)
    login = Login_page(driver)
    login.authorization()  # Без параметров!

    # Ждем загрузки страницы товаров
    WebDriverWait(driver, 10).until(EC.url_contains("inventory.html"))
    print("Страница с товарами успешно загружена!")

    # Выбираем товар (индекс начинается с 1)
    product_index = 1

    # Локаторы для товаров
    name_locator = f"(//div[contains(@class, 'inventory_item_name')])[{product_index}]"
    price_locator = f"(//div[contains(@class, 'inventory_item_price')])[{product_index}]"
    add_btn_locator = f"(//button[contains(@class, 'btn_inventory')])[{product_index}]"

    # Ждем появления товара
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, name_locator))
    )

    # Получаем данные о товаре
    product_name = driver.find_element(By.XPATH, name_locator).text.strip()
    product_price = driver.find_element(By.XPATH, price_locator).text.strip()

    print(f"Выбран товар: {product_name}, Цена: {product_price}")

    # Добавляем в корзину
    add_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, add_btn_locator))
    )
    add_btn.click()
    print("Товар добавлен в корзину")

    # Переход в корзину
    cart_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
    )
    cart_link.click()
    print("Переход в корзину")

    # Ждем загрузки страницы корзины
    WebDriverWait(driver, 10).until(EC.url_contains("cart.html"))

    # Ждем появления товара в корзине
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "(//div[contains(@class, 'inventory_item_name')])[1]")
        )
    )

    # Проверяем товар в корзине
    cart_name = driver.find_element(
        By.XPATH, "(//div[contains(@class, 'inventory_item_name')])[1]"
    ).text.strip()

    cart_price = driver.find_element(
        By.XPATH, "(//div[contains(@class, 'inventory_item_price')])[1]"
    ).text.strip()

    # Assert-проверки
    assert product_name == cart_name, "Название товара в корзине не совпадает!"
    assert product_price == cart_price, "Цена товара в корзине не совпадает!"

    print(" Проверки пройдены успешно!")

    # Задержка чтобы увидеть результат
    time.sleep(5)

    # Закрываем браузер
    driver.quit()


# Запуск теста
if __name__ == "__main__":
    test_buy_product()