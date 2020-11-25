from base.basepage import BasePage
#Importing logging and custom logger for logger make records from CustomLogger module and not from SElenium Driver
from utilities.custom_logger import customLogger as CL
import logging


class NavigationPage(BasePage):

    log = CL(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _home = "HOME"#LinkText
    _allCourses = "ALL COURSES"#LinkText#
    _support = "SUPPORT"#LinkText#
    _myCourses = "MY COURSES"#LinkText#
    _userIcon = "//button[@id='dropdownMenu1']/span[text()='My Account']"#xpath
    _myAccount = "My Account "#LinkText

    def navigateToHomeScreen(self):
        self.elementClick(self._home, locatorType='LINKTEXT')

    def navigateToAllCoursesScreen(self):
        self.elementClick(self._allCourses, locatorType='LINKTEXT')

    def navigateToSupportScreen(self):
        self.elementClick(self._support, locatorType='LINKTEXT')

    def navigateToMyCoursesScreen(self):
        self.elementClick(self._myCourses, locatorType='LINKTEXT')

    def clickOnMyAccountIcon(self):
        self.elementClick(self._userIcon, locatorType='XPATH')

    def clickOnMyAccountLink(self):
        self.elementClick(self._myAccount, locatorType='LINKTEXT')

    def navigateToMyAccount(self):
        self.clickOnMyAccountIcon()
        self.clickOnMyAccountLink()