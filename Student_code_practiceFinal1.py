
#==========================================================================
## I CERTIFY THAT THE CODE SHOWN BELOW IS MY OWN WORK
## AND THAT I HAVE NOT VIOLATED THE UNCW ACADEMIC HONOR CODE
## WHILE WRITING THIS CODE
## you may use your editor, help from the shell, use your textbooks, 
## your previous codes, and the lecture notes as reference
## no other resources can be used during the test.
## no additional import statements please
## If the function is not complete as instructed, you get
## AT BEST 50% of the grade for that question.

# PROGRAM PURPOSE:... Practice 1 
# AUTHOR:............ Last, First
# COURSE:............ CSC 131-YOUR SECTION NUMBER
# TERM:.............. Fall 2021
# COLLABORATION:..... None
#==========================================================================

from testing_practice1 import test,test_file_content,test_LOM,testNoPrint
import sys
import random


#=============================================================================
# q1 - create function quarter() to meet the conditions below
#    - accept one parameter:  a string (month name)
#    - add a meaningful docstring
#    - determine the quarter of the year given the month name
#    - return the quarter # (1, 2, 3, or 4)
#    - you can assume that the input parameter is a valid, full name of a month
#
#    --- e.g. for March -> returns 1
#    --- e.g. for June -> returns 2
#    --- e.g. for October -> returns 4
#
#    The quarters are:
#    --- quarter 1: January - March
#    --- quarter 2: April - June
#    --- quarter 3: July - September
#    --- quarter 4: October - December
#
#    - RESTRICTIONS:  None
#
#    - param:   string
#    - return:  integer
#=============================================================================


       
    
    
#=============================================================================
# q2 - create function listOfLists() to meet the conditions below
#    - accept one parameter:  a list of lists of integer values
#    - add a meaningful docstring
#    - the lists in the list are all of a same size
#    --- e.g. [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
#    --- e.g. [ [4, 3, 2, 1], [4, 4, 3, 6], [1, 0, 5, 2] ]
#    --- e.g. [ [3, 2], [6, 6], [1, 9], [2, 8] ]
#    - calculate the sum of the matched items from all the lists,
#       store them into a new list and return it
#    --- e.g. [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ] -> returns [12, 15, 18]
#    --- e.g. [ [4, 3, 2, 1], [4, 4, 3, 6], [1, 0, 5, 2] ] -> returns [9, 7, 10, 9]
#    --- e.g. [ [3, 2], [6, 6], [1, 9], [2, 8] ] -> returns [12, 25]
#    - return the new list
#
#    - RESTRICTIONS:  None
#
#    - params:  integer
#               integer
#    - return:  integer
#=============================================================================

def listOfLists(lst):

    newlist = []
    newlist.append(lst[0][0]+lst[1][0]+lst[2][0])
    newlist.append(lst[0][1]+lst[1][1]+lst[2][1])
    newlist.append(lst[0][2]+lst[1][2]+lst[2][2])
    return(newlist)
        
    
    
#==========================================================================
# q3 - create function longestLength() to meet the conditions below
#    - accept unknown number of parameters: n strings (n>0)
#    - add a meaningful docstring
#    - return the length of the longest string
#
#    --- e.g. "Hello" and "Good-bye", 'Hi'; function returns 8
#    --- e.g. "Hello"; function returns 5
#
#    - RESTRICTIONS: None
#
#    - params:  n number of string(s)
#    - return:  integer
#==========================================================================

def longestLength(*seq): 
    longest = len(seq[0])
    for i in seq:
        if len(i) > longest:
            longest = len(i)
    return longest

    
    
#==========================================================================
# q4 - create function numTriangle() to meet the conditions below
#    - accept one parameter: a single digit integer
#    - add a meaningful docstring
#    - creates a number triangle with x rows.
#    - each row consists of the row numbers starting from 10.
#    - you can assume the parameter is a value between 2 and 9 (both inclusive).
#
#    --- e.g. 3 is passed to the function
#       displays:
#       10
#       10 11
#       10 11 12
#    --- e.g. 5 is passed to the function
#       displays:
#       10
#       10 11
#       10 11 12
#       10 11 12 13
#       10 11 12 13 14
#
#    - RESTRICTIONS: None
#
#    - param:   integer
#    - return:  None
#==========================================================================

