# Ties
Simple program counting matchs between ties.
## Table of Contents
[About](#about)<br>
[Technologies](#technologies)<br>
[Setup](#setup)<br>
[Features](#features)

## About
My friends asked me about this script. They hope it could bring them the rich. I wish them it.

This project aims is to take a file with scores and count numbers of matches between ties and write results to an excel acceptable file.

## Technologies
The project was created in **Visual Studio 2019**.\
The language of code is **Python 3.7**.\
This program can use **lxml** library for HTML parsing and extending XPath compatibility, but it is not required.

## Setup
The code files are in folder _ties_. The main file is _ties.py_, but it requires file _default.py_ and content of folder _scripts_.
To run the program, type in the command line:
```shell
python ties.py
```
### unpack.py
If you do not need project VS project and git files, you can delete them manually or use _unpack.bat_:
* for Windows
```shell
unpack.bat
```
* for Linux(bash required)
```shell
bash unpack.bat
```
_unpack.py_ is batch and bash polyglot.\
You can run it safe from different places, you do not need to be at the same folder what script, but you should not use ```source``` or ```.```to run this script.\
When _unpack.bat_ finishes its job, it shows remained files. The show shape depends on the command accessible in OS. Currently important files are:
```
 📂ties
 ├📂scripts
 │├📜arguments.py
 │├📜calculations.py
 │└📜HTMLtoXML.py
 ├📜ties.py
 └📜default.py
```
### ties.py file
If you want to see usage, type:
```shell
python ties.py -h
```
The default files are data.html for input and result.csv for output. To change them use --source, --src, or -in for input data and --results, --rzt, or -out for output.
```shell
python ties.py -in soccer.html -out soccer.csv
```
To service other formats of HTML files you should specify the path to scores of both sides. To specify elements containing text with score use --path1 or -p1 for the first side and --path2 or -p2 for another. The path should be XPath. Python standard library has poor support for it. To expand support, install the lxml library.
E.g.
```shell
python ties.py -p1 ".//*[@class='game']/*[@class='score'][3]" -p2 ".//*[@class='game']/*[@class='score'][4]"
```
can be used for file:
```html
<!doctype html>
<html lang=en>
	<head>
		<meta charset=utf-8>
		<title>blah</title>
	</head>
	<body>
		<table>
			<tr class='game'>
				<td class="team">
					first
				</td>
				<td class="team">
					second
				</td>
				<td class="score">
					2
				</td>
				<td class="score">
					2
				</td>
			</tr>
			<tr class='game'>
				<td class="team">
					first
				</td>
				<td class="team">
					thrid
				</td>
				<td class="score">
					2
				</td>
				<td class="score">
					1
				</td>
			</tr>
			<tr class='game'>
				<td class="team">
					first
				</td>
				<td class="team">
					fourth
				</td>
				<td class="score">
					2
				</td>
				<td class="score">
					2
				</td>
			</tr>
		</table>
	</body>
</html>
```
If the node with a score is more text than just a number you can use --regexp1, -r1, --regexp2, -r2 to specify the shape of data.
E.g.
```shell
python ties.py -p1 ".//*[@class='game']/*[@class='team'][1]" -p2 ".//*[@class='game']/*[@class='team'][2]" -r1 "(?<=\()\d+" -r2 "(?<=\()\d+"
```
```html
<!doctype html>
<html lang=en>
	<head>
		<meta charset=utf-8>
		<title>blah</title>
	</head>
	<body>
		<table>
			<tr>
				<th>
					host (score)
				</th>
				<th>
					guest (score)
				</th>
			</tr>
			<tr class='game'>
				<td class="team">
					first1 (2)
				</td>
				<td class="team">
					second2 (2)
				</td>
			</tr>
			<tr class='game'>
				<td class="team">
					first1 (2)
				</td>
				<td class="team">
					thrid3 (1)
				</td>
			</tr>
			<tr class='game'>
				<td class="team">
					first1 (2)
				</td>
				<td class="team">
					fourth1 (2)
				</td>
			</tr>
		</table>
	</body>
</html>
```
You can deal even with scores for both teams in one element
```shell
python ties.py -p1 ".//*[@class='scores']" -r1 "\d+" -p2 ".//*[@class='scores']" -r2 "(?<=:)\d+"
```
can be used for file:
```html
<!doctype html>
<html lang=en>
	<head>
		<meta charset=utf-8>
		<title>games</title>
	</head>
	<body>
		<table>
			<tr>
				<th>
					host
				</th>
				<th>
					guest
				</th>
				<th>
					scores
				</th>
			</tr>
			<tr class='game'>
				<td class="team">
					first
				</td>
				<td class="team">
					second
				</td>
				<td class="scores">
					2:2
				</td>
			</tr>
			<tr class='game'>
				<td class="team">
					first
				</td>
				<td class="team">
					thrid
				</td>
				<td class="scores">
					2:1
				</td>
			</tr>
			<tr class='game'>
				<td class="team">
					first
				</td>
				<td class="team">
					fourth
				</td>
				<td class="scores">
					2:2
				</td>
			</tr>
		</table>
	</body>
</html>
```

### default.py file
default.py contains default parameter, so if you do not write -p1, -p2, ... the ties.py takes values from here. Be careful about this content because until now it is an executable file and it is not injection resistant so be careful by untrusted code pasted here.
If you want to change some default value, do not edit a single line but copy the line, put # at begin of the original line, and edit copy.
The following table shows which constant response to which parameter.
|parameter|default.py|
|---------|----------|
|-p1<br>--path1|PATH_FIRST|
|-p2<br>--path2|PATH_SECOND|
|-r1<br>--regexp1|EXPR_FIRST|
|-r2<br>--regexp2|EXPR_SECOND|
|-in<br>--src<br>--source|PATH_DATA|
|-out<br>--rzt<br>--result|PATH_RESULT|
## Features
* count distant between ites
* suport for any shape HTML file

To Do:
* support for XML file
* support for MS Excel file format
