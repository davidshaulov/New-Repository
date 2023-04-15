from selenium.webdriver.common.by import By


class RegistrationScreen():
    def __init__(self, driver):
        self.driver = driver

    def press_and_enter_details(self):

        self.driver.find_element(By.XPATH, value="//li[@class='notSigned']").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, value="//span[@class='text-link theme']").click()
        name = "david"
        self.driver.find_element(By.XPATH, value="//input[@placeholder='שם פרטי']").send_keys(name)
        assert name == "david"
        self.driver.find_element(By.XPATH, value="//input[@placeholder='מייל']").send_keys("davidshaulov054@gmail.com")
        self.driver.find_element(By.XPATH, value="//input[@placeholder='סיסמה']").send_keys("David.s.123")
        self.driver.find_element(By.XPATH, value="//input[@placeholder='אימות סיסמה']").send_keys("David.s.123")

        registration_button = self.driver.find_element(By.XPATH, value="//span[@class='label']")
        self.driver.execute_script("arguments[0].scrollIntoView()", registration_button)

        confirm_button = self.driver.find_element(By.XPATH, value="//div[@role='checkbox']")
        self.driver.execute_script("arguments[0].click();", confirm_button)
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.XPATH, value="//button[@gtm='הרשמה ל-BUYME']").click()
