from colorama import Fore, Back, Style
import random


playing = True  #Global Variables
score = {}
cont = "yes"
choices = {
  1: "ROCK",
  2: "PAPER",
  3: "SCISSORS"
}

print(Fore.RED + "Welcome to Rock Paper Scissors!")    #Gameplay Instructions
print(Fore.BLUE + "Choices: \n1. Rock\n2. Paper\n3. Scissors")

print(Fore.YELLOW)
turns = input("Enter the amount of rounds your would like to play (Maximum rounds is 15): ")   #Input Turns
print("\n")

while (turns != "1" and turns != "2" and turns != "3"and turns != "4"and turns != "5"and turns != "6"and turns != "7" and turns != "8" and turns != "9" and turns != "10" and turns != "11" and turns != "12" and turns != "13" and turns != "14" and turns != "15"):   #Input Validation
  print(Fore.RED + "You provided something invalid.")
  print(Fore.YELLOW)
  turns = input("Enter the amount of rounds your would like to play (Maximum rounds is 15): ") 
  print("\n")
turns = int(turns)

def game_Cycle(best_of, p1, p2):    #Main Engine
  trials = 0
  points = {  #Dictionary For Point Storage
    "p1_points": p1,  
    "p2_points": p2
  }

  while trials < best_of: #All Conditionals
    player_choice = input(Fore.BLUE + "Enter your choice (Rock/Paper/Scissors): ")  #Choice Input
    comp_choice = choices[random.randint(1, 3)]

    if comp_choice == player_choice.upper():
      print(f"{Fore.WHITE}Both players chose {player_choice.lower()} resulting in a tie.\nNo points are awarded.")
      trials += 1

    elif (comp_choice == "ROCK") and (player_choice.upper() =="PAPER"):
      print(f"{Fore.GREEN}You chose {player_choice.lower()} while player 2 chose {comp_choice.lower()}.\nYou are awarded 1 point.")
      points["p1_points"] += 1
      trials += 1

    elif (comp_choice == "PAPER") and (player_choice.upper() =="ROCK"):
      print(f"{Fore.RED}You chose {player_choice.lower()} while player 2 chose {comp_choice.lower()}.\nPlayer 2 is awarded 1 point.")
      points["p2_points"] += 1
      trials += 1

    elif (comp_choice == "SCISSORS") and (player_choice.upper() =="ROCK"):
      print(f"{Fore.GREEN}You chose {player_choice.lower()} while player 2 chose {comp_choice.lower()}.\nYou are awarded 1 point.")
      points["p1_points"] += 1
      trials += 1
    
    elif (comp_choice == "ROCK") and (player_choice.upper() =="SCISSORS"):
      print(f"{Fore.RED}You chose {player_choice.lower()} while player 2 chose {comp_choice.lower()}.\nPlayer 2 is awarded 1 point.")
      points["p2_points"] += 1
      trials += 1

    elif (comp_choice == "PAPER") and (player_choice.upper() =="SCISSORS"):
      print(f"{Fore.RED}You chose {player_choice.lower()} while player 2 chose {comp_choice.lower()}.\nYou are awarded 1 point.")
      points["p1_points"] += 1
      trials += 1
    
    elif (comp_choice == "SCISSORS") and (player_choice.upper() =="PAPER"):
      print(f"{Fore.RED}You chose {player_choice.lower()} while player 2 chose {comp_choice.lower()}.\nPlayer 2 is awarded 1 point.")
      points["p2_points"] += 1
      trials += 1
    
    else:  #Input Validation
      print(f"{Fore.RED}Your current choice, {player_choice}, is not one of the 3 given choices.\nTry again.")
    
    print("\n")
  return points  #Return Point Dictionary
 

while cont.upper() == "YES":   #Execution of Engine
  score = game_Cycle(turns, 0, 0) 
  if score["p1_points"] > score["p2_points"]:
    print(f"{Fore.GREEN}You win the game with {score['p1_points']} point(s)! Player 2 had {score['p2_points']} point(s).")

  elif score["p2_points"] > score["p1_points"]:
    print(f"{Fore.RED}You lose the game with {score['p1_points']} point(s). Player 2 had {score['p2_points']} point(s).")

  else:
    print(f"{Fore.WHITE}Both players tie the game with {score['p1_points']} point(s)!?")

  cont = input(f"{Fore.BLUE}Would you like to play again? (Yes/No): ")   #Game Continuation Input
  print("\n")

  if cont.upper() == "YES":   
    print(Fore.YELLOW)
    turns = input("Enter the amount of rounds your would like to play (Maximum rounds is 15): ")   #Input Turns
    print("\n")
    while (turns != "1" and turns != "2" and turns != "3"and turns != "4"and turns != "5"and turns != "6"and turns != "7" and turns != "8" and turns != "9" and turns != "10" and turns != "11" and turns != "12" and turns != "13" and turns != "14" and turns != "15"):   #Input Validation
      print(f"{Fore.RED}You provided an invalid number.")
      print(Fore.YELLOW)
      turns = input("Enter the amount of rounds your would like to play (Maximum rounds is 15): ") 
      print("\n")
    turns = int(turns)
      
print("\n")
print(f"{Fore.GREEN}Thanks for playing!")
playing = False