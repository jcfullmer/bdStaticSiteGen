from textnode import *


test = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")

print(test.__repr__())