def numTriangle(int):

#how to go to new line between loops
    print(int)
    for r in range(10, 10+int+1):
        for c  in range(10, r):
            print(c, end = ' ')



     
    
    
#==========================================================================
# q5 - create function combineWords() to meet the conditions below
#    - accept two parameters: two lists named firstnames and lastnames
#    - add a meaningful docstring
#    - returns a new list representing all possible combinations of EACH
#    - firstname string and EACH lastname string with a space between
#
#    --- e.g. first: ["sara", "alex"] and last: ["smith", "murphy"]
#       returns the final list:
#       ["sara smith", "sara murphy", "alex smith", "alex murphy"]
#       
#
#    - RESTRICTIONS: None
#
#    - params:  list
#               list
#    - return:  list
#==========================================================================

def combineWords(firstnames, lastnames):
    newlist=[]
    for i  in firstnames:
        for j in lastnames:
            newlist.append(i + ' '+ j)
    return newlist


    
#==========================================================================
# q6 - create function secondIndex() to meet the conditions below
#    - accept two parameters: a list of integers and an integer
#    - add a meaningful docstring
#    - find the index of the SECOND occurrence of the number (2nd parameter)
#       in the list (1st parameter).
#    - return: Index of second occurrence of the integer in the list.
#    - -1 if the number does not occur two or more times in the list.
#
#    --- e.g. 1: secondIndex([2,34,3,45,34,45,3,3], 3) returns 6
#    --- e.g. 2: secondIndex([2,34,3,45,34,45,3,3], 45) returns 5
#    --- e.g. 3: secondIndex([2,34,3,45,134,45,3,3], 134) returns -1
#    --- e.g. 4: secondIndex([2,34,3,45,134,45,3,3], 100) returns -1
#
#    - RESTRICTIONS: None
#
#    - params:  list
#               integer
#    - return:  integer
#==========================================================================

# def secondIndex(lst, int):
#     for i in lst:
#         if i == int:


        
    
    
#==========================================================================
# q7 - create function lineLengths() to meet the conditions below
#    - accept one parameter: a string (filename)
#    - add a meaningful docstring
#    - open the file and read each line
#    - count the characters in each line
#    - don't forget to close the file
#    - return the length of the longest line in the file
#    - it's not required for you to handle the line breaks at the end.
#    - test files (sample1.txt, sample2.txt) will be created by the testing code.
#
#    - RESTRICTIONS: None
#
#    - param:   string
#    - return:  integer
#==========================================================================

def lineLengths(filename):
    file = open('filename.txt', 'r')
    longest = 0
    for line in file:
        for character in line:
            if character >longest:
                longest = character
    return(len(longest))
             


    file.close()



    
#==========================================================================
# q8 - create function writeRandomNumbers() to meet the conditions below
#    - accept one parameter: a string (filename) 
#    - add a meaningful docstring
#    - write ten random integers (of your choice) between 0 and 100 into the textfile
#      ---NOTE:  if done correctly, the output textfile is placed in the same
#                directory as this exam file
#    - don't forget to add the newline (line break) character to each line
#    - don't forget to close the file
#    - the testing code will create two files by itself for two test cases.
#    - return None 
#
#    - RESTRICTIONS:  None
#
#    - param:   string
#    - return:  None
#
#==========================================================================

    
    
