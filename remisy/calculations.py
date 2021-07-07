import xml.etree.ElementTree as ET
import re
import sys

def calc_gaps(data,first_path,first_reg_exp,second_path,second_reg_exp,results,reverse):
    count=1
    first_reg_exp=re.compile(first_reg_exp)
    second_reg_exp=re.compile(second_reg_exp)
    first_list=data.findall(first_path)
    second_list=data.findall(second_path)
    if(reverse):
        first_list.reverse()
        second_list.reverse()
    for first_node,second_node in zip(first_list,second_list):
        first_text=first_node.text;
        second_text=second_node.text;
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
