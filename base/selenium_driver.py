from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from traceback import print_stack
from utilities.custom_logger import customLogger as CL
import logging
import time
import os
# from selenium import webdriver
# driver = webdriver.Chrome()
class SeleniumDriverCust():

    log = CL(logging.INFO)

    def __init__(self, driver):
        self.driver = driver

    def screenShot(self, resultMessage):
        """
        Takes screenshot of the current open web page
        """
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        print(relativeFileName)
        currentDirectory = os.path.dirname(__file__)
        print(currentDirectory)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        print(destinationFile)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)
        print(destinationDirectory)
        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot saved to directory: " + destinationFile)
        except:
            self.log.error("### Exception Occurred")
            print_stack()


    def getTitle(self):
        title = self.driver.title
        self.log.info("Title of the page is " + title)
        return title

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        if locatorType == "name":
            return By.NAME
        if locatorType == "class":
            return By.CLASS_NAME
        if locatorType == "xpath":
            return By.XPATH
        if locatorType == "linktext":
            return By.PARTIAL_LINK_TEXT
        if locatorType == "css":
            return By.CSS_SELECTOR
        else:
            self.log.error("Locator type " + locatorType + " is not supported")
            return False

    def getElement(self, locator, locatorType='id'):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.driver.find_element(self.getByType(locatorType), locator)
            self.log.info("ELement with locator: " + locator + " and locatorType: " + locatorType + " was found")
        except:
            self.log.error("ELement with locator: " + locator + " and locatorType: " + locatorType + " wasn't found")
        return element

    def getElements(self, locator, locatorType='id'):
        """
        Get list of elements with common locator
        :param locator:
        :param locatorType:
        :return:
        """
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.driver.find_elements(self.getByType(locatorType), locator)
            self.log.info("ELements with locator: " + locator + " and locatorTypes: " + locatorType + " was found")
        except:
            self.log.error("ELements with locator: " + locator + " and locatorTypes: " + locatorType + " wasn't found")
        return element

    def isElementPresent(self, locator, locatorType='id'):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element Found")
                return True
            else:
                self.log.error("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def isElementDisplayed(self, locator, locatorType):
        isDisplayed = False
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element is displayed with locator: " + locator +
                              " locatorType: " + locatorType)
            else:
                self.log.error("Element not displayed with locator: " + locator +
                              " locatorType: " + locatorType)
            return isDisplayed
        except:
            self.log.error("Element is displayed with locator: " + locator +
                              " locatorType: " + locatorType)
            return False

    def elementPresenceCheck(self, locator, locatorType='id'):
        try:
            elementList = self.getElements(locator, locatorType)
            if len(elementList) > 0:
                self.log.info("Element found")
                return True
            else:
                self.log.warn("Element not found")
                return False
        except:
            self.log.error("Exception. Element not found")
            return False


    def waitforElement(self, locator, locatorType='id', timeout=10, pollFrequency=0.5):
        element = None
        try:
            self.log.info("Waiting for max " + str(timeout) + " seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout, pollFrequency, ignored_exceptions = [NoSuchElementException, ElementNotVisibleException,
                                                                                                             ElementNotInteractableException,
                                                                                                             ElementNotSelectableException])
            element = wait.until(EC.presence_of_element_located((self.getByType(locatorType), locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.error("Element not appeared on the web page")
        return element


    def elementClick(self, locator="", locatorType="id", element=None):
        """
        Click on an element
        Provide element or a combination of locator and locatorType
        :param locator:
        :param locatorType:
        :return:
        """
        try:
            if locator: #if it's not empty
                element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Click on element with locator: " + locator + " and locator Type: " + locatorType)
        except:
            self.log.error("Cannot click on the element")
            print_stack()

    def sendKeysToElement(self, data, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Data: " + str(data) + " was sent to the element with locator: " + locator + " and locator Type: " + locatorType)
        except:
            self.log.error("Cannot send data to the element")
            print_stack()

    def getText(self, locator="", locatorType="id", info=""):
        """
        Get 'Text' on an element
        Either provide element or a combination of locator and locatorType
        :param locator:
        :param locatorType:
        :param info:
        :return:
        """
        try:
            element = self.getElement(locator, locatorType)
            self.log.debug("Before finding text")
            text = element.text
            self.log.info("size of the text is " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on lement :: " + info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            text = None
        return text

    def webScroll(self, direction='up', scale=1):
        """
        Method for scrolling up or down the web page
        :param direction:
        :return:
        """
        #i=1
        if direction.lower() == "up":
            for i in range(scale):
                self.driver.execute_script("window.scrollBy(0, -200);")

        if direction.lower() == "down":
            for i in range(scale):
                self.driver.execute_script("window.scrollBy(0, 200);")


    def switchToFrameForAction(self, locator, locatorType, mode="iframe", action="click", data=""):

        iframeList = self.getElements("//iframe", "XPATH")
        self.log.debug("There are " + str(len(iframeList)) + " elements in the iframeList")
        for i in range(len(iframeList)):
            #print(iframeList[i])
            self.driver.switch_to.frame(i)
            self.log.debug("cycle = " + str(i))
            try:
                #element = self.getElement(locator, locatorType)
                if self.elementPresenceCheck(locator, locatorType):
                    self.log.debug("Element found")
                    if action.lower() == "sendkeys":
                        self.sendKeysToElement(data, locator, locatorType)
                        self.log.info("Keys were sent to the element")
                        self.driver.switch_to.default_content()
                        break
                else:
                    self.log.debug("element not found")
            except:
                self.log.debug("Error happened on cycle " + str(i))
            #time.sleep(1)
            self.driver.switch_to.default_content()









        ###########################################################


        # if mode.lower() == "iframe":
        #     frameList = len(self.getElements("//iframe", "XPATH"))
        #     self.log.info("There are " + str(frameList) + " items in the list.")
        #
        #     try:
        #         elementPresent = False
        #         i = 0
        #         while elementPresent is not True or i < frameList:
        #         #for i in range(frameList):
        #             self.driver.switch_to.frame(i)
        #             self.log.debug("frame number " + str(i))
        #             if self.elementPresenceCheck(locator, locatorType):
        #                 self.log.info("Element located in iframe with index: " + str(i))
        #                 time.sleep(1)
        #                 element = self.getElement(locator, locatorType)
        #                 element.clear()
        #                 self.log.info("Clearing element with locator: " + locator + " and LocatorType: " + locatorType)
        #
        #                 if action.lower() == "click":
        #                     self.elementClick(locator, locatorType)
        #                 elif action.lower() == "sendkeys":
        #                     self.sendKeysToElement(data, locator, locatorType)
        #                 elementPresent = True
        #             i+=1
                    # elif action.lower() == "clear":
                    #     element = self.getElement(locator, locatorType)
                    #     element.clear()
                    #     self.log.info("Clearing element with locator: " + locator + " and LocatorType: " + locatorType)
                    # else:
                    #     self.log.error("Couldn't perform " + str(action) + " action in the iframe with index: " + str(i))
        #             self.log.info("Return to default screen")
        #             self.driver.switch_to.default_content()
        #     except:
        #         self.log.error("Couldn't perform " + str(action) + " action in iframes")
        # else:
        #     self.log.error("Couldn't switch to " + str(mode) + " mode.")