#==========================================================================
# q9 - create function mergeLists() to meet the conditions below
#    - accept two parameters:  two lists
#    - add a meaningful docstring
#    - you may assume the lists are the same length
#    - return the merged dictionary
#
#    --- e.g.
#        list1 is: ['A', 'B', 'C']
#        list2 is : [1, 4, 5]
#        Resultant dictionary is : {'A': 1, 'B': 4, 'C': 5}
#
#    - RESTRICTIONS:  None
#
#    - params:  list
#               list
#    - return:  dictionary
#==========================================================================
def mergeLists(lst1, lst2):
    dictionary = {}
    for key in lst1:
        for value in lst2:
            dictionary[key] = value

    return dictionary
    
#==========================================================================
# q10- create function sumNum() to meet the conditions below
#    - accept one parameter: an n-character string
#    - add a meaningful docstring
#    - find all the string numbers in the string, convert them to integer
#      and add them together
#    - you may assume all numbers are single digit
#    - return the integer result
#
#    --- e.g. "2KL5", returns 7
#    --- e.g. "Z3r5Q1h2g5Q", returns 16
#    --- e.g. "5A1E3yfE0", returns 9
#
#    - RESTRICTIONS:  None
#
#    - param:   string
#    - return:  integer
#==========================================================================


    
    
#==========================================================================
# q11 - DEBUG function numVowels(sentence)
#    - This function currently returns INCORRECT answers
#    - Find and fix the error(s) in the function below
#
#    - accept one parameter: sentence - a string  
#
#    - numVowels should iterate over the string and count how many of the
#      characters are vowels
#    - you may assume all the letters are lowercases.
#    - return the number of vowels
#
#    ---e.g. 'Hello' returns 2
#
#    - RESTRICTIONS: do NOT re-write the function, just find/fix error(s)
#
#    - param:  string
#    - return: integer
#
#==========================================================================
def numVowels(sentence):
    count = 0
    for ch in sentence:
        if ch in ['aeiou']:  
            count =+ 1

    return ch





#==========================================================================
# *************************************************************************
# ******************* DO NOT EDIT CODE BELOW THIS POINT *******************
# *************************************************************************
#==========================================================================
def printErr():
    print(" ",sys.exc_info()[0].__name__,"-line",sys.exc_info()[-1].tb_lineno)
    print(" ",sys.exc_info()[1])
    
#==========================================================================   
def test_quarter():
    results = []
    print("\n\t\t**** (10 points) - quarter() ****")
    monthList = [(1,'January'), (1,'February'), (1,'March'), (2,'April'),
                 (2,'May'), (2,'June'), (3,'July'), (3,'August'),
                 (3,'September'), (4,'October'), (4,'November'), (4,'December')]

    passed = 0
    attempted = 0

    for i in range(3):
        attempted += 1
        idx = random.randint(0,11)
        if test(monthList[idx][0], quarter, monthList[idx][1]):
            passed += 1

    return passed, attempted

#==========================================================================
def test_listOfLists():
    results = []
    print("\n\t\t**** (10 points) - listOfLists() ****")
    passed = 0
    attempted = 0
    lst = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
    anw = [12, 15, 18]
    attempted += 1
    if test(anw, listOfLists, lst):            
        passed += 1
    lst = [ [4, 3, 2, 1], [4, 4, 3, 6], [1, 0, 5, 2] ]
    anw = [9, 7, 10, 9]
    attempted += 1
    if test(anw, listOfLists, lst):            
        passed += 1
    lst = [ [3, 2], [6, 6], [1, 9], [2, 8] ]
    anw = [12, 25]
    attempted += 1
    if test(anw, listOfLists, lst):            
        passed += 1
    
    return passed, attempted
            
