__author__ = 'luiz'

from bs4 import BeautifulSoup, NavigableString
import argparse
import os


class NodeFinder(object):

    def __init__(self, html_text):
        self.html_text = html_text
        self.bs = BeautifulSoup(self.html_text, 'html.parser')
        self.max_scored_node = None

    def node_text(self, node):
        if node.string:
            return node.string.strip()
        else:
            return "".join([c.string.strip() for c in node.children if isinstance(c, NavigableString)])

    def node_text_len(self, node):
        return len(self.node_text(node))

    def parse_node(self, node):
        result = self.node_text_len(node) + 0.5 * self.children_score(node.children)
        if self.max_scored_node is None or self.max_scored_node[1] < result:
            self.max_scored_node = (node, result)
        return result

    def children_score(self, children):
        result = 0
        for child in children:
            if not isinstance(child, NavigableString):
                result += self.parse_node(child)
        return result

    def run(self):
        for child in self.bs.body.contents:
            if not isinstance(child, NavigableString):
                self.parse_node(child)
        return self.max_scored_node[0] if self.max_scored_node else None

    @staticmethod
    def extract_file_content(file_path):
        if file_path and os.path.isfile(file_path):
            with open(file_path, "r+") as f:
                return "".join(f.readlines())
        else:
            raise Exception("File %s not found" % file_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--html_file", help="HTML source file path to parse and find node")
    args = parser.parse_args()

    if not args.html_file:
        parser.print_help()
        exit(0)

    nf = NodeFinder(NodeFinder.extract_file_content(args.html_file))
    print nf.run()
