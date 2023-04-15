import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ReceiverInformationScreen():

    def __init__(self, driver):
        self.driver = driver

    def input_information(self):

        self.driver.execute_script("window.scrollBy(0, 360)")
        time.sleep(2)
        receiver_name = "פלוני"
        self.driver.find_element(By.XPATH, value="//input[@title='שם מקבל המתנה']").send_keys(receiver_name)
        assert receiver_name == "פלוני"
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.XPATH, value="//span[@alt='לאיזה אירוע?']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, value="//li[@value='10']").click()
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.XPATH, value="//span[@class='textarea-clear-all ']").click()
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.XPATH, value="//textarea[@class='parsley-success']").send_keys("מזל טוב עד 120 לא כולל מעמ")
        self.driver.find_element(By.XPATH, value="//input[@type='file']").send_keys('C:\Python-350x350.jpg')
        self.driver.execute_script("window.scrollBy(0, 60)")
        self.driver.find_element(By.XPATH, value="//button[@gtm='המשך']").click()
        self.driver.set_page_load_timeout(10)
        self.driver.execute_script("window.scrollBy(0, 150)")
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.CSS_SELECTOR, value="svg[gtm='method-email']").click()

        email_box = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//input[@placeholder='מייל מקבל/ת המתנה']")))
        email_box.send_keys('davidshaulov565@gmail.com')

        self.driver.find_element(By.XPATH, value="//input[@placeholder='שם שולח המתנה']").send_keys('דוד')

        self.driver.find_element(By.CSS_SELECTOR, value="button[gtm='המשך לתשלום']").click()
        time.sleep(4)