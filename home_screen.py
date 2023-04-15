import time

from selenium.webdriver.common.by import By


class HomeScreen():

    def __init__(self, driver):
        self.driver = driver

    def selection_bar(self):
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0, 360)")
        first_category = self.driver.find_element(By.XPATH, "//span[@title='סכום']")
        self.driver.execute_script("arguments[0].click();", first_category)
        self.driver.implicitly_wait(2)

        self.driver.find_element(By.XPATH, value="//li[@value='3']").click()
        second_category = self.driver.find_element(By.XPATH, "//span[@title='אזור']")
        self.driver.execute_script("arguments[0].click();", second_category)
        self.driver.implicitly_wait(2)

        self.driver.find_element(By.XPATH, value="//li[@value='9']").click()
        self.driver.find_element(By.XPATH, value="//span[@title='קטגוריה']").click()
        self.driver.implicitly_wait(2)

        self.driver.find_element(By.XPATH, value="//li[@value='22']").click()
        self.driver.implicitly_wait(2)

        self.driver.find_element(By.XPATH, value="//a[@rel='nofollow']").click()
