import random
mark = 0


def simple_math():
    global mark
    counter = 0
    while counter < 5:
        result = ""
        operations = ["+", "-", "*"]
        operation = random.choice(operations)
        first_number = random.randint(2, 9)
        second_number = random.randint(2, 9)
        if operation == "+":
            result = first_number + second_number
        elif operation == "-":
            result = first_number - second_number
        elif operation == "*":
            result = first_number * second_number
        print(str(first_number) + " " + operation + " " + str(second_number))
        while True:
            try:
                user_result = int(input())
            except ValueError:
                print("Incorrect format.")
            else:
                break
        if int(user_result) == result:
            print("Right!")
            mark += 1
        else:
            print("Wrong!")
        counter += 1
    print(f"Your mark is {str(mark)}/5. Would you like to save the result?")


def advanced_math():
    global mark
    counter = 0
    while counter < 5:
        number = random.randint(11, 29)
        result = number * number
        print(number)
        while True:
            try:
                user_result = int(input())
            except ValueError:
                print("Incorrect format.")
            else:
                break
        if int(user_result) == result:
            print("Right!")
            mark += 1
        else:
            print("Wrong!")
        counter += 1
    print(f"Your mark is {str(mark)}/5. Would you like to save the result")

while True:
    print("Which level do you want? Enter a number:")
    print("1 - simple operations with numbers 2-9")
    print("2 - integral squares of 11-29")
    first_input = input()
    if first_input == "1":
        simple_math()
        description = "simple operations with numbers 2-9"
        break
    elif first_input == "2":
        advanced_math()
        description = "integral squares of 11-29"
        break
    else:
        print("Incorrect format.")

print("Enter yes or no.")
user_input = input()
yes = ["yes", "YES", "y", "Yes"]

if user_input in yes:
    name = input("What is your name?")
    file = open("results.txt", mode="a")
    file.write(f"{name}: {mark}/5 in level {first_input} ({description}).")
    file.close()
    print("The results are saved in \"results.txt\".")
