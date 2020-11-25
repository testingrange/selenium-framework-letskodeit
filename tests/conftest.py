import pytest
from base.webdriverfactory import WebDriverFactory
from pages.home.login_page import LoginPage

@pytest.fixture()
def setUp():
    print("**BEFORE every method***")
    yield
    print("***AFTER every method***")


@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("\n================================\nONE TIME !!! BEFORE All the methods\n================================")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    # lp = LoginPage(driver)
    # lp.login("michaelsole75@gmail.com", "MS75gl")
    # 4266 8416 1160 6102 -> Your card is declined. Please contact your Bank/Card Issuer for more information.
    # if browser == 'firefox':
    #     #     baseURL = "https://courses.letskodeit.com/"
    #     #     driver = webdriver.Firefox()
    #     #     driver.implicitly_wait(6)
    #     #     driver.maximize_window()
    #     #     driver.get(baseURL)
    #     #     print("Running test on FF")
    #     # else:
    #     #     baseURL = "https://courses.letskodeit.com/"
    #     #     driver = webdriver.Chrome()
    #     #     driver.implicitly_wait(6)
    #     #     driver.maximize_window()
    #     #     driver.get(baseURL)
    #     #     print("Running tests on chrome")

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    print("\n================================\nONE TIME AFTER !!! All the methods\n================================")

@pytest.fixture(scope="class")
def oneTimeSetUpCoursePage(request, browser):
    print("\n================================\nONE TIME !!! BEFORE All the methods\n================================")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    lp = LoginPage(driver)
    lp.login("michaelsole75@gmail.com", "MS75gl")
    # 4266 8416 1160 6102 -> Your card is declined. Please contact your Bank/Card Issuer for more information.
    # if browser == 'firefox':
    #     #     baseURL = "https://courses.letskodeit.com/"
    #     #     driver = webdriver.Firefox()
    #     #     driver.implicitly_wait(6)
    #     #     driver.maximize_window()
    #     #     driver.get(baseURL)
    #     #     print("Running test on FF")
    #     # else:
    #     #     baseURL = "https://courses.letskodeit.com/"
    #     #     driver = webdriver.Chrome()
    #     #     driver.implicitly_wait(6)
    #     #     driver.maximize_window()
    #     #     driver.get(baseURL)
    #     #     print("Running tests on chrome")

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    #driver.quit()
    print("\n================================\nONE TIME AFTER !!! All the methods\n================================")


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

