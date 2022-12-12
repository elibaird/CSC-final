# PROGRAM PURPOSE:............ Final Exam
# (1 point) AUTHOR:............ Last, First
# COURSE:..................... CSC 131-YOUR SECTION NUMBER
# TERM:....................... Fall 2022
# YOU MUST NOT CONSULT ANYONE (OTHER THAN YOUR INSTRUCTOR) ON
# ANYTHING ON THIS TEST
#==========================================================================
## Read and follow all instructions carefully
##
## I CERTIFY THAT THE CODE SHOWN BELOW IS MY OWN WORK
## AND THAT I HAVE NOT VIOLATED THE UNCW ACADEMIC HONOR CODE
## WHILE WRITING THIS CODE
##
## You may use your editor, help from the shell, your textbooks,
## computer programs previously written by you,
## and the lecture notes as reference.
## No other resources can be used during the test.
## You MAY NOT visit any web site or Google anything
## No additional import statements please
##
## You must include a meaningful docstring with each function
##
## If the function is not complete as instructed, you get
## AT BEST 50% of the grade for that question.
#==========================================================================

## NO ADDITIONAL IMPORT STATEMENTS ALLOWED
from testing_Test2_F22 import test,test_file_content,test_LOM,testNoPrint,test_NoReturn
import sys
import random



#=============================================================================
# q1 - create function quarter() to meet the conditions below
#    - accept one parameter: a string corresponding to the name of a month
#    - string 'month' is a capitalized word (the first letter is an uppercase letter)
#    - determine the quarter of the year within which the month falls
#       --- Example 1: for March -> returns 1
#       --- Example 2: for June -> returns 2
#       --- Example 3: for October -> returns 4
#    - return the quarter # (1, 2, 3, or 4)
#    The quarters are:
#    --- quarter 1: January - March
#    --- quarter 2: April - June
#    --- quarter 3: July - September
#    --- quarter 4: October - December
#
#    - RESTRICTIONS:  None
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - param:  string
#    - return:  integer
#=============================================================================




#==========================================================================
# q2 - create function sumOfSquares() to meet the conditions below
#    - accept one parameter: an integer
#    - calculate the sum of all the squares of integers from 1 up to
#      and including the integer parameter
#        --- Example 1: 5 -> returns 55, i.e (1+4+9+16+25)
#        --- Example 2: 10 -> returns 385, i.e. (1+4+9+16+25+36+49+64+81+100)
#    - return the sum of squares
#
#    - RESTRICTIONS:  You may NOT use the built-in sum function
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - param:  integer
#    - return: integer
#==========================================================================

def sumOfSquares(int):
    sum = 0
    for i in range(1, int +1):
        sum = sum + (i**2)
    return sum





#==========================================================================
# q3 - create a function named:  divisibleByTwoInts to meet the conditions below
#    - accept 2 integer parameters n1 and n2
#    - and returns a list of numbers between 1 and 100, both included,
#     that are divisible by both n1 and n2.
#       --- Example 1: 
#               n1 = 3
#               n2 = 7
#               returns the list:  [21, 42, 63, 84]
#
#       --- Example 2: 
#               n1 = 50
#               n2 = 150
#               returns the list:  []
#
#    - RESTRICTIONS:  None
#
#    - HINT: You may want to use the modulo operator
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#
#     param:    integer
#               integer
#     return:   list (of integers)
#==========================================================================

def divisibleByTwoInts(n1,n2):
    lst=[]
    for i in range(1, 101):
        if i%n1 ==0 and i%n2==0:
            lst.append(i)
    return lst



#==========================================================================
# q4 - create function addValue() to meet the conditions below
#    - accept two parameters: a list of numbers and a number
#    
#    - iterate over the list and add the 2nd parameter value to each
#    - value in the list.
#
#    - you MUST change the values within the list and NOT create a new list
#
#       --- Example: [-5.4379, 7.0643, -41.87, 174.53, -4220] and 33.3 ->
#                     [27.8621, 40.3643, -8.57, 207.83, -4186.7]
#
#    - RESTRICTIONS:  None
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - param:  list (of numbers)
#              float
#    - return: None
#==========================================================================

def addValue(lst, flt):
    for i in range(len(lst)):
        lst[i] = lst[i] + flt
    




