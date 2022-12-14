"""

The pre-defined minimum characters for the program is 8 characters.
The pre-defined maximum characters for the program is 20 characaters.

"""


#GET password
password = str(input("Please enter your intended password: \t"))
is_valid = True                         #SET Validity to TRUE
lowercase_password = password.lower()   #SET password to lowercase
print(lowercase_password)
if len(lowercase_password) < 8:         #IF password is LESS THAN 8 charcters
	is_valid = False                #SET validity to FALSE
	#SET reason
	reason = "Password length is too short"
elif len(lowercase_password) > 20:      #ELSE IF password is LONGER THAN 20
	is_valid = False                #SET validity to FALSE
	reason = "Password is too long" #SET reason
elif "umgc" in lowercase_password:      #ELSE IF paswword CONTAINS UMGC || umgc
	is_valid = False                #SET validity to FALSE
	#SET reason
	reason = "Password should not contain 'UMGC' or 'umgc'"  
elif "#" not in lowercase_password[1:-1]:   #ELSE IF password doesn't contain '#'
	is_valid = False                #SET validity to FALSE
	reason = "Password should contain '#' except in the first and last character"
        #SET reason
elif lowercase_password[0] == "#":      #ELSE IF password has '#' as FIRST character
	is_valid = False                #SET validity to FALSE
	#SET reason
	reason = "Password should not contain '#' in the first character"
elif lowercase_password[-1] == "#":     #ELSE IF password has '#' has last character
	is_valid = False                #SET validity to FALSE
	#SET reason
	reason = "Password should not contain '#' in the last character"
#END IF
if is_valid != True:                    #IF validity is FALSE
	print(reason)                   #PRINT reason
else:                                   #ELSE [validity is TRUE]
	print("Password is valid")      #PRINT password is valid
#ENDIF
