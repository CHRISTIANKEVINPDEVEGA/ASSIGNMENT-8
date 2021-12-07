import random

while True:
 def User_Input():
  print("Give 3 numbers ranging from 0-9.")
  Number_1=int(input("Enter your first number: "))
  Number_2=int(input("Enter your second number: "))
  Number_3=int(input("Enter your third number: "))
  return Number_1, Number_2, Number_3
 
 def lottery_system(N_1, N_2, N_3):
  user_number = N_1, N_2, N_3
  winning_num1= random.randint(0,9)
  winning_num2= random.randint(0,9)
  winning_num3= random.randint(0,9)
  winning_numbers= winning_num1, winning_num2, winning_num3
  print(f"winning numbers: {winning_numbers}")
  if set(winning_numbers) == set(user_number):
    print("Winner")
  else:
    print("You lost")    
  
 Num1, Num2, Num3=User_Input()
 lottery_system(Num1, Num2, Num3)
 
 choice = input("do you want to try again? y/n ")
 if choice == "y":
  continue
 elif choice == "n":
  break


