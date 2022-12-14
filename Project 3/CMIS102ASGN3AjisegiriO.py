"""
                           PSEUDOCODE
START: 
    Function: calculateCost
      Params: width, length, carpetGrade
      IF carpetGrade == BASIC
          SET surcharge to 20%
      ELIF carpetGrade == NORMAL
          SET surcharge to 60%
      ELIF carpetGrade == LUXURY
          SET surcharge to 120%
      ENDIF
      SET carpetPrice to surcharge + base price
      SET totalPrice to the MULTIPLICATION of width, length, and carpetPrice
      RETURN totalPrice
    EndFunction

    SET BASE PRICE = $10.00 per Sq Ft
    
    GET width: width                         
    GET length: length
    GET grade of carpet: carpetGrade         
    CALL FUNCTION: calculateCost(width, length, carpetGrade)
    SET RETURN VALUE to cost
    PRINT cost
END
"""



def calculateCost(w,l,cg):                    #Function: calculateCost
    if cg == 1:                               #IF carpetGrade == BASIC
        surcharge = 0.20                      #  SET surcharge to 20%
    elif cg == 2:                             #ELIF carpetGrade == NORMAL
        surcharge = 0.60                      #  SET surcharge to 60%
    elif cg == 3:                             #ELIF carpetGrade == LUXURY 
        surcharge = 1.20                      #  SET surcharge to 120%
    cPrice = (surcharge * B_PRICE) + B_PRICE  #Computing carpet price 
    totalPrice = cPrice * w * l               #Calculating the total price
    return totalPrice                         #returning the total price to MAIN

B_PRICE = 10.00                               #SET BASE PRICE = $10.00 per SqFt

#Getting WIDTH, LENGTH, CARPETGRADE values from the user
width = eval(input("Please enter the width of the room to be carpetted: \t"))
length = eval(input("Please enter the length of the room to be carpetted: \t"))
carpetPrice = eval(input("Please enter the quality of the carpet:- 1:Basic, 2:Normal, 3:Luxury : \t"))
#Calling the function to calculate the total price.
cost = calculateCost(width, length, carpetPrice)
#Printing out the total price
print("The price of carpeting the room is: $", cost)

