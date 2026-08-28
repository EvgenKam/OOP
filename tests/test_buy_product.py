import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from utilities.login_page import Login_page
from utilities.main_page import Main_page
from utilities.cart_page import Cart_page

def test_buy_product():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options
    )

    print("Start Test")

    # Авторизация
    login = Login_page(driver)
    login.authorization()

    # Работа с главной страницей (покупка товара)
    mp = Main_page(driver)
    mp.select_product()
    # 3. Переход к оформлению заказа (Checkout)
    cp = Cart_page(driver)
    cp.click_checkout_button()
    time.sleep(10)