#==========================================================================
# q5 - create function commonItem() to meet the conditions below
#    - accept two lists of arbitrary values as parameters
#    
#    - returns True if the lists share at least one common member,
#       False otherwise
#       --- Example 1: [2,5,4,7,2] and [1,2,1,4,2] -> returns True
#       --- Example 2: ['a','b','c','a'] and ['g','z','f'] -> returns False
#
#    - RESTRICTIONS: You are NOT allowed to use set() function. You also
#       may NOT use the "in" operator with an "if" statement.
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - param:  list
#              list
#    - return: boolean
#==========================================================================

def commonItem(lst1, lst2):
    for i in lst1:
        for j in lst2:
            if i ==j:
                return True
    return False            




#=============================================================================
# q6 - create function openAndReturnAverage() to meet the conditions below
#    - accept one parameter:  a file name
#    - return the average of the integer values in the textfile
#      NOTE:
#           --- the file is automatically generated when this exam file
#                is run and it is placed in the same directory as this
#                exam file
#           --- The file contains one integer per line
#           --- don't forget to close the file
#
#    - RESTRICTIONS:  None
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - params:  string
#    - return:  float
#=============================================================================

def openAndReturnAverage(filename):
    file = open(filename, 'r')
    total = 0
    num = 0
    
    for i in file:
        total = total + int(i.strip())
        num = num +1
    avg = float(total / num)
    return avg

        




#==========================================================================
# q7 - create function writeMinMaxSumCount() to meet the conditions below
#    - accept 2 parameters; a str (filename) & a list (arbitrary numbers)
#    
#    - open the filename for writing
#    - iterate over the list and write into the textfile the min, max, sum, 
#        and count of all the numbers in the list
#    --- don't forget to add the newline character to each line 
#       --- example: [1, 2, 0, 3, 2, 2, 5, 1, 4, 1, 1, 1]
#       --- the following numbers must be written into the file:
#           --- 0
#           --- 5
#           --- 23
#           --- 12
#    --- don't forget to close the file
#    - the output file is called sample_output1.txt or sample_output2.txt
#    - and will be created in the same folder as your program.
#    - you can open the output file to check its contents.
#
#    - RESTRICTIONS:  None
#
#      HINT: You may want to use the built-in functions min, max, sum, len
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - params:  string
#               list (of integers)
#    - return:  None
#==========================================================================

def writeMinMaxSumCount(filename,lst):
    file = open(filename, 'w')
    file.write(str(min(lst))+'\n')
    file.write(str(max(lst))+'\n')
    file.write(str(sum(lst))+'\n')
    file.write(str(len(lst))+'\n')
    
    file.close


#==========================================================================
# *************************************************************************
# ******************* DO NOT EDIT CODE BELOW THIS POINT *******************
# *************************************************************************
#==========================================================================
def printErr():
    print(" ",sys.exc_info()[0].__name__,"-line",sys.exc_info()[-1].tb_lineno)
    print(" ",sys.exc_info()[1])
    
#q1 =========================================================================
def test_quarter():
    print("\n\n\t*******(10 points) - quarter********")
    monthList = [(1,'January'), (1,'February'), (1,'March'), (2,'April'),
                 (2,'May'), (2,'June'), (3,'July'), (3,'August'),
                 (3,'September'), (4,'October'), (4,'November'), (4,'December')]

    passed = 0
    attempted = 0

    for i in range(5):
        attempted += 1
        idx = random.randint(0,11)
        if test(monthList[idx][0], quarter, monthList[idx][1]):
            passed += 1

    return passed, attempted



#q2==========================================================================
def test_sumOfSquares():
    print("\n\t\t**** (10 points) - sumOfSquares() ****")
    passed = 0
    attempted = 0
    values = [(20,2870),(2,5),(5,55),(4,30), (10,385), (0,0)]
    random.shuffle(values)
    for i in range(6):        
        attempted += 1
        if test(values[i][1], sumOfSquares, values[i][0]):          
            passed += 1
    return passed, attempted


#q3==========================================================================
def test_divisibleByTwoInts():
    import string
    print("\n\t\t**** (10 points) - divisibleByTwoInts() ****")
    passed = 0
    attempted = 0
    values = ((3,7,[21, 42, 63, 84]),(50,150,[]),(2,11,[22,44,66,88]),(31,11,[]),(20,4,[20, 40, 60, 80, 100]))
    for i in range(5):
        attempted += 1
        if test(values[i][2], divisibleByTwoInts, values[i][0], values[i][1]):
            passed += 1
    return passed, attempted
           



