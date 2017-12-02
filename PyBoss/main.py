# Author : David Hui
# Date : 12/1/2017


import os
import csv
# Specify the file to read from

# Dictionary for US States
states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

location = input ("Enter the folder name (including the full path) of the source file : ")
fileName = input ( "\nEnter the file name : ")

outputLocation = input ( "\nEnter the name of output folder (including the full path) : ")

outputFileName = input ("\nEnter the name of the output file : ")

while (outputFileName == fileName):
	outputFileName = input ( "\nCan not use the same file name . Please enter a different output file name : ")
	

read_path = os.path.join(location, fileName)

outputFilePath = outputLocation + str("/") + outputFileName
f = open(outputFilePath,"w")


# Open the file using "read" mode. Specify the variable to hold the contents
with open(read_path, "r", newline='') as csvfile:

    # Initialize csv.writer
	csvreader = csv.reader(csvfile, delimiter=',')
	
	# print(states)
	
	for row in csvreader:
		
		if row[0] != "Emp ID":
			FN,LN = row[1].split(" ")
			A,B,C =  row[3].split("-")
			maskedSSN = "***-**-" + str(C)
			DOBYear, DOBMon, DOBDay = row[2].split("-")
			DOB = DOBMon + "/" + DOBDay + "/" + DOBYear
			for key, keyValue in states.items():
				
				if row[4] == keyValue:
					st = key
					
					#print(str(row[0]) + "," + FN + "," + LN + "," + DOB + "," + maskedSSN + "," + row[4] + "=" + st) 	

					
			f.write(str(row[0]) + "," + FN + "," + LN + "," + DOB + "," + maskedSSN + "," + st + "\n") 
		else:
			f.write("Emp ID,First Name,Last Name,DOB,SSN,State\n")
f.close()
