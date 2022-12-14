"""
Cold Day < 45 F
45F > Cool Day < 60F
60F > Warm Day < 76F
76F > Hot Day 
"""
def calculatingFarenheit(temp_arr):         #FUNCTION to calculate FARENHEIT
    for tempF in range(len(temp_arr)):      #FOR EACH temperature in the TEMPERATURE ARRAY
        temp_farenheit = round((temp_arr[tempF] * 1.8) + 32,0)  #CALCULATING FARENHEIT equivalent TEMPERATURE
        temp_arr.pop(tempF)                 #REMOVE the CELSIUS TEMPERATURE
        temp_arr.insert(tempF, temp_farenheit)  #INSERT the FARENHEIT temperature
    #END FOR
    return temp_arr                         #RETURN the FARENHEIT TEMPERATURE ARRAY to the MAIN FUNCTION
                                            #END FUNCTION
    
def counter(tempFarenheit_arr):             #FUNCTION to count cool, warm and hot days 
    global coldDays_counter                 #GLOBAL COLD day counter
    global coolDays_counter                 #GLOBAL COOL day counter
    global warmDays_counter                 #GLOBAL WARM day counter
    global hotDays_counter                  #GLOBAL HOT day counter
    for tempF in range(len(tempFarenheit_arr)):     #FOR EACH TEMPERATURE in the ARRAY
        if tempFarenheit_arr[tempF] < 45:               #IF TEMPERATURE is < 45
            coldDays_counter += 1                           #INCREMENT COLD day COUNTER
        elif tempFarenheit_arr[tempF] < 60:             #IF TEMPERATURE is < 60
            coolDays_counter += 1                           #INCREMENT COOL day COUNTER
        elif tempFarenheit_arr[tempF] < 76:             #IF TEMPERATURE is < 76
            warmDays_counter += 1                           #INCREMENT WARM day COUNTER
        else:                                           #ELSE [TEMPERATURE is > 76]
            hotDays_counter += 1                            #INCREMENT HOT day COUNTER
        #END IF
    #END FOR
    #PRINT the counted days
    print("There were ", coldDays_counter," cold days in the last ten days")
    print("There were ", coolDays_counter," cool days in the last ten days")
    print("There were ", warmDays_counter," warm days in the last ten days")
    print("There were ", hotDays_counter," hot days in the last ten days")
                                            #END FUNCTION
    
#MAIN FUNCTION
###   DECLARE AND DEFINE VARIABLES    ###
tempratures = []        #Temperature array     
coldDays_counter = 0    #Cold days counter
coolDays_counter = 0    #Cool days counter
warmDays_counter = 0    #Warm days counter
hotDays_counter = 0     #Hot days counter
#PROMPT the user to enter the temperatures of the last 10 consecutive days based on prompts
print("Enter the temprature of the last ten consecutive days in Celsius using the prompts below.")
for temp in range(10):	                                            #FOR EACH of the inputted temprature
    temperature = eval(input("Enter temperature in Celsius: \t"))   #PROMPT user to input temperature
    tempratures.append(temperature)                                 #POPULATE the temperature array
#END FOR
print("The temperatures for the last 10 consective days in Celsius are: ",tempratures)      #PRINT TEMPERATURE ARRAY
temp_farenheit = calculatingFarenheit(tempratures)                  #Call FUNCTION to calculate FARENHEIT degree AND SAVE RETURN VALUE
print("The temperatures for the last 10 consective days in Farenheit are: ",temp_farenheit) #PRINT the FARENHEIT TEMPERATURE ARRAy
counter(temp_farenheit)                                             #Call FUNCTION to count cool, warm and hot days
#END MAIN FUNCTION
