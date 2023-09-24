input_number = 0
sum = 0
count = 0
average = 0
while True:
    input_number = (input("> "))
    #if input_number[0] == "done":
    #    print("Dont write done at the first input")
    #    continue 
    if input_number.lower() == "done":
        break
    try:
        number = float(input_number)
        sum = sum + number
        count = count + 1
    except:
        print('Enter a number or "done" to end')
    if count == 0:
        print("You cannot proceed")
        break
    average = sum / count
print("The sum of the numbers is ",sum)
print("The average of the sum of the numbers is ",average)
print("The count of the numbers is ",count)