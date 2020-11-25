from base.basepage import BasePage
from utilities.custom_logger import customLogger as CL
import logging


class RegisterCoursesPage(BasePage):

    log = CL(logging.INFO)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Test data
    #ccNumber = 5454 5045 0524 1258
    #cc_expy = 1123
    #cc_cvv = 545

    #Variables
    course = "JavaScript"

    #Locators
    _searchBox = "//input[contains(@id,'search') and contains(@name,'course')]" #xpath
    _searchBtn = "//button[@class='find-course search-course']" #xpath
    _course = "//div[@class='zen-course-list']//h4[contains(text(),'{0}')]" #xpath
    _category = "categories"
    #select all cources
    _enrollBtn = "//button[text()='Enroll in Course']" #xpath
    _cc_num = "//input[@placeholder='Card Number']" #xpath
    _cc_exp = "//input[@placeholder='MM / YY']" #xpath
    _cc_cvc = "//input[@placeholder='Security Code']" #xpath
    _country = "country-list" #name Select
    _buyBtn = "//div[@class='panel payment-panel']//button[contains(.,'Buy')][1]" #xpath



    # locators for later test cases
    _pay_paypal = ""
    _pay_later = ""

    #Locators for test verification
    _cc_error_message = "//p[contains(.,'{0}')]"
    _cc_error_message1 = '//li[contains(.,"{0}")]' #Your card's expiration date is incomplete.
    _enroll_error_message = "//li[.='{0}']" #xpath //Your card number is incomplete.
    _incorrect_ccnumber_error_message = "//p[contains(.,'Your card number is incorrect.')]" #xpath
    _declined_card_error_message = "//p[contains(.,'Your card was declined.')]"  # xpath

    #Locators for possible later verifications and tests
    _error_message_dismiss = "//p[contains(.,'Your card number is incorrect.')]/button" #xpath

    ###Test methods below

    def enterCourseName(self, courseName):
        self.sendKeysToElement(courseName, self._searchBox, locatorType='XPATH')

    def clickSearchBtn(self):
        self.elementClick(self._searchBtn, locatorType="XPATH" )

    def selectCourse(self, courseName):
        self.elementClick(self._course.format(courseName), locatorType="XPATH")

    def enrollIntoCourse(self):
        self.elementClick(self._enrollBtn, locatorType="XPATH")

    def enterCardNum(self, cardNumber):
        self.switchToFrameForAction(self._cc_num, locatorType="XPATH", mode="iframe", action="sendkeys", data=cardNumber)
        #self.sendKeysToElement(cardNumber, self._cc_num, locatorType="XPATH")

    def enterCardExp(self, expNum):
        self.switchToFrameForAction(self._cc_exp, locatorType="XPATH", mode="iframe", action="sendkeys",
                                    data=expNum)
        #self.sendKeysToElement(expNum, self._cc_exp, locatorType="ID")

    def enterCVV(self, cvc):
        self.switchToFrameForAction(self._cc_cvc, locatorType="XPATH", mode="iframe", action="sendkeys",
                                    data=cvc)
        #self.sendKeysToElement(cvc, self._cc_cvc, locatorType="ID")

    def selectCountry(self):
        #Need to create method for select
        pass

    def clickBuyBtn(self):
        self.elementClick(self._buyBtn, locatorType="XPATH")

    def enterCreditCardInformation(self, num, exp, cvv):
        self.util.sleep(0.5, "wait for page")
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCVV(cvv)
        self.clickBuyBtn()

    def enrollCourse(self, courseNameBox, courseName="", num="", exp="", cvv=""):
        self.util.sleep(0.5, "Waiting for page to appear")
        self.enterCourseName(courseNameBox)
        self.util.sleep(0.5, "Entering course name")
        self.clickSearchBtn()
        self.util.sleep(0.5, "press search button")
        self.selectCourse(courseName)
        self.util.sleep(0.5, "Enroll into course")
        self.enrollIntoCourse()
        self.webScroll("down", 4)
        self.enterCreditCardInformation(num, exp, cvv)

    def verifyEnrollFailed_incompleteCardNum(self):
        result = self.isElementPresent(self._enroll_error_message, locatorType="XPATH")
        return result

    def verifyEnrollFailed_incorrect_declinedCardNum(self):
        if self.waitforElement(self._incorrect_ccnumber_error_message, locatorType="XPATH"):
            return True
        elif self.waitforElement(self._declined_card_error_message, locatorType="XPATH"):
            return True
        else:
            return False

    def verify_CC_ErrorMessage(self, errorMessage, element1=None, element2=None, element3=None):
        if element1 == "":
            if self.waitforElement(self._cc_error_message1.format(errorMessage), locatorType="XPATH"):
                return True
            else:
                return False
        elif element2 == "":
            if self.waitforElement(self._cc_error_message1.format(errorMessage), locatorType="XPATH"):
                return True
            else:
                return False
        elif element3 == "":
            if self.waitforElement(self._cc_error_message1.format(errorMessage), locatorType="XPATH"):
                return True
            else:
                return False
        elif self.waitforElement(self._cc_error_message.format(errorMessage), locatorType="XPATH"):
            return True
        else:
            return False
