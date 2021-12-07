import random

generated_number= random.randint(0,100)
#print(generated_number)
user_answer=int(input("Guess a number from 0-100 that the program will generate.\n"))
while generated_number != user_answer:
   if user_answer < generated_number:
      print("your answer is less than the generated number")
      user_answer=int(input("Please guess again.\n"))
   elif user_answer > generated_number:
      print("your answer is greater than the generated number")
      user_answer=int(input("Please guess again.\n"))
if generated_number == user_answer:
   print("That is correct, WOW amazing!")