import random
while True:
#Create a program that ask 3 numbers (0-9) from the user.
 Number_1=int(input("Enter your first number: "))
 Number_2=int(input("Enter your second number: "))
 Number_3=int(input("Enter your third number: "))
 your_number = Number_1, Number_2, Number_3

#Generate 3 random winning numbers (0-9)
 winning_num1= random.randint(0,99)
 winning_num2= random.randint(0,99)
 winning_num3= random.randint(0,99)
 winning_numbers= winning_num1, winning_num2, winning_num3
 print(f"winning numbers: {winning_numbers}")

#Display “Winner” if all 3 input numbers matched the generated numbers
 if winning_numbers == your_number:
    print("win")
 else:
    print("lost")    
#Display ”You loss” if not
#Display ”Try again y/n” after each game
 choice=input("do you want to try again? y/n ")
 if choice == "y":
  continue
 elif choice == "n":
  break
#If the user enter “y” the user will play again
#if “n” the program will exit.

