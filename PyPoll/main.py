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
	
	totalCastCnt = 0
	candidatesList = {}  # dictionary
	percentageVote = 0
	totalVoteCnt = 0
	winner =  ""
	
	
	for row in csvreader:
		
		if row[0] != "Voter ID":  # skips header
		
			totalCastCnt += 1
			if row[2] not in candidatesList:
				candidatesList[row[2]] = 1
			else:
				candidatesList[row[2]] = candidatesList[row[2]] + 1
	

	print("Election Results")
	print("--------------------------")
	print("Total Votes : " + str(totalCastCnt))
	print("--------------------------")
	for candidate, voteCnt in candidatesList.items() :
		print(candidate + ": " + str((voteCnt/ totalCastCnt)*100) + " %")
		
	print("--------------------------")
	
	maxval = max(candidatesList.values())
	v = list(candidatesList.values())
	k = list(candidatesList.keys())
	Winner = [k for k,v in candidatesList.items() if v==maxval]
	
	print("Winner : " + " ".join(Winner))
	print("--------------------------")

outputFilePath = outputLocation + str("/") + outputFileName
f = open(outputFilePath,"w")

f.write("Election Results")
f.write("\n--------------------------")
f.write("\nTotal Votes : " + str(totalCastCnt))
f.write("\n--------------------------")
for candidate, voteCnt in candidatesList.items() :
	f.write("\n" + candidate + ": " + str((voteCnt/ totalCastCnt)*100) + " %")
	
f.write("\n--------------------------")

maxval = max(candidatesList.values())
v = list(candidatesList.values())
k = list(candidatesList.keys())
Winner = [k for k,v in candidatesList.items() if v==maxval]

f.write("\nWinner : " + " ".join(Winner))
f.write("\n--------------------------")

f.close()
