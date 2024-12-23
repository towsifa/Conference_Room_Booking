import pytest
from selenium import webdriver
from config.browser_config import BrowserConfig


@pytest.fixture
def setup():
    if BrowserConfig.BROWSER_NAME == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        if BrowserConfig.HEADLESS_MODE:
            chrome_options.add_argument('--headed')
        driver = webdriver.Chrome(chrome_options)

    elif BrowserConfig.BROWSER_NAME == 'firefox':
        firefox_options = webdriver.FirefoxOptions()
        if BrowserConfig.HEADLESS_MODE:
            firefox_options.add_argument('--headed')
        driver = webdriver.Firefox(firefox_options)

    elif BrowserConfig.BROWSER_NAME == 'edge':
        edge_options = webdriver.EdgeOptions()
        if BrowserConfig.HEADLESS_MODE:
            edge_options.add_argument('--headless')
        driver = webdriver.Edge(edge_options)

    else:
        raise ValueError("Unsupported Browser!!")

    yield driver
    driver.quit()
