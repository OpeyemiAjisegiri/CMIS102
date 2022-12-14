           ######       Assignment 1      ######

#####     TASK  ######
#Calculate a car sales weekly earning using
#Using user inputed values: hours worked and week's sales
#And programmer's pre-defined hourly wage and commission



####           Pseudocode               ####
#DECLARE and DEFINE constants: HRLYWAGE  and COMMISSION
##Employee earns $15/hour and a commission of 20%
#PROMPT user to input the numbers of hours worked
#  Accept input [eval(input)]
#MULTIPLY  input with 'HRLYWAGE' 
#PROMPT user to input the amount of weekly sales
#    Accept the input
#MULTIPLY input with 'COMMISSION'
#Calculate weekly wage  through ADDITION
#PRINT wklyWage



####      Program: Code Base     ####
HRLYWAGE   = 15         
COMMISSION = 0.20       
hrsWorked  = eval(input('Enter the number of hours worked: \t'))
wklyWage   = hrsWorked * HRLYWAGE
wkSales    = eval(input('Enter the amount of sales for this week: '))
wklyCom    = (wkSales * COMMISSION)
wklyWage += wklyCom
print('The employee earned: $', round(wklyWage, 2), ' this week')
   
