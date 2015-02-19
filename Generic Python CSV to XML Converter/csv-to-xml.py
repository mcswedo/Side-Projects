"""
csv-to-xml.py - SIMPLE CSV TO XML CONVERTER
BY: MICHAEL SWEDO

STEPS FOR USE:
    1. Format your csv file with the first row containing all the "tags" for 
       the properties, and subsequent rows containing all the data.
    2. Place csv file to convert in the same folder as this file.
    3. Run this script. 
    4. In the section marked "FILL IN," add any prompts for xml header properties.
"""

import csv, os

# Get this file's directory to find the csv and create the xml file.
path = os.path.dirname(os.path.realpath(__file__)) + "/"

# Prompt for file name. Catch invalid filenames as IOErrors and valid ones as AttributeErrors.
# IOErrors will come with a failed open, Attribute Errors as a failed close - csv files are 
# non-unicode and cannot be closed in this fashion.
nameSet = False
while not nameSet:
    filename = raw_input("Enter file name (WITHOUT EXTENSION): ")
    csvFile = path + filename + ".csv"
    try: 
        open(csvFile)
        csvFile.close()
        break
    except IOError:
        print "Invalid filename. Please try again."
    except AttributeError:
        nameSet = True
       
# Create xml file path. 
xmlFile = path + filename + ".xml"

# Exception-catching method of opening the csv file to safely be able to close it even if program exits unexpectedly.
with open(csvFile) as openCSV:
	csvData = csv.reader(openCSV)
	xmlData = open(xmlFile, 'w')

	# Write required xml.
	xmlData.write('<?xml version="1.0" encoding="utf-8"?>' + "\n")
	xmlData.write("<Root>" + "\n")
	xmlData.write("  " + "<Head>" + "\n")

	"""
	
	FILL IN WITH HEADER PROPERTIES
	
	"""
	
	xmlData.write("  " + "</Head>" + "\n")
	xmlData.write("  " + "<Body>" + "\n")

	# Begin data conversion using each row of the csv file.
	rowNum = 0
	for row in csvData:
		# first row in the csv file will always be the tags.
		if rowNum is 0:
			# so establish a list of all the tags for use in the body.
			tags = row
		else:
			# Write each note and each note's properties.
			xmlData.write("    " + "<Note>" + "\n")
			for i in range(len(tags)):
				xmlData.write("      " + "<" + tags[i] + ">" + row[i] + "</" + tags[i] + ">" + "\n")
			
			# close the current note.
			xmlData.write("    " + "</Note>" + "\n")
		# move on to the next note.
		rowNum += 1
	   
	# Finish required xml and close the xml file.
	xmlData.write("  " + "</Body>" + "\n")
	xmlData.write("</Root>" + "\n")
	xmlData.close()
