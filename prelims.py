#FERRER, MARION CARYL R.
#3ITD
#ELEC2C PRELIMS LAB

import sys


def login():
    attempts = 0

    while True: 
        userName = input("Username: ") 
        password = input("Password: ")
        attempts += 1

        #Successful Login
        if userName == 'IT ELE2C' and password == 'P83Lim_3xAm':
            print('\nWelcome.')

            #2nd condition start
            try:
                while True:
                    string = input('Enter a word: ')
                    

                    if string.isalpha():
                        lower = [ ]
                        upper = [ ]
                       
                        for i in range(0, len(string)):

                            ch = string[i]

                            #Transform upper to lower case
                            ch = ch.lower()

                            #Sort vowels from consonants
                            if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
                                lower.append(ch)
                            else:
                                upper.append(ch)

                        #Puts a space between vowels
                        #and dash between consonants
                        #then join them together
                        output = ' '.join(" ".join(lower) + "-".join(upper))
                        print(output)
                        break
                    else:
                        print('Enter letters only.\n')                            
                
            except Exception as e:
                print(e)
                
            break

        else:
            if attempts == 3:
                print('Account locked.')
                break
            else:
                print('Wrong username or password. Try again. \n')

login()


while True:
    try_again = input('\nTry again? (Y/N): ')
    
    if try_again == 'Y':
        login()
    elif try_again == 'N':
        print('Made by: Ferrer, Marion Caryl R. | 3ITD')
        sys.exit()
    else:
        try_again
