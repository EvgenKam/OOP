from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    # Локатор Add to  в корзину
    product_1 = "//button[@data-test='add-to-cart-sauce-labs-backpack']"
    # Локатор   корзины
    cart = "//div[@id='shopping_cart_container']"

    # Getters
    def get_product_1(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_1))
        )

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart))
        )

    # Actions
    def click_select_product_1(self):
        self.get_product_1().click()
        print("Click select product 1")

    def click_cart(self):
        self.get_cart().click()
        print("Click cart")

    # Methods
    def select_product(self):
        self.get_current_url()
        self.click_select_product_1()
        self.click_cart()