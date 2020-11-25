from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TestStatus
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUpCoursePage", "setUp")
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self, oneTimeSetUpCoursePage):
        self.rc = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def testEmptyCardCredentials(self):
        self.rc.enrollCourse(courseNameBox="javascript", courseName="JavaScript")
        result = self.rc.verifyEnrollFailed_incompleteCardNum()
        self.ts.markFinal("testEmptyCardCredentials", result, "Credit card number error message")

    @pytest.mark.run(order=2)
    def testIncorrectCardCredentials(self):
        self.rc.enterCreditCardInformation("4534 5345 3634 6344", "1123", "545")
        result = self.rc.verifyEnrollFailed_incorrect_declinedCardNum()
        self.ts.markFinal("testIncorrectCardCredentials", result, "Credit card credentials are incorrect")



#Test data
    #ccNumber = 5454 5045 0524 1258
    #cc_expy = 1123
    #cc_cvv = 545


