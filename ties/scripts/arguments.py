import argparse

import default

#get command line arguments
argparser=argparse.ArgumentParser(description="This program load data of match results form source file (in html syntax) and create file (csv) with distance between ties.")
argparser.add_argument(
    "--source","--src","-in",
    dest="source",
    default=default.PATH_DATA,
    help="Path to file with data. File have to have html format."
)
argparser.add_argument(
    "--result","--rzt","-out",
    dest="result",
    default=default.PATH_RESULT,
    help="Path to file to append result. File will have csv format."
)
argparser.add_argument(
    "--path1","-p1",
    dest="path1",
    default=default.PATH_FIRST,
    help="XPath to the element containing text with first team scores."
)
argparser.add_argument(
    "--path2","-p2",
    dest="path2",
    default=default.PATH_SECOND,
    help="XPath to the element containing text with first team scores."
)
argparser.add_argument(
    "--regexp1","-r1",
    dest="exp1",
    default=default.EXPR_FIRST,
    help="Regular expression showing shape and position of first team scores."
)
argparser.add_argument(
    "--regexp2","-r2",
    dest="exp2",
    default=default.EXPR_SECOND,
    help="Regular expression showing shape and position of second team scores."
)
argparser.add_argument(
    "--direction","-d",
    dest="direction",
    default=default.DIRECTION,
    choices=["forward","backward"],
    help="Determine direction of writing a result. Accepts only two values: 'forward' (default) or 'backward'."
)
args=argparser.parse_args()
