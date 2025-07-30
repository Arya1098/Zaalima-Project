def calculate_grade(score, bonus):
    final_grade = score + bonus
    if final_grade >= 60:
        print("Passed")
    else:
        print("Failed")
    return final_grade

result = calculate_grade(45, 10)
print("Final Grade:", result)