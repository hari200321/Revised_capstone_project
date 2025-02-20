"""base_page.py"""

#importing webdriver related modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#importing Expected conditions modules and Explicit waits
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

#importing Exception handling modules to handle the error gracefully
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException

#importing Action chains modules
from selenium.webdriver.common.action_chains import ActionChains

#Here im importing the Data class common python package
from common import Data

#here im importing Weblocators class from locators python package
from locators import WebLocators


#This is the parent class which inherit the Data and WebLocators
class WebAutomation(Data, WebLocators):

    #constructor
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 15)
        self.actions = ActionChains(self.driver)

    #Here im starting the automation by maximizing the window using the URL
    def start(self):
        self.driver.maximize_window()
        self.driver.get(self.BASE_URL)

    #Here in login method im doing login with several username to check the validation also im using exception handling
    def login(self):
        try:  # Here im using the exception handling to handle errors gracefully
            self.driver.find_element(by=By.ID, value = self.username_locator).send_keys(self.USERNAME1)
            self.driver.find_element(by=By.ID, value = self.password_locator).send_keys(self.PASSWORD)
            self.driver.find_element(by=By.ID, value = self.login_locator).click()
            self.driver.back()

            self.driver.find_element(by=By.ID, value=self.username_locator).send_keys(self.USERNAME2)
            self.driver.find_element(by=By.ID, value=self.password_locator).send_keys(self.PASSWORD)
            self.driver.find_element(by=By.ID, value=self.login_locator).click()
            self.driver.back()

            self.driver.find_element(by=By.ID, value=self.username_locator).send_keys(self.USERNAME3)
            self.driver.find_element(by=By.ID, value=self.password_locator).send_keys(self.PASSWORD)
            self.driver.find_element(by=By.ID, value=self.login_locator).click()
            self.driver.back()

            self.driver.find_element(by=By.ID, value=self.username_locator).send_keys(self.USERNAME4)
            self.driver.find_element(by=By.ID, value=self.password_locator).send_keys(self.PASSWORD)
            self.driver.find_element(by=By.ID, value=self.login_locator).click()
            self.driver.back()

            return f"1) {self.USERNAME4} is Blocked others all are get logged in successfully"


        except (NoSuchElementException, ElementNotVisibleException) as error:
            return error

    #in this method im trying to login using wrong username to validate
    def login_using_invalid_name(self):
        try:

            self.driver.find_element(by=By.ID, value = self.username_locator).send_keys(self.INVALID_U_NAME)
            self.driver.find_element(by=By.ID, value = self.password_locator).send_keys(self.INVALID_PWD)
            self.driver.find_element(by=By.ID, value = self.login()).click()

            expected_msg = "Epic sadface: Username and password do not match any user in this service"

            err_msg = self.driver.find_element(by=By, value = self.err_mes_locator)
            displayed_err_msg = err_msg.text
            print("pass")

            assert displayed_err_msg == expected_msg

        except NoSuchElementException as error:
            print(error)

    #in this method im checking the whether the logout button is clickable or not
    def is_logout_clickable(self):
        try:


            self.driver.find_element(by=By.ID, value=self.username_locator).send_keys(self.USERNAME1)
            self.driver.find_element(by=By.ID, value=self.password_locator).send_keys(self.PASSWORD)
            self.driver.find_element(by=By.ID, value=self.login_locator).click()

            menu_locator = self.wait.until(EC.element_to_be_clickable((By.ID, self.menu_butn_locator)))
            menu_locator.click()

            logout_locator = self.wait.until(EC.element_to_be_clickable((By.ID, self.logout_locator)))
            logout_locator.click()
            return 'Pass: Logout button is functioning'

        except (NoSuchElementException, ElementNotVisibleException) as error:
            print(error)

    #in this method im checking the whether the logout button is visible or not
    def visibility_of_logout_button(self):
        try:

            self.driver.find_element(by=By.ID, value=self.username_locator).send_keys(self.USERNAME1)
            self.driver.find_element(by=By.ID, value=self.password_locator).send_keys(self.PASSWORD)
            self.driver.find_element(by=By.ID, value=self.login_locator).click()

            menu_locator = self.wait.until(EC.visibility_of_element_located((By.ID, self.menu_butn_locator)))
            menu_locator.click()

            logout_locator = self.wait.until(EC.visibility_of_element_located((By.ID, self.logout_locator)))
            logout_locator.click()
            return 'Pass: Logout button is Visible!'

        except NoSuchElementException as error:
            print(error)

   #in this method im checking the whether the cart button is visible or not
    def visibility_of_cart_button(self):
        try:
            self.driver.find_element(by=By.ID, value=self.username_locator).send_keys(self.USERNAME1)
            self.driver.find_element(by=By.ID, value=self.password_locator).send_keys(self.PASSWORD)
            self.driver.find_element(by=By.ID, value=self.login_locator).click()

            cart_button = self.wait.until(EC.visibility_of_element_located((By.ID, self.cart_button)))
            cart_button.click()

            return 'Pass: Cart Button button is Visible!'

        except (NoSuchElementException, ElementNotVisibleException) as error:
            print(error)

   # in this method im choosing the products, and add them to cart,
   # enter the username, and postal code details to move further
   # and do checkout, and took screenshot of checkout summary, and click finish to see confirmation message
    def choose_products(self):
        try:
            self.driver.find_element(by=By.ID, value=self.username_locator).send_keys(self.USERNAME1)
            self.driver.find_element(by=By.ID, value=self.password_locator).send_keys(self.PASSWORD)
            self.driver.find_element(by=By.ID, value=self.login_locator).click()

            self.driver.find_element(by=By.ID, value = self.add_to_Cart_back_pack_locator).click()
            self.driver.find_element(by=By.ID, value=self.add_to_cart_jacket_locator).click()
            self.driver.find_element(by=By.ID, value=self.add_to_cart_bike_light_locator).click()
            self.driver.find_element(by=By.ID, value=self.add_to_cart_t_shirt_locator).click()

            self.driver.find_element(by=By.ID, value = self.cart_button).click()

            self.driver.find_element(by=By.ID, value = self.checkout_locator).click()
            self.driver.find_element(by=By.ID, value = self.f_name_locator).send_keys(self.FIRST_NAME)

            self.driver.find_element(by=By.ID, value = self.l_name_locator).send_keys(self.LAST_NAME)
            self.driver.find_element(by=By.ID, value = self.zip_c_locator).send_keys(self.ZIP_CODE)


            self.driver.find_element(by=By.ID, value = self.continue_locator).click()


            self.driver.find_element(by=By.ID, value = self.finish_locator).click()
            self.driver.get(self.CHECKOUT_URL)
            self.driver.save_screenshot('D:\\Automation_practise\\Capstone_Project\\screenshot.png')
            return 'Automation done Successfully'

        except Exception as error:
            print(error)

   # once program finish this method will quit the program
    def shutdown(self):
        self.driver.quit()

#main Execution function
if __name__ == "__main__":
    hari = WebAutomation()
    hari.start()
    #print(hari.login())
    #print(hari.login_using_invalid_name())
    #print(hari.is_logout_clickable())
    #print(hari.visibility_of_logout_button())
    #print(hari.visibility_of_cart_button())
    print(hari.choose_products())
    hari.shutdown()

