import random


from art import logo
from art import vs
from game_data import data

#PRINT THE LOGO
#CHOOSE RANDOM ACCOUNTS FROM THE GIVEN DATA LIST OF ACCOUNTS
#PRINT THE ACCOUNTS SELECTED IN PRINTABLE FORM
#CALCULATE THE FOLLOWERS OF ACCOUNTS TO COMPARE THE ACCOUNTS ON THE BASIS OF HEIR FOLLOWERS
#ASK THE USER TO GUESS TO WHICH HAVE MORE FOLLOWERS
#CHECK IF USER GUESS IS RIGHT
#CALCULATE USER SCORE IF ANSWER IS RIGHT

def format_acc(accounts):
 account_name = accounts["name"]
 account_description = accounts["description"]
 account_country = accounts["country"]
 return f"{account_name} a {account_description} from {account_country}."

def check(guess, a_followers, b_followers):
 if a_followers > b_followers:
  return guess == "A"
 elif a_followers < b_followers:
  return guess == "B"


score = 0
account_b = random.choice(data)
print(logo)

should_continue = True
while should_continue:

 account_a = account_b
 account_b = random.choice(data)
 if account_a == account_b:
  account_b = random.choice(data)
 print(logo)
 print(f"Compare A: {format_acc(account_a)}")
 print(vs)
 print(f"Against B: {format_acc(account_b)}")

 guess = input("Who has more followers? Choose 'A' or 'B'. ")

 print("\n" *10)

 account_a_followers = account_a["follower_count"]
 account_b_followers = account_b["follower_count"]

 is_correct = check(guess, account_a_followers, account_b_followers)

 if is_correct:
  score += 1
  print(f"You are right, Final score {score}")
 else:
  print("Oops You got the wrong answer.")
  should_continue = False