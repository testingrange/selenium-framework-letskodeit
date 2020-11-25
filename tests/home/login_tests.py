from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)


    @pytest.mark.run(order=4)
    def test_validLogin(self):
        self.lp.login("michaelsole75@gmail.com", "MS75gl")
        result = self.lp.verifyLoginTitle("All Courses")
        self.ts.mark(result, "Title is incorrect")
        result2 = self.lp.verifyLoginSuccess()
        self.ts.markFinal("test_validLogin", result2, "Login was not successful")


    @pytest.mark.run(order=1)
    def test_invalidLogin_emptyFields(self):
        self.lp.login()
        result = self.lp.verifyEmptyFldsLoginFailed()
        assert result == True
        result2 = self.lp.verifyLoginTitle("Login")
        assert result2 == True


    @pytest.mark.run(order=2)
    def test_invalidLogin_email(self):
        self.lp.login("test@jmail.com", "MS75gl")
        # result = self.lp.verifyLoginFailed()
        # self.ts.mark(result, "Test failed")
        result = self.lp.verifyLoginFailed()
        self.ts.mark(result, "Test failed")
        result2 = self.lp.verifyLoginTitle("Login")
        self.ts.mark(result2, "Title is incorrect")


    @pytest.mark.run(order=3)
    def test_invalidLogin_password(self):
        self.lp.login("michaelsole75@gmail.com", "testtest")
        result = self.lp.verifyLoginFailed()
        assert result == True
        result2 = self.lp.verifyLoginTitle("Login")
        assert result2 == True




