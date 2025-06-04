import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(props={"href": "https://google.com", "target": "_blank"})

        result = node.props_to_html()
        print(result)
        assert result == ' href="https://google.com" target="_blank"'


if __name__ == "__main__":
    unittest.main()