#q4==========================================================================
def test_addValue():
    print("\n\t\t**** (10 points) - addValue() ****")
    passed = 0
    attempted = 0

    nums = [(random.random() * 1000 - 500) for i in range(100)]
    pos = []
    for i in nums:
        pos.append(abs(i))

    for i in range(5):
        nums1 = []
        value = random.random() * 1000 - 500
        nums2 = []
        for j in range(10):
            k = random.randint(0, 99)
            nums2.append(nums[k])
            nums1.append(nums[k] + value)
        attempted += 1
        
        if test_NoReturn(nums1, addValue, nums2, value): passed += 1

    return passed, attempted
      
#q5==========================================================================
def test_commonItem():
    print("\n\t\t**** (10 points) - commonItem() ****")
    passed = 0
    attempted = 0

    lst1 = [2,5,4,7]
    lst2 = [1,2,1,4]  
    attempted += 1
    if test(True, commonItem, lst1, lst2):
        passed += 1

    lst1 = ['a','b','c','a']
    lst2 = ['g','a','c'] 
    attempted += 1
    if test(True, commonItem, lst1, lst2):
        passed += 1
    
    lst1 = ['sara', 'peter', 'alex', 'tom']
    lst2 = ['smith', 'brown', 'jones']    
    attempted += 1
    if test(False, commonItem, lst1, lst2):
        passed += 1

    return passed, attempted



#q6==========================================================================
def test_openAndReturnAverage():
    results = []
    print("\n\t\t**** (10 points) - openAndReturnAverage() ****")    
    passed = 0
    attempted = 0
    
    list_Size = 10
    lst = random.sample(range(1, 100), list_Size) 
    total = sum(lst)/len(lst)
    random.shuffle(lst)
    output_file = open("sample_input1.txt",'w')
    ms = ""
    ml = []
    for i in range(len(lst)):
        output_file.write(str(lst[i])+"\n")
    output_file.close()
    attempted += 1
    if test(total,openAndReturnAverage,"sample_input1.txt"):            
        passed += 1
        
    list_Size = 5
    lst = random.sample(range(1, 100), list_Size)  
    total = sum(lst)/len(lst)
    random.shuffle(lst)
    output_file = open("sample_input2.txt",'w')
    ms = ""
    ml = []
    for i in range(len(lst)):
        output_file.write(str(lst[i])+"\n")
    output_file.close()     
    attempted += 1
    if test(total,openAndReturnAverage,"sample_input2.txt"):            
        passed += 1

    return passed, attempted          

#q7 =========================================================================
def test_writeMinMaxSumCount():
    results = []
    print("\n\t\t**** (10 points) - writeMinMaxSumCount() ****")

    attempted = 0
    passed = 0

    list_Size = 10
    for n in range(0,3):
        lst = random.sample(range(1, 100), list_Size)  
        random.shuffle(lst)
        
        attempted += 1
        filename = "sample_output"+str(n+1)+'.txt'
        returnVal = writeMinMaxSumCount(filename, lst)
        try:
            infile = open(filename, 'r')
        except:
            print("The output file hasn't be created correctly")
        finalList = [min(lst), max(lst), sum(lst), len(lst)]
        studentList = []
        for i in infile:
            studentList.append(int(i.strip()))
        
        if studentList == finalList and returnVal is None:
            passed += 1
        infile.close()
    

    return passed, attempted

        

# Main =======================================================================
def main():

    testFunctionList = [test_quarter, test_sumOfSquares, test_divisibleByTwoInts, test_addValue, test_commonItem,
                        test_openAndReturnAverage, test_writeMinMaxSumCount]
        
    functionNames = ['quarter', 'sumOfSquares', 'divisibleByTwoInts', 'addValue', 'commonItem',
                     'openAndReturnAverage', 'writeMinMaxSumCount']

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
        #print(format('q'+str(i+1),'<4'), format(functionNames[i], "27s"), end="")
        print(format('q'+str(i+1),'<4'), format(functionNames[i], "27s"), end="")
        if points[i] >= 0:
            print("%2d out of %2d" % (points[i], totals[i]))            
            if points[i] == totals[i] and points[i] in [0,1]:
                print("{}: Instructor will check the output manually".format(functionNames[i]))
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


