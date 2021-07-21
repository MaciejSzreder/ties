import re
import sys

try:
    from lxml import etree

    def findall(node,path):
        #try:
            return node.xpath(path)
        #except:
            return node.findall(path)

except:
    import xml.etree.ElementTree as etree

    def findall(node,path):
        return node.findall(path)


def calc_gaps(data,first_path,first_reg_exp,second_path,second_reg_exp,results,reverse):
    count=1
    first_reg_exp=re.compile(first_reg_exp)
    second_reg_exp=re.compile(second_reg_exp)
    first_list=findall(data,first_path)
    second_list=findall(data,second_path)
    if(reverse):
        first_list.reverse()
        second_list.reverse()
    for first_node,second_node in zip(first_list,second_list):
        if(etree.iselement(first_node)):
           first_text=etree.tostring(first_node).decode()
        elif(isinstance(first_node,str)):
           first_text=first_node
        if(etree.iselement(second_node)):
           second_text=etree.tostring(second_node).decode()
        elif(isinstance(second_node,str)):
           second_text=second_node
        first_match=first_reg_exp.search(first_text)
        if not first_match:
            sys.stderr.write("There is no '"+first_reg_exp.pattern+"' in '"+first_text+"'.\n")
            continue
        second_match=second_reg_exp.search(second_text)
        if not second_match:
            sys.stderr.write("There is no "+second_reg_exp.pattern+" in "+second_text+".\n")
            continue
        first=int(first_match.group())
        second=int(second_match.group())
        #print(winer,loser)
        if second==first:
            results.write(str(count)+'\n')
            count=1
        else:
            count+=1
