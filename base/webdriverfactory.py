"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations
Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""

from selenium import webdriver
import traceback

class WebDriverFactory():

    def __init__(self, browser):
        """
        Inits WebDriverFactory class
        """
        self.browser = browser


    def getWebDriverInstance(self):
        """
        Get WebDriver Instance based on the browser configuration

        :return:'WebDriver Instance'
        """
        baseURL = "https://courses.letskodeit.com/"
        if self.browser == "iexplorer":
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox()

        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(baseURL)
        return driver