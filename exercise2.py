import random

# write a function to ask user to type a number.
# 1. this function should generate a random number between 0 and 100
# 2. it should save the number that user typed and check if the number is a real number. 
#    2.1 if the number is not a valid number
#        it should tell user that the number is illegal and ask user to type again
# 3. if the number is valid then compare the number with the generated random number
#    give user hint whether it is too small or too big and ask user to try again
# 4. if the the number is equal to the generated random number, print congratulations 
#    and end the function 
 
def guess_number():
    expected = random.randint(0,100)
    print("welcome to Number Guessing")
    guessed = input("Please type a number between 0 and 100: ").strip()
    while True:
        if len(guessed)==0 or not guessed.isnumeric():
            guessed = input("{} is not a number, try again: ".format(guessed)).strip()
            continue
        elif int(guessed) < expected:
            guessed = input("{} is too small, try again: ".format(guessed)).strip()
            continue
        elif int(guessed) > expected:
            guessed = input("{} is too big, try again: ".format(guessed)).strip()
            continue 
        else: 
            print("You got it, the number is {}, congratulations!!!".format(expected))
            break
            
guess_number()

