#PATH_DATA="data.html"
#PATH_RESOULT="result.csv"

#PATH_FIRST=".//*[@class='fin']"
#PATH_SECOND=".//*[@class='fin']"
#EXPR_FIRST='\d+'
#EXPR_SECOND='(?<=:)\d+'

#-p1 ".//*[@class='fin']" -r1 "\d+" -p2 ".//*[@class='fin']" -r2 "(?<=:)\d+"





from scripts.HTMLtoXML import HTML2XML
from scripts.arguments import args
from scripts.calculations import calc_gaps

#load data
HTMLFile = open(args.source, "r",encoding='utf-8')
data = HTMLFile.read()
parser = HTML2XML()
parser.feed(data)
root=parser.get_root()


results=open(args.result,'a')
calc_gaps(root,args.path1,args.exp1,args.path2,args.exp2,results,args.direction=="backward")
results.close()

#calculate and write resoults