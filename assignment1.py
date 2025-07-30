num = input("Enter a 4-digit number:")

if len(num) == 4 and num.isdigit():
    reversed_num = num[::-1]
    print("Reversed number:", reversed_num)
else:
    print("Invalid input. Please enter a 4-digit number.")