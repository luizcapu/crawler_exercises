__author__ = 'luiz'

from datetime import datetime


class TestCustomCollector(object):

    def __init__(self, url):
        pass

    def extract_content(self):
        return "Custom content %s" % datetime.utcnow()

    def get_children_urls(self):
        return []
