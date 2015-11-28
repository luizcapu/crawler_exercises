__author__ = 'luiz'

from bs4 import BeautifulSoup, NavigableString
import urllib2
from collector_interface import CollectorInterface


class DefaultCollector(CollectorInterface):

    def __init__(self, url):
        self.url = url
        self.domain = self._get_url_domain(self.url)

        f = urllib2.urlopen(url)
        self.html_content = str(f.read())
        f.close()

        self.bs = BeautifulSoup(self.html_content, 'html.parser')
        [s.extract() for s in self.bs.findAll('script')]  # remove script tags
        [s.extract() for s in self.bs.findAll('style')]  # remove style tags
        self.max_scored_node = None

    def _get_url_domain(self, url):
        try:
            return url.split("/")[2]
        except:
            return None  # consider invalid url

    def _node_text(self, node):
        if node.string:
            return node.string.strip()
        else:
            return "".join([c.string.strip() for c in node.children if isinstance(c, NavigableString)])

    def _node_text_len(self, node):
        return len(self._node_text(node))

    def _parse_node(self, node):
        result = self._node_text_len(node) + 0.5 * self._children_score(node.children)
        if self.max_scored_node is None or self.max_scored_node[1] < result:
            self.max_scored_node = (node, result)
        return result

    def _children_score(self, children):
        result = 0
        for child in children:
            if not isinstance(child, NavigableString):
                result += self._parse_node(child)
        return result

    def extract_content(self):
        if self.bs.body:
            for child in self.bs.body.contents:
                if not isinstance(child, NavigableString):
                    self._parse_node(child)
            return str(self.max_scored_node[0]).strip() if self.max_scored_node else None

    def get_children_urls(self):
        return set([
            a["href"]
            for a in self.bs.find_all('a', href=True)
            if self._get_url_domain(a["href"]) == self.domain
        ])
