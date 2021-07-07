import xml.etree.ElementTree as ET
import re
import sys

def calc_gaps(data,first_path,first_reg_exp,second_path,second_reg_exp,results):
    count=1
    first_reg_exp=re.compile(first_reg_exp)
    second_reg_exp=re.compile(second_reg_exp)
    for firstNode,secondNode in zip(data.findall(first_path),data.findall(second_path)):
        firstText=firstNode.text;
        secondText=secondNode.text;
        firstMatch=first_reg_exp.search(firstText)
        if not firstMatch:
            sys.stderr.write("There is no '"+first_reg_exp.pattern+"' in '"+firstText+"'.\n")
            continue
        secondMatch=second_reg_exp.search(secondText)
        if not secondMatch:
            sys.stderr.write("There is no "+second_reg_exp.pattern+" in "+secondText+".\n")
            continue
        first=int(firstMatch.group())
        second=int(secondMatch.group())
        #print(winer,loser)
        if second==first:
            results.write(str(count)+'\n')
            count=1
        else:
            count+=1
