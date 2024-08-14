print("Enter a strong password.\nA strong pssword shold contain at least 8 charaters, a number, a uper case letter and a special character")

password = input("Enter your password: ")

result = {}

# checking the length 
if len(password) > 8:
    result["length"] = True
else:
    result["length"] = False

# checking if the password contains a number
for i, chr in enumerate(password):
    if chr.isdigit():
        result["Number"] = True
        break
    else:
        if chr == password[-1] and i+1 == len(password):
            result["Number"]= False
        continue

# checking if the password contains a uper case letter
uppercase = False
for i in password:
    if i.isupper():
        uppercase = True
    
result["Uppercase"] = uppercase

# check for special characters
special_chr = any(not i.isalnum() for i in password)

result["Special character"] = special_chr

if all(result.values()):
    print ("Your have entered a strong password")
else:
    print("Your password doesn't match all the conditions.\nYou have entered a week password.")