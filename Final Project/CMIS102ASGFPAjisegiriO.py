def bmiCALCULATION(height, weight):                             #FUNCTION to calculate the BMI
	##Calculating BMI using the formular: weight × 703 / height squared.
	bmi = round((weight * 703/(height ** 2)),2)
	return bmi                                              #RETURN BMI to MAIN FUNCTION
                                                                #END FUNCTION

def weightCATEGORIZATION(bmi):                                  #FUNCTION to Categorize BMI
	if bmi < 19:                                            #IF BMI < 19
		wCategory = "underweight"                               #SET WEIGHT CATEGORY to underweight
	elif bmi < 25:                                          #ELIF BMI < 25
		wCategory = "normalweight"                              #SET WEIGHT CATEGORY to normal weight
	elif bmi > 25:                                          #ELIF BMI > 25
		wCategory = "overweight"                                #SET WEIGHT CATEGORY to overweight
	#END IF	
	return wCategory                                        #RETURN WEIGHT CATEGORY to MAIN FUNCTION
                                                                #END FUNCTION


###  MAIN FUNCTION  ###
#DECLARE and DEFINE PARTICIPANTS ARRAY to pre-defined values
participants = [{"name": "Garry Allen", "height": 0, "weight": 0},{"name": "Lola Parlour", "height": 0, "weight": 0},{"name": "Mary Barlow", "height": 0, "weight": 0},{"name": "Joshua Strong", "height": 0, "weight": 0},{"name": "Alexander Bryant", "height": 0, "weight": 0},{"name": "Cornelius Vanderbilt", "height": 0, "weight": 0}]
participants_bmi = []                                           #DECLARE and DEFINE BMI ARRAY to an empty array
for n in range(len(participants)):                              #FOR EACH PARTICIPANT
        #GET PARTICIPANT's HEIGHT
	participants[n]["height"] = eval(input("Please, how tall is {} in inches:\t".format(participants[n]["name"])))
	#GET PARTICIPANT's WEIGHT
	participants[n]["weight"] = eval(input("Please, enter {}'s weight in lbs:\t".format(participants[n]["name"])))
	#SET BMI to FUNCTION to CALCULATE BMI
	bmi = bmiCALCULATION(participants[n]["height"],participants[n]["weight"])       
	participants_bmi.insert(n, bmi)                         #INSERT PARTICIPANT's BMI into BMI ARRAY
	print("{0} is {1}ft tall, weighs {2}lbs and has a body mass index of {3} \n".format(participants[n]["name"], round(participants[n]["height"]/12,2), participants[n]["weight"], bmi))
#END FOR 
underWeight_count = normalWeight_count = overWeight_count = 0   #DECLARE and DEFINE COUNTERS to 0
for g in range(len(participants)):                              #FOR EACH BMI in the BMI ARRAY
	category = weightCATEGORIZATION(participants_bmi[g])    #SET CATEGORY to WEIGHT CATEGORY from FUNCTION
	if category == "underweight":                           #IF CATEGORY EQUALS "underweight"
		underWeight_count += 1                                  #INCREMENT UNDERWEIGHT COUNTER
	elif category == "normalweight":                        #ELIF CATEGORY EQUAL "normalweight"
		normalWeight_count += 1                                 #INCREMENT NORMALWEIGHT COUNTER
	elif category == "overweight":                          #ELIF CATEGORY EQUAL "overweight"
		overWeight_count += 1			                #INCREMENT OVERWEIGHT COUNTER
	#END IF
#END FOR
print(participants)                                             #PRINT PARTICIPANTS
print("\n")
#PRINT COUNTERS
print("The number of people in the list that are underweight are(is): ",underWeight_count)
print("The number of people in the list that are of normal bodyweight are(is): ",normalWeight_count)
print("The number of people in the list that are overweight are(is): ",overWeight_count)
###  END MAIN FUNCTION  ###
