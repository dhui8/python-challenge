# Specify the file to read from
# Author : David Hui
# Date : 12/1/2017

location = input ("Enter the folder name (including the full path) of the source file : ")
fileName = input ( "\nEnter the file name : ")

sourceFilePath = location + str("/") + fileName
file = open(sourceFilePath,"r")

wordCount = 0
sentenceCount = 0
letterCount = 0
avgSentenceLength = 0

for word in file.read().split():
	wordCount += 1
	if str(word[len(word)-1]) == '.' :
		sentenceCount += 1
	for char in word :
		if char != ',' and char != '-' and char != '(' and char != ')': 
			letterCount += 1
		
print ("Approximate Word Count = " + str(wordCount))
print ("Approximate Setence Count = " + str(sentenceCount))
print ("Average Letter Count = " + str(letterCount/wordCount))
print ("Average Sentence Length = " + str(wordCount/sentenceCount))

file.close()
