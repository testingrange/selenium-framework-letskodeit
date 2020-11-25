"""
@package base

Base Page class implementation
It implements methods which are common to all the pages throughout the application
k
This class needs to be inherited by all the page classes
This should not be used by creating object instances

Example:
    Class LoginPage(BasePage)
"""

from base.selenium_driver import SeleniumDriverCust
from traceback import print_stack
from utilities.util import Util

class BasePage(SeleniumDriverCust):

    def __init__(self, driver):
        """
        Inits BasePage class
        Returns:
            None
        """
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util()

    def verifyPageTitle(self, titleToVerify):
        """
        Verify the page Title
        :param titleToVerify: Title on the page that needs to be verified
        """
        try:
            actualTitle = self.getTitle()
            return self.util.verifyTextContains(actualTitle, titleToVerify)
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False