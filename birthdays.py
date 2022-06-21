birthdays = {'Mireya': 'August 6th', 'Taylor': 'November 2nd', 'Trevor': 'January 17th', 'Ricardo': 'May 9th'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have the birthday information for ' + name)
        print('Do you know their birthday? Enter Yes or No')
        response = input()
        if response == 'Yes' or 'yes':
            print ('Please enter their birthday:')
            bday = input()
            birthdays[name] = bday
            print('Birthday database updated.')

        elif response == 'No' or 'no':
            print('Understood, would you like to search more information?')
            responseTwo = input()
            if responseTwo == 'Yes' or 'yes':
                continue
            
            elif responseTwo == 'No' or 'no':
                break