#==========================================================================
def test_longestLength():
    import string
    print("\n\t\t**** (10 points) - longestLength() ****")
    lst1 = (('sam', 3),('rose',4),('apple',5))    
    lst3 = (('Tom','Alex','Rose', 4), ('book', 'fork','keypad','cup', 6),
            ('orange', 'apple', 'cherry', 6))
    lst4 = (('boo','banana', 'cherry', 'hi', 6), ('sara', 'derek', 'tom', 'jack', 5),
            ('watermelon', 'banana', 'orange', 'apple', 10))

    passed = 0
    attempted = 0
    for i in range(3):        
        a = random.randint(0,2)
        attempted += 1
        if test(lst1[a][-1], longestLength, lst1[a][0]):            
            passed += 1
        attempted += 1
        if test(lst3[a][-1], longestLength, lst3[a][0],lst3[a][1],lst3[a][2]):            
            passed += 1
        attempted += 1
        if test(lst4[a][-1], longestLength, lst4[a][0],lst4[a][1],lst4[a][2],lst4[a][3]):            
            passed += 1
    return passed, attempted    

#==========================================================================
def test_numTriangle():
    results = []
    print("\n\t\t**** (10 points) - numTriangle() ****")
    
    passed = 0
    attempted = 0
    row = random.randint(2,9)
    numTriangle(row)
    row = random.randint(2,9)
    numTriangle(row)
    return passed, attempted    

#==========================================================================
def test_combineWords():
    print("\n\t\t**** (10 points) - combineWords() ****")    
    passed = 0
    attempted = 0
    
    first = ['sara', 'peter', 'alex', 'tom']
    last = ['smith', 'brown', 'jones']
    names = ['alex brown', 'alex jones', 'alex smith', 'peter brown',
             'peter jones', 'peter smith', 'sara brown', 'sara jones',
             'sara smith', 'tom brown', 'tom jones', 'tom smith']
    attempted += 1
    if test(names, combineWords, first, last):
        passed += 1

        
    first = ['rick', 'peter']
    last = ['williams', 'davis', 'wilson']
    names = ['peter davis', 'peter williams', 'peter wilson',
             'rick davis', 'rick williams', 'rick wilson']
    attempted += 1
    if test(names, combineWords, first, last):
        passed += 1

    return passed, attempted

#==========================================================================
def test_secondIndex():
    results = []
    print("\n\t\t**** (10 points) - secondIndex() ****")    
    passed = 0
    attempted = 0
    
    nums = [20,2,5,4,54,24,24,25,2,5,10,10,2]
    values = [(20,-1), (2,8), (5,9), (25,-1), (100,-1)]
    random.shuffle(values)

    for i in range(4):
        attempted += 1
        if test(values[i][1], secondIndex, nums, values[i][0]):            
            passed += 1
    
    return passed, attempted    
        
#==========================================================================
def test_lineLengths():
    results = []
    print("\n\t\t**** (10 points) - lineLengths() ****")
    lst1 = ('pretty', 'sick', 'warm', 'nice', 'tired', 'book',
           'pillow', 'bedroom', 'car', 'sky', 'wonderful')
    maxLen1 = 9
    output_file = open("sample1.txt",'w')
    ms = ""
    ml = []
    for i in range(len(lst1)):
        output_file.write(lst1[i]+"\n")
    output_file.close()
    
    lst2 = ('hall', 'gallery', 'factory', 'depot', 'barn', 'airport',
           'garage', 'gym', 'hotel', 'cabin', 'mall', 'kiosk')
    maxLen2 = 7
    output_file = open("sample2.txt",'w')
    ms = ""
    ml = []
    for i in range(len(lst2)):
        output_file.write(lst2[i]+"\n")
    output_file.close()    

    passed = 0
    attempted = 0

    attempted += 1
    if test(maxLen1,lineLengths,"sample1.txt") or test(maxLen1+1,lineLengths,"sample1.txt"):            
        passed += 1
    attempted += 1
    if test(maxLen2,lineLengths,"sample2.txt") or test(maxLen2+1,lineLengths,"sample2.txt"):            
        passed += 1

    return passed, attempted  

