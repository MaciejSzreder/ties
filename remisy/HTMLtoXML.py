from html.parser import HTMLParser
import xml.etree.ElementTree as ET

#read htms as xml
class HTML2XML(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tree=ET.TreeBuilder()

    def handle_starttag(self, tag, attrs):
        dic={}
        for id,val in attrs:
            dic[id]=val
        self.tree.start(tag,dic)

    def handle_endtag(self, tag):
        self.tree.end(tag)
        
    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_data(self, data):
        self.tree.data(data)

    def getRoot(self):
        return self.tree.close()
