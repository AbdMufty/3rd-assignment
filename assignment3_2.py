grade = "null"
try:
    score = float(input("Enter your score to evaluate grades\n==>"))
    if score < 0 or score > 100:
        print("Enter valid score from 0 to 100")
    else:
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"
except:
    print("Enter a numeric value from 0 to 100")
print("Your grade is ",grade)