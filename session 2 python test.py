# This program asks you for your name and password.

print('Hello World!') 
print('What is your name?') #name 
name = input()

if name == "Mary":
    print('Hello, Mary!')
else:
    print('Hey, stranger')

print('It is good to meet you, ' + name + '.')

print('What is your password?') #password

password = input()

if password == 'swordfish':
    print('I see you know the code.')
    print('Now then, what is your age?')

    age = input()
    age = int(age)

    if age < 18:
        print('Huh. A child, then.')
    elif age > 120:
        print('I highly doubt that.')
    elif age == 24:
        print('Samesies.')

    else:
        print("Understood. Let's begin then.")

else:
    print('You do not know the way.')

print('Goodbye.')