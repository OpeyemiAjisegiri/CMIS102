"""
#### PRE-DEFINED DATA USED [AND TESTING GRADES] #####
STUDENTS          | TEST 1: GRADE  | TEST 2: GRADE
Allen Curry       |    85.7        |    94.6
Brenda Parlor     |    89.9        |    80.4
Xio Ting          |    100         |    90.5
Joy King          |    92.3        |    78.6
Clint Black       |    90.0        |    70.8
##################################################

###########       ALGORITHM       ################  
DEFINE and DECLARE a list containing the names of students
DECLARE and DEFINE prevGrade to ZERO
DECLARE and DEFINE totalGrade = 0
DECLARE and DEFINE num_of_grades = 0
FOR student in students array/list
   currentGrade = GET student's grade
   SET totalGrade += currentGrade
   INCREMENT num_of_grades
   IF currentGrade > prevGrade
      SET highestGrade = currentGrade
      SET prevGrade = curentGrade
    ENIF
ENDFOR
PRINT the highestGrade
PRINT the class average
################################################
"""

#DEFINE and DECLARE and array or list containing the names of students 
students = ["Allen Curry", "Brenda Parlor", "Xio Ting", "Joy King", "Clint Black"]
print(students)
prevGrade = 0                           #DECLARE and DEFINE prevGrade = 0
totalGrade = 0                          #DECLARE and DEFINE totalGrade = 0
num_of_grades = 0                       #DECLARE and DEFINE num_of_grades = 0
for x in students:                      #FOR each student in students 
    #currentGrade = GET student's grade
    currentGrade = eval(input("Please enter {}'s grade: \t".format(x)))
    totalGrade += currentGrade          #SET totalGrade += currentGrade 
    num_of_grades += 1                  #INCREMENT num_of_grades
    if currentGrade > prevGrade:        #IF currentGrade > prevGrade
        highestGrade = currentGrade     #SET highestGrade = currentGrade
        prevGrade = currentGrade        #SET prevGrade = curentGrade
#PRINT the highestGrade
print("The highest grade in the class is: ", highestGrade)
#COMPUTE and PRINT class average
print("The class average is : ", round(totalGrade / num_of_grades,2))
