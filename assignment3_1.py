
while True:
    try:
        hour = int(input("Enter the employment hours: "))
    except:
        print("\nEnter a correct value for hours (only integer)")
        break
    try:
        rate = float(input("Enter the rate per hour: "))
    except:
        print("\nEnter a correct value for payment rate (only float)")
        break
    total_salary = hour * rate
    if hour <= 40:
        print("Salary is ",total_salary)
    elif hour > 40:
        extra_hour = hour - 40
        salary_over_time = (rate * 1.5) * extra_hour
        salary =  salary_over_time + total_salary - (extra_hour * rate)
        print ("After doing", extra_hour, "hours overtime, total salary is ",salary)
        break