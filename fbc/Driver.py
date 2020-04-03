from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class Driver:
    chrome = None
    wait = None
    timeout = 60
    hide_browser = True

    @staticmethod
    def is_closed():
        try:
            Driver.chrome.title
        except:
            return True
        return False

    @staticmethod
    def reopen():
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-notifications')
        # print(Driver.hide_browser)
        if (Driver.hide_browser):
            options.add_argument('--headless')
        Driver.chrome = webdriver.Chrome(options=options)
        Driver.chrome.maximize_window()
        # setup for explicit wait
        Driver.wait = WebDriverWait(Driver.chrome, Driver.timeout)
        return Driver.chrome

def open():
    return Driver.reopen() if (Driver.is_closed()) else Driver.chrome

def close():
    if (not Driver.is_closed()):
        Driver.chrome.close()

def hide(flag):
    Driver.hide_browser = flag

def wait_until(func):
    Driver.wait.until(func)

def wait_until_not(func):
    Driver.wait.until_not(func)

    
# def __get_clear_browsing_button(driver):
#     """Find the "CLEAR BROWSING BUTTON" on the Chrome settings page."""
#     return driver.find_element_by_css_selector('* /deep/ #clearBrowsingDataConfirm')

# def clear_cache():
#     driver = open()
#     driver.get("chrome://settings/clearBrowserData")
#     wait = WebDriverWait(driver, 3)
#     wait.until(__get_clear_browsing_button)
#     __get_clear_browsing_button(driver).click()
#     wait.until_not(__get_clear_browsing_button)