#PATH_DATA="data.htm"
#PATH_RESOULT="result.csv"

#PATH_FIRST=".//*[@class='fin']"
#PATH_SECOND=".//*[@class='fin']"
#EXPR_FIRST='\d+'
#EXPR_SECOND='(?<=:)\d+'

#-p1 ".//*[@class='fin']" -r1 "\d+" -p2 ".//*[@class='fin']" -r2 "(?<=:)\d+"



import xml.etree.ElementTree as ET
import re
import sys


from  HTMLtoXML import HTML2XML

from arguments import args

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