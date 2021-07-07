#PATH_DATA="data.htm"
#PATH_RESOULT="result.csv"

#PATH_FIRST=".//*[@class='fin']"
#PATH_SECOND=".//*[@class='fin']"
#EXPR_FIRST='\d+'
#EXPR_SECOND='(?<=:)\d+'

#-p1 ".//*[@class='fin']" -r1 "\d+" -p2 ".//*[@class='fin']" -r2 "(?<=:)\d+"





from  HTMLtoXML import HTML2XML
from arguments import args
from calculations import calc_gaps

#load data
HTMLFile = open(args.source, "r",encoding='utf-8')
data = HTMLFile.read()
parser = HTML2XML()
parser.feed(data)
root=parser.getRoot()


results=open(args.result,'a')
calc_gaps(root,args.path1,args.exp1,args.path2,args.exp2,results)
results.close()

#calculate and write resoults