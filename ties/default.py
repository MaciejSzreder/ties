# If you want to change the default behaviour, duplicate line, cloned line ahead the '#' sign, modify value of the oryginal line.
# Be careful this file is vulnreable for script injection, don't copy untrusted code nor value
PATH_DATA="data.htm"
PATH_RESOULT="result.csv"

PATH_FIRST=".//*[@class='event__scores fontBold']/span[1]"
PATH_SECOND=".//*[@class='event__scores fontBold']/span[2]"
EXPR_FIRST='\d+'
EXPR_SECOND='\d+'
