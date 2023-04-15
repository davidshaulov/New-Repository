from selenium.webdriver.common.by import By


class PickBusiness():

    def __init__(self, driver):
        self.driver = driver

    def choosing_step(self):

        self.driver.find_element(By.XPATH, value="//span[@class='name bm-subtitle-1']").click()
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.XPATH, value="//input[@placeholder='הכנס סכום']").send_keys("250")
        self.driver.find_element(By.XPATH, value="//button[@type='submit']").click()

