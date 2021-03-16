print("Enter number: ")
try:
    user_number = int(input())
except ValueError:
    print("You must enter an integer!")


def collatz(number):
    while number != 1:
        if number % 2 == 0:
            number = (number // 2)
            return print(int(number))

        elif number % 2 == 1:
            number = (3 * number + 1)
            return print(int(number))

        continue


collatz(number=user_number)
