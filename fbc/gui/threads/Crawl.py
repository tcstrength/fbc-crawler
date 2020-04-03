from PyQt5 import QtCore
from fbc import Stream
from fbc.spider.Crawler import Crawler

class CrawlThread(QtCore.QThread):
    one_crawled = QtCore.pyqtSignal(str)
    error = QtCore.pyqtSignal(Exception, str)

    def __init__(self):
        super().__init__()
        self.count = 0

    def set_posts(self, posts):
        self.posts = posts

    def run(self):
        for post in self.posts:
            try:
                cr = Crawler(post)
                comments = cr.crawl_comments()
                for cmt in comments:
                    Stream.write(cmt)
                    self.count += cmt.count(' ')
                    self.count += cmt.count('\n')
                self.one_crawled.emit(post)
            except Exception as e:
                print(e)
                self.error.emit(e, post)