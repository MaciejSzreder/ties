#PATH_DATA="data.htm"
#PATH_RESOULT="result.csv"

#PATH_FIRST=".//*[@class='fin']"
#PATH_SECOND=".//*[@class='fin']"
#EXPR_FIRST='\d+'
#EXPR_SECOND='(?<=:)\d+'

#-p1 ".//*[@class='fin']" -r1 "\d+" -p2 ".//*[@class='fin']" -r2 "(?<=:)\d+"

PATH_DATA="data.htm"
PATH_RESOULT="result.csv"

PATH_FIRST=".//*[@class='event__scores fontBold']/span[1]"
PATH_SECOND=".//*[@class='event__scores fontBold']/span[2]"
EXPR_FIRST='\d+'
EXPR_SECOND='\d+'

import xml.etree.ElementTree as ET
from html.parser import HTMLParser
import re
import sys
import argparse

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
        pass #print("<", tag,'>')

    def handle_endtag(self, tag):
        self.tree.end(tag)
        pass #print("</", tag,'>')
        
    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_data(self, data):
        self.tree.data(data)
        pass #rint(data)

    def getRoot(self):
        return self.tree.close()

#get command line arguments
argparser=argparse.ArgumentParser(description="This program load data of match results form source file (in html syntax) and create file (csv) with distance between ties")
argparser.add_argument(
    "--source","--src","-in",
    dest="source",
    default=PATH_DATA,
    help="Path to file with data. File have to be html structure."
)
argparser.add_argument(
    "--result","--rzt","-out",
    dest="result",
    default=PATH_RESOULT,
    help="Path to file with data. File have to be html structure."
)
argparser.add_argument(
    "--path1","-p1",
    dest="path1",
    default=PATH_FIRST,
    help="XPath to the element containing text with first data"
)
argparser.add_argument(
    "--path2","-p2",
    dest="path2",
    default=PATH_SECOND,
    help="XPath to the element containing text with second data"
)
argparser.add_argument(
    "--regexp1","-r1",
    dest="exp1",
    default=EXPR_FIRST,
    help="Pattern of first data in text."
)
argparser.add_argument(
    "--regexp2","-r2",
    dest="exp2",
    default=EXPR_SECOND,
    help="Pattern of second data in text."
)
args=argparser.parse_args()

dataPath=args.source;
outDataPath=args.result;

firstPath=args.path1
secondPath=args.path2
firstRegExp=args.exp1
secondRegExp=args.exp2

#load data
HTMLFile = open(dataPath, "r",encoding='utf-8')
data = HTMLFile.read()
parser = HTML2XML()
parser.feed(data)
root=parser.getRoot()

#calculate and write resoults
count=1
firstRegExp=re.compile(firstRegExp)
secondRegExp=re.compile(secondRegExp)
resuts=open(outDataPath,'a')
for firstNode,secondNode in zip(root.findall(firstPath),root.findall(secondPath)):
    firstText=firstNode.text;
    secondText=secondNode.text;
    firstMatch=firstRegExp.search(firstText)
    if not firstMatch:
        sys.stderr.write("There is no '"+firstRegExp.pattern+"' in '"+firstText+"'.\n")
        continue
    secondMatch=secondRegExp.search(secondText)
    if not secondMatch:
        sys.stderr.write("There is no "+secondRegExp.pattern+" in "+secondText+".\n")
        continue
    first=int(firstMatch.group())
    second=int(secondMatch.group())
    #print(winer,loser)
    if second==first:
        resuts.write(str(count)+'\n')
        count=1
    else:
        count+=1
resuts.close()