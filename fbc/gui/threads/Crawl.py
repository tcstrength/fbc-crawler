from PyQt5 import QtCore
from fbc import Stream
from fbc.spider.Crawler import Crawler

class CrawlThread(QtCore.QThread):
    one_crawled = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.count = 0

    def set_posts(self, posts):
        self.posts = posts

    def run(self):
        for post in self.posts:
            cr = Crawler(post)
            comments = cr.crawl_comments()
            for cmt in comments:
                Stream.write(cmt)
                self.count += cmt.count(' ')
                self.count += cmt.count('\n')
            self.one_crawled.emit()