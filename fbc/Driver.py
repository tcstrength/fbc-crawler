from selenium import webdriver

class Driver:
    chrome = None
    hide_browser = True

    @classmethod
    def is_closed(cls):
        try:
            cls.chrome.title
        except:
            return True
        return False

    @classmethod
    def reopen(cls):
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-notifications')
        print(cls.hide_browser)
        if (cls.hide_browser):
            options.add_argument('--headless')
        cls.chrome = webdriver.Chrome(options=options)
        cls.chrome.maximize_window()
        return cls.chrome

    @classmethod
    def hide(cls, flag):
        cls.hide_browser = flag

def open():
    return Driver.reopen() if (Driver.is_closed()) else Driver.chrome

def close():
    try:
        Driver.chrome.close()
    except:
        pass