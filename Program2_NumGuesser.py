from operator import ge
import random

#Generate 1 random number (0-100)
generated_number= random.randint(0,100)
print(generated_number)
#Ask the user to guess the number
while True:
 user_answer=int(input("can you guess the number? "))
#Display “Greater than” if the inputed number is greater than the random number


 if user_answer == generated_number:
    print("correct")
 else:
     if user_answer <= generated_number:
                print("your answer is less than the generated number")
     elif user_answer >= generated_number:
                print("your answer is greater than the generated number")
     if user_answer == generated_number:
                print("correct")
                break
#Display “Less than” if the inputed number is less than the random number
#Repeat asking the user until the random number has been guessed correctly