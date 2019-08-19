"""
pydom: 
    All dom logic is managed by this module.
    author: fgonza at gmail.com
"""

from htmldom import htmldom

class HtmlDocument:
    def __init__(self, htmlFile, selector=None):
        self.dom =  htmldom.HtmlDom("file:" + htmlFile).createDom()
        if selector != None:
            self.node = self.dom.find(selector)
        else:
            self.node = None

    def find(self, selector):
        node = self.dom.find(selector)
        return HtmlNode(node)

    def findBestMatch(self, origNode):
        nodes = self.dom.find(origNode.nodeName())
        bestMatch = {'node': None, 'count':0}
        for n in nodes:
            node = HtmlNode(n)
            matches = node.compare(origNode)
            if matches > bestMatch['count']:
                bestMatch['node'] = node
                bestMatch['count'] = matches

        return bestMatch['node']


class HtmlNode:
    def __init__(self, node):
        self.node = node


    def attr(self, name):
        if self.node:
            return self.attributes().get(name)
        else:
            return None

    def _isNodeList(self):
        return type(self.node) == htmldom.HtmlNodeList

    def _getNodeParent(self, node):
        if type(node) == htmldom.HtmlNodeList:
            return node.nodeList[0].parentNode
        else:
            return node.parentNode

    def _getNodeName(self, node):
        if type(node) == htmldom.HtmlNodeList:
            return node.nodeList[0].getName()
        else:
            return node.getName()

    def path(self):
        xpath = []
        if self.node:
            xpath.append(self._getNodeName(self.node))
            parent = self._getNodeParent(self.node)
            while parent:
                xpath.append(self._getNodeName(parent))
                parent = self._getNodeParent(parent)
        xpath.reverse()
        return ' > '.join(xpath)

    def compare(self, node):
        matches = 0
        if self.node:
            for attr in node.attributes():
                value = node.attr(attr)
                if attr in self.attributes() and value == self.attr(attr):
                    matches += 1

        return matches

    def attributes(self):
        if self.node:
            if self._isNodeList():
                return self.node.nodeList[0].attributes
            else:
                return self.node.attributes

        return {}

    def text(self):
        if self.node:
            if self._isNodeList:
                return self.node.nodeList[0].getText()
            else:
                return self.node.getText()
        else:
            return None

    def nodeName(self):
        return self._getNodeName(self.node)

    def html(self):
        if self.node:
            return self.node.html()
        else:
            return ''
