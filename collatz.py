# Collatz sequence

def Collatz(number):

    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 == 1:
        print(3 * number + 1)
        return 3 * number + 1

while True:         # creating a loop in case there are any errors
    print('Please enter a number.')      
    try:                                 
        number = input()
        number = int(number)
        while number >= 2:              # if 1 or under, it will finish
            number = Collatz(number)
    except ValueError:
        print('Please make sure to enter a number.')
        continue
    break