num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
num3 = input("Enter the third number: ")
if num1 > num2 and num3:
    print("The largest number is: ", num1)
elif num2 > num1 and num3:
    print ("The largest number is: ", num2)
else:
    print("The largest number is: ", num3)