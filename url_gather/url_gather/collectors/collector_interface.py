from abc import ABCMeta, abstractmethod

__author__ = 'luiz'


class CollectorInterface(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, url):
        """Receives an URL and do the job to extract html content and parse
        :param url: The URL to parse and extract content
        :type url: A string containing the URL
        :returns:  None
        """
        pass

    @abstractmethod
    def extract_content(self):
        """Parse URL content and decides what is relevant to be returned
        :returns:  A string with the relevant content for this collector
        """
        pass

    @abstractmethod
    def get_children_urls(self):
        """Parse URL hrefs children and decides which should be returned
        :returns:  An iterable (i.e. list, set) of strings of current URL hrefs children
        """
        pass