#==========================================================================
def test_writeRandomNumbers():
    results = []
    print("\n\t\t**** (10 points) - writeRandomNumbers() ****")
    
    passed = 0
    attempted = 0

    writeRandomNumbers("sample_output1.txt")
    inputFile = open("sample_output1.txt", 'r')
    count = 0
    attempted += 1
    passed += 1
    for i in inputFile:
        count += 1
        if int(i.strip()) < 0 or int(i.strip()) > 100:
            passed = 0
    if count != 10:
        passed = 0

    writeRandomNumbers("sample_output2.txt")
    inputFile = open("sample_output2.txt", 'r')
    count = 0
    attempted += 1
    passed += 1
    for i in inputFile:
        count += 1
        if int(i.strip()) < 0 or int(i.strip()) > 100:
            passed = 0
    if count != 10:
        passed = 0


    return passed, attempted

#==========================================================================
def test_mergeLists():
    results = []
    print("\n\t\t**** (10 points) - mergeLists() ****")
    eng = ["samples", "test", "earth", "book", "glass", "ball"]
    spn = ["muestras", "prueba", "tierra", "libro", "vaso", "pelota"]
    translate = {"samples":"muestras", "test":"prueba", "earth":"tierra",
                 "book":"libro", "glass":"vaso", "ball":"pelota"}
    passed = 0
    attempted = 0

    attempted += 1
    if test(translate,mergeLists,eng,spn):            
        passed += 1

    lst1 = ['A', 'B', 'C']
    lst2 = [1, 4, 5]
    final = {'A': 1, 'B': 4, 'C': 5}
    attempted += 1
    if test(final,mergeLists,lst1,lst2):            
        passed += 1
        
    return passed, attempted    
    
#==========================================================================
def test_sumNum():
    results = []
    print("\n\t\t**** (5 points) - sumNum() ****")
    passed = 0
    attempted = 0
    lst = [("2KL5",7), ("Z5Q1h2Q",8), ("0r5A1E3yfE2",11)]

    for i in range(len(lst)):
        attempted += 1
        if test(lst[i][1],sumNum,lst[i][0]):            
            passed += 1

    return passed, attempted
        
#==========================================================================   

def test_numVowels():
    results = []
    print("\n\t\t**** (5 points) - numVowels() ****")
    passed = 0
    attempted = 0
    lst = [("hello world",3), ("table",2), ("it is a nice day!",6),
           ("picnic",2), ("myth",0), ("rhythm",0), ("sync",0)]
    for i in range(len(lst)):
        attempted += 1
        if test(lst[i][1],numVowels,lst[i][0]):            
            passed += 1

    return passed, attempted    
        
# Main =======================================================================
def main():

    testFunctionList = [test_quarter, test_listOfLists,
                        test_longestLength, test_numTriangle,
                        test_combineWords, test_secondIndex,
                        test_lineLengths, test_writeRandomNumbers,
                        test_mergeLists, test_sumNum,
                        test_numVowels]
    
    functionNames = ["quarter", "listOfLists", 
                     "longestLength", "numTriangle",
                     "combineWords", "secondIndex",
                     "lineLengths", "writeRandomNumbers",
                     "mergeLists", "sumNum",
                     "numVowels"]

    points = [-1 for i in range(len(testFunctionList))]
    totals = [0 for i in range(len(testFunctionList))]

    for i in range(len(testFunctionList)):
        try:
            points[i], totals[i] = testFunctionList[i]()
                
        except:
            print("**Something is wrong with " + functionNames[i] + "()")
            printErr()
            points[i], totals[i] = -1, 0

    print("\n\n")
    print("Summary of the Test Results")
    print("======================================")

    for i in range(len(testFunctionList)):
        print(format('q'+str(i+1),'<4'), format(functionNames[i], "27s"), end="")
        if points[i] >= 0:
            print("%2d out of %2d" % (points[i], totals[i]))            
            if points[i] == totals[i] and points[i] in [0,1]:
                print("{}: Instructor will check the output in read-time".format(functionNames[i]))
        else:
            print("Not defined or error in function")
#fail =========================================================================
def countFailed(points, totals):
    count = 0
    for i in range(len(points)):
        count += points[i] != totals[i]
    return count
#call =========================================================================
if __name__ == "__main__":
    main()



