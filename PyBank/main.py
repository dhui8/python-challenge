
# Author : David Hui
# Date : 12/1/2017

import os
import csv
# Specify the file to read from


location = input ("Enter the folder name (including the full path) of the source file : ")
fileName = input ( "\nEnter the file name : ")

outputLocation = input ( "\nEnter the name of output folder (including the full path) : ")

outputFileName = input ("\nEnter the name of the output file : ")

while (outputFileName == fileName):
	outputFileName = input ( "\nCan not use the same file name . Please enter a different output file name : ")
	

read_path = os.path.join(location, fileName)

# Open the file using "read" mode. Specify the variable to hold the contents
with open(read_path, "r", newline='') as csvfile:

    # Initialize csv.writer and variables
	csvreader = csv.reader(csvfile, delimiter=',')
	
	monthCount = 0
	totalRev = 0
	GreatestIncrease = 0
	GreatestDecrease = 0
	GreatestIncMonth =  ""
	GreatestDecMonth = ""
	
	revenueList=[]
	totalReveneueChange = 0
	
	# Read The source file
	for row in csvreader:
		
		if row[0] != "Date":  # Skips the header
		
			monthCount += 1
			totalRev += int(row[1])
			revenueList.append(int(row[1]))
			
			# Compare the Greatest Increase with the current record
			if GreatestIncrease < int(row[1]):
				GreatestIncrease = int(row[1])
				GreatestIncMonth = row[0]
				
			#	Compare the Greatest Decrease with the current record
			if GreatestDecrease > int(row[1]):
				GreatestDecrease = int(row[1])
				GreatestDecMonth = row[0]
			
	dataPointCnt = 0
	
	# Builds Revenue list
	for idx in revenueList:
		
		if monthCount > int(revenueList.index(idx)+1):
			totalReveneueChange += (int(revenueList[revenueList.index(idx)+1]) - int(idx))
			dataPointCnt += 1
			
	
	print("\nTotal Months: " + str(monthCount))
	print("Total Revenue: " + str(totalRev))
	print("Average Revenue Change: " + str(round(float(totalReveneueChange/dataPointCnt),2)))
	print("Greatest Increase in  Revenue: " + GreatestIncMonth + " (" + str(GreatestIncrease)+str(")"))
	print("Greatest Decrease in  Revenue: " + GreatestDecMonth + " (" + str(GreatestDecrease)+str(")"))
	
	
outputFilePath = outputLocation + str("/") + outputFileName
f = open(outputFilePath,"w")

f.write("\nTotal Months: " + str(monthCount))
f.write("\nTotal Revenue: " + str(totalRev))
f.write("\nAverage Revenue Change: " + str(round(float(totalReveneueChange/dataPointCnt),2)))
f.write("\nGreatest Increase in  Revenue: " + GreatestIncMonth + " (" + str(GreatestIncrease)+str(")"))
f.write("\nGreatest Decrease in  Revenue: " + GreatestDecMonth + " (" + str(GreatestDecrease)+str(")"))

f.close()
