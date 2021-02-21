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
    # write your code here
    pass
            
guess_number()

import random
def guess_number():
    # write your code here
    rand_number = random.randrange(0, 101)
    input_number = input("Enter a number: ")
    while (input_number.isnumeric()==False or int(input_number)!=rand_number):
        if int(input_number)<rand_number:
            print ("Too small.")
        else:
            print ("Too big.")
        input_number = input("Enter another number: ")
    else:
        print ("Congratulations!")

guess_number()
