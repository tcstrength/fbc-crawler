from selenium import webdriver

class Driver:
    chrome = None
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
        print(Driver.hide_browser)
        if (Driver.hide_browser):
            options.add_argument('--headless')
        Driver.chrome = webdriver.Chrome(options=options)
        Driver.chrome.maximize_window()
        return Driver.chrome

def open():
    return Driver.reopen() if (Driver.is_closed()) else Driver.chrome

def close():
    if (not Driver.is_closed()):
        Driver.chrome.close()

def hide(flag):
    Driver.hide_browser = flag