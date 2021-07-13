# ties
Simple program counting matchs between ties.
## Table of Contents

## General info
The aim of the project is 

## Technologies
The project was created in Visual Studio 2019.
Language of a code is Python 3.7.
This program can use lxml liblary for HTML parsing and extending XPath compability, but it is not required.

## Setup
The code files are in folder "ties". The main file is "ties.py", but it require file "default.py" and content of folder scripts.
To run the program type in command line:
```shell
python ties.py
```
If you want to see usage type:
```shell
python ties.py -h
```
The default files are data.html for input and result.csv for output. To change them use --source, --src or -in for input data and --resoult, --rzt or -out for output.
```shell
python ties.py -in soccer.html -out soccer.csv
```
To service different format of HTML file you should specify the path to scores of both sides. To specify element containing text with score use --path1 or -p1 for
first side and --path2 or -p2 for second. The path should be XPath. Python standard liblary have poor suport for it, to expand support instal lxml liblary.
```shell
python ties.py -p1 "[@class='game']/[@class='score'][1]" -p2 "[@class='game']/[@class='score'][2]" 
```
If the node with score is more text than just a number you can use --regexp1, -r1, --regexp2, -r2 to specyfi the shape of data.
```shell
python ties.py -p1 "[@class='scores']" -r1 "\d+" -p2 "[@class='scores']" -r2 "(?<=:)\d+"
```

## Features
* count distant between ites
* suport for any shape HTML file
To Do:
* support for XML file
* support for MS Excel file format
