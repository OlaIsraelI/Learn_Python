import random

def get_choices():

  valid_choice = ["rock", "paper", "scissors"]

  while True:
    user_choice = input("Enter a choice (Rock, Paper, Scissors: )").strip().lower()

    if user_choice in valid_choice:
      break
    
    print("Invalid choice, Enter only Rock, Paper, Scissors: ")

  options = ["rock", "paper", "scissors"]
  computer_choice = random.choices(options)

  choices = {"player": user_choice, "computer": computer_choice}

  return choices

def check_win(player, computer):
  print(f"you chose {player}, computer chose {computer}")
  if player == computer:
    return "It's a tie!"
  
  elif player == "rock":
    if computer == "scissors":
      return "Rock smashes scissors! You win!"
    else:
      return "paper covers rock, You lose."

  elif player == "paper":
    if computer == "Rock":
      return "paper covers Rock! You win!"
    else:
      return "scissors cuts paper!, You lose."

  elif player == "scissors":
    if computer == "paper":
      return "scissors cuts paper! You win!"
    else:
      return "rock smashes scissors."


choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)