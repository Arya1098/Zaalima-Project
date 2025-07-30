a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

temp = a
a = b
b = temp

print("After swapping (using third variable):")
print("a =", a)
print("b =", b)