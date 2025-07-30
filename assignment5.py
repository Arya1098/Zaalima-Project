add = lambda a, b: a + b
print("Addition (5 + 3):", add(5, 3))

mul = lambda a, b: a * b
print("Multiplication (4 × 6):", mul(4, 6))

power = lambda x, y=2: x ** y
print("Power default (5²):", power(5))

average = lambda *nums: sum(nums) / len(nums)
print("Average of (2, 4, 6):", average(2, 4, 6))

greet = lambda who="Guest": f"Hi, {who}!"
print(greet())
print(greet("Arya"))