# Summary: This program takes a CSV file with Jeopardy Information, and turns it
# into a Jeorpday-esque game. It prints the board, adds up your points, and does
# everything else a jeopardy game should have.
# author: Caleb Gee
# date:4/20/2023

import random

# Constants for the parts of a question

CATEGORY = 0
VALUE = 1
QUESTION = 2
ANSWER = 3

# Constant representing a used question

NO_QUESTION = "____"

#=======================================================================
#  _____  __ __  ____     __ ______  ____  ___   ____    _____
# |     ||  T  T|    \   /  ]      Tl    j/   \ |    \  / ___/
# |   __j|  |  ||  _  Y /  /|      | |  TY     Y|  _  Y(   \_ 
# |  l_  |  |  ||  |  |/  / l_j  l_j |  ||  O  ||  |  | \__  T
# |   _] |  :  ||  |  /   \_  |  |   |  ||     ||  |  | /  \ |
# |  T   l     ||  |  \     | |  |   j  ll     !|  |  | \    |
# l__j    \__,_jl__j__j\____j l__j  |____j\___/ l__j__j  \___j
#=======================================================================                                                            


# Splits a String containing all question information, then
# returns the specified part of the question
# Parameters
#   question - String containing comma separated quiz question details
#   whichInfo - constant representing which part of the question to return
#                should be one of CATEGORY, VALUE, QUESTION, ANSWER
# Return String containing the specified part of the question


def getInfo(quesInfo, whichInfo):
    
    question_list = quesInfo.split(",")
    
    if whichInfo == CATEGORY:
        
        if quesInfo == NO_QUESTION:
            return NO_QUESTION

        else:
            return question_list[CATEGORY]
        
    elif whichInfo == VALUE:
        
        if quesInfo == NO_QUESTION:
            return NO_QUESTION

        else:
            return question_list[VALUE]
        
    elif whichInfo == QUESTION:
        
        if quesInfo == NO_QUESTION:
            return NO_QUESTION
        
        else:
            return question_list[QUESTION]
        
    elif whichInfo == ANSWER:
        
        if quesInfo == NO_QUESTION:
            return NO_QUESTION

        else:
            return question_list[ANSWER]
    else:
        return NO_QUESTION
    
    return ""




# Reads a file and returns a list containing the lines in the file
# parameter: filename - name of CSV file to read
# return: list containing stripped lines of the file

def loadCSV(filename):
    outputList = []

    try:
        source = open(filename,"r", encoding="UTF-8")
        outputList = source.readlines()
        source.close()

    except FileNotFoundError:
        print("Unable to open input file: " + inputFile)


    for i in range(len(outputList)):
        outputList[i] = outputList[i].strip('\n')



    return outputList


# Takes a list containing every line from the question csv list
# Returns a new list containing only the categories
# parameter:  fileList - list containing lines of a CSV file containing quiz data
# return : list of strings containing exactly 3 unique categories of questions


def getCategoryList(fileList):

    categoryList = []
    length = len(fileList)
    statement = 0

    while statement < 3:

        category = getInfo(fileList[random.randint(0,length-1)],CATEGORY)

        if category in categoryList:
            pass
        else:
        
            categoryList.append(category)
            statement += 1

    return categoryList



# Takes a list containing every line from the question csv list
# Returns a new list containing only the questions whose category is in categoryList
# parameter:  fileList - list containing lines of a CSV file containing quiz data
#             categoryList - list containing categories from which to choose questions
# return : list of exactly 9 strings containing CSV formatted question info
#                  from only the categories contained in categoryList


def getQuestionList(fileList, categoryList):

    questionList = []
    
    length = len(fileList)
    
    for i in range(3):
        
        helpfulValue = 0

        while helpfulValue < 3:
            questionAdder = fileList[random.randint(0,length-1)]

            if categoryList[i] in questionAdder and questionAdder not in questionList:

                questionList.append(questionAdder)
                helpfulValue += 1

            else:
                pass
       
    return questionList

# Prints question board
# For example:
# Q0($100)  Q1($200)  Q2($400)
# Q3($200)  Q4($150)  Q5($600)
# Q6($200)  Q7($150)  Q8($600)
#
# parameter:  questionList - list of 9 CSV formatted questions
# return: none


def printBoard(questionList,categoryList):

    print("")
    print("PRINTING BOARD...")
    print("")
    
    printBoardList = []

    for i in range(9):
        boardQuestions = getInfo(questionList[i],VALUE)
        printBoardList.append(boardQuestions)

    print( categoryList[0] + "   " + categoryList[1] + "   " + categoryList[2] )
    print("============================================================")
    print ("")
    print("Q0 ($" + printBoardList[0] + ")   " + "Q3 ($" + printBoardList[3] + ")   " + "Q6 ($" + printBoardList[6] + ")   ")
    print("Q1 ($" + printBoardList[1] + ")   " + "Q4 ($" + printBoardList[4] + ")   " + "Q7 ($" + printBoardList[7] + ")   ")
    print("Q2 ($" + printBoardList[2] + ")   " + "Q5 ($" + printBoardList[5] + ")   " + "Q8 ($" + printBoardList[8] + ")   ")
    print("")
    print("============================================================")
    
    


