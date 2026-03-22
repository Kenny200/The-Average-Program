# 5/20/2025
def calculateAverage():
    total = 0
    count = 0
    print("Welcome to my average calcualtion program")
    print("Please enter as many numbers as you would like")
    print("Enter stop, quit, s, or q to stop entering numbers")

    while True:
        user = input("Enter an integer: ")

        if user.lower() == 'stop' or user.lower() == 'quit' or user.lower() == 'q' or user.lower() == 's':
            break

        try:
            number = float(user)
            if number.isdigit():
                total += number
                count += 1
            else:
                print(f"{user} is not an valid digit.")
        except ValueError:
            print(f"{user} is not an numberr.")

    if count > 0:
        average = total / count
        print(f"Average of the {count} integers is: {average}")
        return average
    else:
        print("No valid integers were entered.")
        return 0
    
print(calculateAverage())
