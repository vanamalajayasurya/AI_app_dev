num = int(input("enter the number"))

if (num < 0 ):
    print("correct is number")
elif (num > 0):
    if (num <= 10):
        print("number between 1-10")
    elif(num > 10 and num <= 30):
        print("numbers between 11 - 20 ")
    else:
        print("number is greter than 20")
else:
    print("number is zero")        

                   