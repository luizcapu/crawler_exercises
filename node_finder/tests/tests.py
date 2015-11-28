__author__ = 'luiz'

import unittest

from node_finder.node_finder import NodeFinder


class NodeFinderTests(unittest.TestCase):
    _payload = [
        {
            "in": """
            <html><head><title>The Dormouse's story TITLE</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<div>
ABCDE
<div>
askjdhaskjdhaskjdh ashdkjas hdkj ashdjk sakjd jash djahskjdhaskjhdjkashdas dkja shjdhask
askjdhaskjdhaskjdh ashdkjas hdkj ashdjk sakjd jash djahskjdhaskjhdjkashdas dkja shjdhask
askjdhaskjdhaskjdh ashdkjas hdkj ashdjk sakjd jash djahskjdhaskjhdjkashdas dkja shjdhask
askjdhaskjdhaskjdh ashdkjas hdkj ashdjk sakjd jash djahskjdhaskjhdjkashdas dkja shjdhask
askjdhaskjdhaskjdh ashdkjas hdkj ashdjk sakjd jash djahskjdhaskjhdjkashdas dkja shjdhask
askjdhaskjdhaskjdh ashdkjas hdkj ashdjk sakjd jash djahskjdhaskjhdjkashdas dkja shjdhask
askjdhaskjdhaskjdh ashdkjas hdkj ashdjk sakjd jash djahskjdhaskjhdjkashdas dkja shjdhask
askjdhaskjdhaskjdh ashdkjas hdkj ashdjk sakjd jash djahskjdhaskjhdjkashdas dkja shjdhask
askjdhaskjdhaskjdh ashdkjas hdkj ashdjk sakjd jash djahskjdhaskjhdjkashdas dkja shjdhask
askjdhaskjdhaskjdh ashdkjas hdkj ashdjk sakjd jash djahskjdhaskjhdjkashdas dkja shjdhask
askjdhaskjdhaskjdh ashdkjas hdkj ashdjk sakjd jash djahskjdhaskjhdjkashdas dkja shjdhask
askjdhaskjdhaskjdh ashdkjas hdkj ashdjk sakjd jash djahskjdhaskjhdjkashdas dkja shjdhask
askjdhaskjdhaskjdh ashdkjas hdkj ashdjk sakjd jash djahskjdhaskjhdjkashdas dkja shjdhask
ESSSEEEEEEEEEEEEEEEE
</div>
</div>

<p class="story">...</p>
</body>
""",
            "out": """
<div>
askjdhaskjdhaskjdh ashdkjas hdkj ashdjk sakjd jash djahskjdhaskjhdjkashdas dkja shjdhask
askjdhaskjdhaskjdh ashdkjas hdkj ashdjk sakjd jash djahskjdhaskjhdjkashdas dkja shjdhask
askjdhaskjdhaskjdh ashdkjas hdkj ashdjk sakjd jash djahskjdhaskjhdjkashdas dkja shjdhask
askjdhaskjdhaskjdh ashdkjas hdkj ashdjk sakjd jash djahskjdhaskjhdjkashdas dkja shjdhask
askjdhaskjdhaskjdh ashdkjas hdkj ashdjk sakjd jash djahskjdhaskjhdjkashdas dkja shjdhask
askjdhaskjdhaskjdh ashdkjas hdkj ashdjk sakjd jash djahskjdhaskjhdjkashdas dkja shjdhask
askjdhaskjdhaskjdh ashdkjas hdkj ashdjk sakjd jash djahskjdhaskjhdjkashdas dkja shjdhask
askjdhaskjdhaskjdh ashdkjas hdkj ashdjk sakjd jash djahskjdhaskjhdjkashdas dkja shjdhask
askjdhaskjdhaskjdh ashdkjas hdkj ashdjk sakjd jash djahskjdhaskjhdjkashdas dkja shjdhask
askjdhaskjdhaskjdh ashdkjas hdkj ashdjk sakjd jash djahskjdhaskjhdjkashdas dkja shjdhask
askjdhaskjdhaskjdh ashdkjas hdkj ashdjk sakjd jash djahskjdhaskjhdjkashdas dkja shjdhask
askjdhaskjdhaskjdh ashdkjas hdkj ashdjk sakjd jash djahskjdhaskjhdjkashdas dkja shjdhask
askjdhaskjdhaskjdh ashdkjas hdkj ashdjk sakjd jash djahskjdhaskjhdjkashdas dkja shjdhask
ESSSEEEEEEEEEEEEEEEE
</div>
""",
            "score": 1177
        }
    ]

    def _run_test_id(self, test_id):
        nf = NodeFinder(NodeFinderTests._payload[test_id]["in"])
        self.assertEqual(nf.run(), NodeFinderTests._payload[test_id]["out"].strip())
        if not NodeFinderTests._payload[test_id]["score"] is None:
            self.assertEqual(nf.max_scored_node[1], NodeFinderTests._payload[test_id]["score"])

    def test_1(self):
        self._run_test_id(0)
