nric = input('Enter an NRIC number: ')

# Type your code below
nric = nric.lower()
checks = [
    nric[0] in "stfg", #first letter must be one of 4 letts
    nric[1:8].isdigit(), # 7 numerical digits
    len(nric) == 9 and nric[8].isalpha() # last char is a letter
]

if all(checks):
    weights = [2, 7, 6, 5, 4, 3, 2]
    digits = nric[1:8]
    conversion = {
        "s": "jzihgfedcba",
        "t": "jzihgfedcba",
        "f": "xwutrqpnmlk",
        "g": "xwutrqpnmlk",
    }
    total = 0
    for index in range(len(weights)):
        total = total + int(digits[index])*weights[index]
    total = total + (nric[0] in "tg")*4

    if conversion[nric[0]][total%11] == nric[-1]:
        print("NRIC is valid.")
    else:
        print("NRIC is invalid.")
else:
    print("NRIC is invalid.")