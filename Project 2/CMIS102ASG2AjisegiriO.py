######         TASK           ######
#Program should compute the price of a theater ticket 
#Using the patron's age and movie format [standarad OR 3D] 
#Children and seniors get a discount  
#3D movies have a sur-charged. 


#####            Pseudode         #####
#DECLARE and DEFINE constants: B_PRICE, C_DISCOUNT,S_DISCOUNT, SURCHARGE
#B_PRICE = $12.00
#C_DISCOUNT = (100 - 30)% = 70% = 0.70
#S_DISCOUNT = (100 - 35)% = 65% = 0.65
#SURCHARGE = 20% = 0.20
#PROMPT user for patron's age: age
#PROMPT user for movie format [standard or 3D]: mFormat
#IF age <= 10 and movie == standard
#     price = B_PRICE * C_DISCOUNT
#     PRINT price
#ELIF age <= 10 and movie == 3D
#     price = (B_PRICE + (B_PRICE * % of surcharge)) * C_DISCOUNT
#     PRINT price
#ELIF age <= 10 and movie == standard
#     price = B_PRICE * SEN_DISCOUNT
#     PRINT price
#ELIF age > 10 and movie == 3D
#     price = (B_PRICE + (B_PRICE * % of surcharge)) * S_DISCOUNT
#     PRINT price
#ELSE
#    IF age > 10 and movie == standard
#        price = B_PRICE
#        PRINT price
#    ELIF age > 10 and movie == 3D
#        price = B_PRICE + (B_PRICE * % of surcharge)
#        PRINT price


B_PRICE = 10.00
C_DISCOUNT = 0.70
S_DISCOUNT = 0.60
SURCHARGE = 0.25
age = eval(input("Please enter patron's age: \t"))
mFormat = input("Please enter the movie format [standard OR 3D]:   ")
if age <= 10 and mFormat == "standard":
    print("The price of the movie is: $", (B_PRICE * C_DISCOUNT))
elif age <= 10 and mFormat == "3D":
    print("The price of the movie is: $", ((B_PRICE + (B_PRICE * SURCHARGE)) * C_DISCOUNT))
elif age >= 65 and mFormat == "standard":
    print("The price of the movie is: $", (B_PRICE * S_DISCOUNT))
elif age >= 65 and mFormat == "3D":
    print("The price of the movie is: $", ((B_PRICE + (B_PRICE * SURCHARGE)) * S_DISCOUNT))
else: 
    if age > 10 and mFormat == "standard":
        print("The price of the movie is : $", B_PRICE)
    elif age > 10 and mFormat == "3D":
        print("The price of the movie is : $", (B_PRICE + (B_PRICE * SURCHARGE)))

    
        
