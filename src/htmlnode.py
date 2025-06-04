

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        listy = list()
        if self.props is None:
            return ""
        else:
            for k, v in self.props.items():
                listy.append(f'{k}="{v}"')
            return f' {" ".join(listy)}'
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
    
