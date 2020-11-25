from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TestStatus
import unittest, pytest
from ddt import ddt, data, unpack
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriverCust as SD

@pytest.mark.usefixtures("oneTimeSetUpCoursePage", "setUp")
@ddt
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self, oneTimeSetUpCoursePage):
        self.rc = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.sd = SD(self.driver)

    @pytest.mark.run(order=1)
    @data(("javascript", "JavaScript", "4534 5345 3634 6245", "1123", "545", "Your card was declined."), ("selenium Webdriver with Python", "Selenium WebDriver With Python 3.x", "5454 5045 0524 1258", "1123", "545", "Credit card credentials are incorrect"))
    @unpack
    def testEmptyCardCredentials(self, courseNameBox, courseName, num, exp, cvv, errorMessage):
        self.rc.enrollCourse(courseNameBox, courseName, num, exp, cvv)
        result = self.rc.verify_CC_ErrorMessage(errorMessage)
        self.ts.markFinal("testIncorrectCardCredentials", result, str(errorMessage))
        self.sd.webScroll("up", 4)
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "ALL COURSES").click()
        #self.ts.markFinal("testEmptyCardCredentials", result, "Credit card number error message")

    # @pytest.mark.run(order=2)
    # def testIncorrectCardCredentials(self):
    #     self.rc.enterCreditCardInformation("4534 5345 3634 6344", "1123", "545")
    #     result = self.rc.verifyEnrollFailed_incorrect_declinedCardNum()
    #     self.ts.markFinal("testIncorrectCardCredentials", result, "Credit card credentials are incorrect")


    #"4534 5345 3634 6344", "Your card number is incorrect."

    #Test data
    #ccNumber = 5454 5045 0524 1258
    #cc_expy = 1123
    #cc_cvv = 545


