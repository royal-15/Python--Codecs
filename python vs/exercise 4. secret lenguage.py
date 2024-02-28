import random as r

code = input("-:Enter your code:-\n")
words = code.split(" ")
operation = int(input("Enter 1 for coding or 0 for decoding: "))

# if (operation != 1):
#     raise ValueError("must enter 0 or 1")

operation = True if(operation == 1) else False

# print(operation)

l = "abcdefghijklmnopqrstuvwxyz"

if (operation):
    nwords = []
    for word in words:
        if (len(word) >= 3):
            newcode = r.choice(l)+r.choice(l)+r.choice(l)+word[1:]+word[0]+r.choice(l)+r.choice(l)+r.choice(l)
            nwords.append(newcode)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
else:
    nwords = []
    for word in words:
        if (len(word) >= 3):
            newcode = word[3:-3]
            newcode = newcode[-1] + newcode[:-1]
            nwords.append(newcode)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))