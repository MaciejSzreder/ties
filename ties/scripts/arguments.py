import argparse

import default

#get command line arguments
argparser=argparse.ArgumentParser(description="This program load data of match results form source file (in html syntax) and create file (csv) with distance between ties")
argparser.add_argument(
    "--source","--src","-in",
    dest="source",
    default=default.PATH_DATA,
    help="Path to file with data. File have to be html structure."
)
argparser.add_argument(
    "--result","--rzt","-out",
    dest="result",
    default=default.PATH_RESOULT,
    help="Path to file with data. File have to be html structure."
)
argparser.add_argument(
    "--path1","-p1",
    dest="path1",
    default=default.PATH_FIRST,
    help="XPath to the element containing text with first data"
)
argparser.add_argument(
    "--path2","-p2",
    dest="path2",
    default=default.PATH_SECOND,
    help="XPath to the element containing text with second data"
)
argparser.add_argument(
    "--regexp1","-r1",
    dest="exp1",
    default=default.EXPR_FIRST,
    help="Pattern of first data in text."
)
argparser.add_argument(
    "--regexp2","-r2",
    dest="exp2",
    default=default.EXPR_SECOND,
    help="Pattern of second data in text."
)
argparser.add_argument(
    "--direction","-d",
    dest="direction",
    default="forward",
    choices=["forward","backward"],
    help="Determine direction of writing a result. Accepts only two values: 'forward' (default) or 'backward'."
)
args=argparser.parse_args()