import random

def generator():
 generated_NUMBER= random.randint(0,100)
 #print(generated_number)
 return generated_NUMBER

def guess_checker(generated_number):
 user_answer=int(input("Guessing game!!!\nGuess the number that the program generated ranging from 0-100.\n"))
 while generated_number != user_answer:
   if user_answer < generated_number:
      print("your answer is less than the generated number")
      user_answer=int(input("Please guess again.\n"))
   elif user_answer > generated_number:
      print("your answer is greater than the generated number")
      user_answer=int(input("Please guess again.\n"))
 if generated_number == user_answer:
   print("That is correct, WOW amazing! I'm impressed.")

generated_num=generator()
guess_checker(generated_num)   