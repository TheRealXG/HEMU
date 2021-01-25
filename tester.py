import os
import sys 
from random import seed
from random import randint

seed(1)

# define your test params
numTests = 10
maxFailedTestsAllowed = 0;
addedIntegerMax = 99
addedIntegerMin = 1
logDir = "logs"
logName = "add_expect"
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

# run the tests in expect scripts
for i in range(numTests):
	if randint(1,10) >= 5:
		failure = 0
	else:
		failure = 1
	failureList.append(failure)	
	firstInt = randint(addedIntegerMin, addedIntegerMax)
	secondInt = randint(addedIntegerMin, addedIntegerMax)
	os.system("./add.exp " + str(firstInt) + " " + str(secondInt) + " " + str((firstInt + secondInt) * failure) + " " + str(i))

# check test output
for i in range(numTests):
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
    		if (failureList[i] == 0 and resultsLine == failMessage):
    			numTestsPassed += 1;
    			resultsList.append("Test " + str(i) + ": Passed")
    		if (failureList[i] == 0 and resultsLine != failMessage):
    			numTestsFailed += 1;
    			resultsList.append("Test " + str(i) + ": Failed")
    			
# output results
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

if (numTestsFailed > maxFailedTestsAllowed): 
	sys.exit(1)
else:
	sys.exit(0)

