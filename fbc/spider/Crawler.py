from fbc import Driver
import time

class Crawler():

    def __init__(self, id):
        self.timeout = 10
        self.driver = Driver.open()
        self.driver.get("https://fb.com/%s" % (id))
        self.hide_header_area()
        
    def hide_header_area(self):
        script = "document.getElementById('headerArea').setAttribute('style', 'display: none')"
        self.driver.execute_script(script)

    def expand_comments(self, form):
        elms = form.find_elements_by_xpath(".//a[@role='button'][@href='#']")
        if (len(elms) > 0):
            elms[-1].click()

    def all_comments_loaded(self, form):
        try:
            form.find_element_by_xpath(".//span[@class='_3bu3 _7a93']")
            return False
        except:
            return True

    def extract_comments(self, form):
        comments = list()
        for elm in form.find_elements_by_xpath(".//div[@role='article']"):
            try:
                comments.append(elm.find_element_by_xpath('.//span[@class="_3l3x"]').text)
                comments.append(elm.find_element_by_xpath('.//span[@class="_3l3x _1n4g"]').text)
            except:
                pass
        return comments

    def crawl_comments(self):
        container = self.driver.find_element_by_id("mainContainer")
        article = container.find_element_by_xpath(".//div[@role='article']")
        form = article.find_element_by_tag_name("form")
        form.find_elements_by_xpath(".//a[@role='button']")[-1].click()

        # Wait for element appearring
        while(self.all_comments_loaded(form)):
            time.sleep(1)

        while(not self.all_comments_loaded(form)):
            time.sleep(1)
            self.expand_comments(form)

        return self.extract_comments(form)
            
            
