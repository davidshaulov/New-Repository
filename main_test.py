import json
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Webproject.registration_screen import RegistrationScreen
from Webproject.home_screen import HomeScreen
from Webproject.pick_business import PickBusiness
from Webproject.receiver_information_screen import ReceiverInformationScreen


class AutomationTest(TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        json_file = open('C:\\nested_data.json', 'r')
        data = json.load(json_file)
        for user in data['users']:
            print(user)

        cls.driver = webdriver.Chrome(service=Service("C:\\Users\\dshaul2x\\Downloads\\chromedriver_win32.exe"))
        cls.driver.maximize_window()
        cls.driver.get('https://buyme.co.il/')
        cls.Registration_Screen = RegistrationScreen(cls.driver)
        cls.Home_Screen = HomeScreen(cls.driver)
        cls.Pick_business = PickBusiness(cls.driver)
        cls.Receiver_information_screen = ReceiverInformationScreen(cls.driver)

    """ This function registers the user to the website """

    def test_01_registration_screen(self):
        self.Registration_Screen.press_and_enter_details()

    """ This function selects categories for choosing the coupon """

    def test_02_Home_Screen(self):
        self.Home_Screen.selection_bar()

    """ This function selects the coupon """

    def test_03_Pick_Business(self):
        self.Pick_business.choosing_step()

    """ This function fills the details for sending the coupon """

    def test_04Information_Screen(self):
        self.Receiver_information_screen.input_information()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

