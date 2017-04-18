import xml.etree.ElementTree as ET

##tree = ET.parse('pubs.txt')
##root = tree.getroot()
f = open("pubs.txt", "r") # reads file

def checkauthor(line): #function for splitting for authors
	linetemp = line.split('<author>')
	if len(linetemp) == 2:
		print "Checked!"
		return 1
#print(f.readline()) reads <pub>
#print(f.readline()) reads <id>

id = "NULL"
idtemp = "NULL"
title = "NULL"
year = "NULL"
booktitle = "NULL"
pages = "NULL"
author = "NULL"


if f.readline() == "<pub>\n":
	idtemp = f.readline() # this will contain the whole next line, which will be manipulated to remove the ID brackets
#	print idtemp  # <ID>0</ID>
	righttempid = idtemp.split('<ID>')[1]
#	print righttempid #0</ID>
	ID = righttempid.split('</ID>')[0]
	print ID # <0>

	titletemp = f.readline()
#	print titletemp #<title>Regression Time Warping for Similarity Measure...</title>
	righttitletemp = titletemp.split('<title>')[1]
#	print righttitletemp # Regression Time Warping...</title>
	title = righttitletemp.split('</title>')[0]
	print title #Regression Time Warping for Similarity Measure of Sequence

	yeartemp = f.readline() 
#	print yeartemp
	rightyeartemp = yeartemp.split('<year>')[1]
	year = rightyeartemp.split('</year>')[0]
	print year # 2004

	booktitletemp = f.readline()
	rightbooktitletemp = booktitletemp.split('<booktitle>')[1]
	booktitle = rightbooktitletemp.split('</booktitle>')[0]
	print booktitle

	pagestemp = f.readline()
	rightpagestemp = pagestemp.split('<pages>')[1]
	pages = rightpagestemp.split('</pages>')[0]
	print pages

	if f.readline() != "</authors>\n": # looks for the end of all authors
		authortemp = f.readline()
		if checkauthor(authortemp):
			rightauthortemp = authortemp.split('<author>')[1]
			print rightauthortemp
			
			author = rightauthortemp.split('</author>')[0]
			print author
			# if f.readline() == "<author>\n":
			# 	exit()








