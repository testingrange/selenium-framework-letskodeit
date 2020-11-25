from base.basepage import BasePage
#Importing logging and custom logger for logger make records from CustomLogger module and not from SElenium Driver
from utilities.custom_logger import customLogger as CL
import logging
from pages.home.navigation_page import NavigationPage


class LoginPage(BasePage):

    log = CL(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    _login_link = "//a[text()='Sign In']"
    _email_field = "email"
    _password_field = "password"
    _login_button = "//input[contains(@value, 'Login')]"

    # Locators for test verification
    _userIcon = "//button[@id='dropdownMenu1']/span[text()='My Account']"
    _loginError = "//input[@id='email']//following-sibling::span[text()='Your username or password is invalid. Please try again.']"
    _logingBtn_verify = "//input[@value='Login']"

    def clickSignBtn(self):
        self.elementClick(self._login_link, locatorType='XPATH')

    def enterEmailFld(self, email):
        self.sendKeysToElement(email, self._email_field, locatorType='ID')

    def enterPasswrdFld(self, password):
        self.sendKeysToElement(password, self._password_field, locatorType='ID')

    def clickLoginBtn(self):
        self.elementClick(self._login_button, locatorType='XPATH')

    def login(self, email="", password=""):
        self.clickSignBtn()
        self.clearFields()
        self.enterEmailFld(email)
        self.enterPasswrdFld(password)
        self.util.sleep(3, "Create an interval input of information and clicking the button")
        self.clickLoginBtn()

    def verifyLoginSuccess(self):
        result = self.isElementPresent(self._userIcon, "XPATH")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent(self._loginError, "XPATH")
        return result

    def verifyEmptyFldsLoginFailed(self):
        result = self.isElementPresent(self._logingBtn_verify, "XPATH")
        return result

    def clearFields(self):
        emailField = self.getElement(self._email_field)
        emailField.clear()
        passworddField = self.getElement(self._password_field)
        passworddField.clear()

    def verifyLoginTitle(self, title):
        return self.verifyPageTitle(title)
