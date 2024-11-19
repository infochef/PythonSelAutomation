import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def pytest_addoption(parser):
    parser.addoption(
        '--browser_name', action='store', default='chrome', help='Name of the browser to use (chrome, firefox, edge)'
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption('browser_name')  # Corrected case of 'getoption'

    if browser_name == 'chrome':
        service_obj = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name == 'firefox':
        service_obj = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service_obj)
    elif browser_name == 'edge':
        service_obj = Service(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service_obj)
    else:
        raise ValueError(f"Unsupported browser name: {browser_name}")

    driver.get('https://rahulshettyacademy.com/angularpractice/')
    driver.maximize_window()

    request.cls.driver = driver
    yield driver

    driver.quit()  # Use quit() instead of close() to ensure all instances are closed