# Checks question list for a valid question
# If every element is NO_QUESTION, return false
# If at least one element has text, return true
# parameter:  questionList - list of 9 CSV formatted questions
# return: true if at least one question is unused, false otherwise


def hasQuestions(questionList):

    if NO_QUESTION in questionList[0] and NO_QUESTION in questionList[1] and NO_QUESTION in questionList[2] and NO_QUESTION in questionList[3] and NO_QUESTION in questionList[4] and NO_QUESTION in questionList[5] and NO_QUESTION in questionList[6] and NO_QUESTION in questionList[7] and NO_QUESTION in questionList[8]: 
        return False
    else:
        return True


# Asks user which question he/she wants to answer
# parameter:  questionList - list of 9 CSV formatted questions
# return: a valid index into questionList


def getQuestionIndex(questionList):
    done = False
    while not done:
        try:
            selectedQuestion = int(input("Which question would you like to answer? "))
            
            if selectedQuestion < 0 or selectedQuestion > 8 or questionList[selectedQuestion] == NO_QUESTION: 
                print("You have either already answered that question, or asked for a question that doesn't exist.")
            else:
                done = True
        except ValueError:
            print("That didn't work. Try typing the question as a number.")
    return selectedQuestion




#===============================================================
#  ___ ___   ____  ____  ____          __   ___   ___      ___ 
# |   T   T /    Tl    j|    \        /  ] /   \ |   \    /  _]
# | _   _ |Y  o  | |  T |  _  Y      /  / Y     Y|    \  /  [_ 
# |  \_/  ||     | |  | |  |  |     /  /  |  O  ||  D  YY    _]
# |   |   ||  _  | |  | |  |  |    /   \_ |     ||     ||   [_ 
# |   |   ||  |  | j  l |  |  |    \     |l     !|     ||     T
# l___j___jl__j__j|____jl__j__j     \____j \___/ l_____jl_____j
#================================================================                                                             



# Constant for filename
QUESTION_FILENAME = "jeopardy.csv"

# READS FILE

fileList = loadCSV(QUESTION_FILENAME)

categoryList = getCategoryList(fileList)

questionList = getQuestionList(fileList,categoryList)

# START

print("")
print(" Welcome to...")
print("")
print("")
print("                                      __ ")
print("    __                       _       |  |")
print(" __|  |___ ___ ___ ___ ___ _| |_ _   |  |")
print("|  |  | -_| . | . | .'|  _| . | | |  |__|")
print("|_____|___|___|  _|__,|_| |___|_  |  |__|")
print("              |_|             |___|      ")
print("")
print("")


# PRINT CATEGORIES

print("The categories are " + categoryList[0] + ", " + categoryList[1] + ", and " + categoryList[2] + ".")

# IF SET FALSE, RUNS GAME OVER

keepGoing = True

currentWinnings = 0

while keepGoing == True:

    print("Your current winnings are $" + str(currentWinnings) + "!")

    # PRINTS BOARD (CHOSEN QUESTIONS ARE BLANK)

    printBoard(questionList,categoryList)

    questionNumber = getQuestionIndex(questionList)

    # STORED VALUES FOR PRINTING QUESTION

    questionAsked = getInfo(questionList[questionNumber],QUESTION)
    answer = getInfo(questionList[questionNumber],ANSWER)
    points = getInfo(questionList[questionNumber],VALUE)
    category = getInfo(questionList[questionNumber],CATEGORY)

    print("")

    # ASKS QUESTION
    
    rightOrWrong = input(category + ": " + questionAsked + " ")

    # RIGHT ANSWER ADDS POINTS

    if rightOrWrong == answer:
        currentWinnings += int(points)
        print("That is correct. You earn " + str(points) + " points. That puts you at a score of " + str(currentWinnings) + "."   )
        questionList[questionNumber] = NO_QUESTION
        keepGoing = hasQuestions(questionList)

    # WRONG ANSWER DOES NOTHING
    
    else:
        print("I'm sorry. That was incorrect. The correct answer would be " + answer + ".")
        questionList[questionNumber] = NO_QUESTION
        keepGoing = hasQuestions(questionList)


print("")
print("   ___                   ___                _ ")
print("  / __|__ _ _ __  ___   / _ \__ _____ _ _  | |")
print(" | (_ / _` | '  \/ -_) | (_) \ V / -_) '_| |_|")
print("  \___\__,_|_|_|_\___|  \___/ \_/\___|_|   (_)")
print("")
print("You earned a total of " + str(currentWinnings) + " dollars!")
print("")

                                              
