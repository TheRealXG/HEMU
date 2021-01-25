import os
import sys
import argparse
from random import seed
from random import randint

seed(1)

# define your test params
numRandTests = 1
testsRun = 0
maxFailedTestsAllowed = 1;
addedIntegerMax = 9
addedIntegerMin = 0
expScriptName = "calc"
logDir = "logs"
logName = "calc_expect"
logExt = ".log"
passMessage = "Test Pass"
failMessage = "Test Fail"

# initialize vars
firstInt = 0
secondInt = 0
failure = 1
failureList = []
resultsList = []
numTestsPassed = 0
numTestsFailed = 0
resultsLine = ""

def main():
	inputFile = False
	inputFileName = ""
	
	# check for input file
	if len(sys.argv) > 1:
		inputFile = True
		inputFileName = sys.argv[1]
		if not os.path.exists(inputFileName):
			print("Input file not found. Generating random values.\n")
			inputFile = False

	# use input file if given, random if not given
	if inputFile:
		runInputTests(inputFileName)
	else:
		runRandTests()
		
	aggregateResults()
	outputResults()	
	
	if (numTestsFailed > maxFailedTestsAllowed):
		sys.exit(1)
	else:
		sys.exit(0)
    

# run the tests in expect scripts with input file
def runInputTests(inputFileName):
	global testsRun
	testCtr = 0
	
	with open(inputFileName) as inputFile:
			for line in inputFile:
				inputs = line.split()
				print (inputs)
				if (len(inputs) != 4):
					print("Line " + str(testCtr + 1) + " of the input file is incorrectly formatted. Skipping.")
					continue
					
				firstInt = inputs[0]
				secondInt = inputs[1]
				total = inputs[2]
				 
				if inputs[3].lower() == 'p':
					failure = 1
				else:
					failure = 2
				failureList.append(failure)
				
				os.system("./" + expScriptName + ".exp " + str(firstInt) + " " + str(secondInt) + " " + str(total * failure) + " " + str(testCtr))
				
				testCtr += 1
				
	testsRun = testCtr

    
# run the tests in expect scripts with random inputs
def runRandTests():
	global testsRun
	
	for i in range(numRandTests):
		if randint(1,10) >= 5:
			failure = 2
		else:
			failure = 1
		failureList.append(failure)
		firstInt = randint(addedIntegerMin, addedIntegerMax)
		secondInt = randint(addedIntegerMin, addedIntegerMax)
		os.system("./" + expScriptName + ".exp " + str(firstInt) + " " + str(secondInt) + " " + str((firstInt + secondInt) * failure) + " " + str(i))
	
	testsRun = numRandTests


# check test output
def aggregateResults():
	global numTestsPassed
	global numTestsFailed
	
	for i in range(testsRun):
		# get last line of the log which has the pass/fail message
		with open(logDir + "/" + logName + str(i) + logExt) as logFile:
			for line in logFile:
				pass
			resultsLine = line.strip()
			# increment pass fail counters based on last line
			if (failureList[i] == 1 and resultsLine == passMessage):
				numTestsPassed += 1;
				resultsList.append("Test " + str(i) + ": Passed")
			if (failureList[i] == 1 and resultsLine != passMessage):
				numTestsFailed += 1;
				resultsList.append("Test " + str(i) + ": Failed")
			if (failureList[i] == 2 and resultsLine == failMessage):
				numTestsPassed += 1;
				resultsList.append("Test " + str(i) + ": Passed")
			if (failureList[i] == 2 and resultsLine != failMessage):
				numTestsFailed += 1;
				resultsList.append("Test " + str(i) + ": Failed")
				
				
# output results				
def outputResults():
	resultFile = open("results.txt", "w")
	resultFile.write("***********\n")
	resultFile.write("Total Tests\n")
	resultFile.write("***********\n")
	resultFile.write("Passed: " + str(numTestsPassed) + "\n")
	resultFile.write("Failed: " + str(numTestsFailed) + "\n\n")
	resultFile.write("****************\n")
	resultFile.write("Individual Tests\n")
	resultFile.write("****************\n")

	for i in range (len(resultsList)):
		resultFile.write(resultsList[i] + "\n")
	resultFile.close()
	
	
if __name__ == "__main__":
    main()	
