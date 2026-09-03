from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Finish_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    finish_button = "//button[@id='finish']"

    # Getters
    def get_finish_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.finish_button))
        )

    # Actions
    def click_finish_button(self):
        self.get_finish_button().click()
        print("Click finish button")

    # Methods
    def finish(self):
        # 1. Сначала кликаем (если это не было сделано в тесте ранее)
        self.click_finish_button()

        # 2. Явно ждем, пока URL изменится и будет содержать нужную строку
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("checkout-complete.html")
        )

        # 3. Только после этого делаем ассерт
        self.assert_url('https://www.saucedemo.com/checkout-complete.html')

        # 4. Делаем скриншот
        self.get_screenshot()