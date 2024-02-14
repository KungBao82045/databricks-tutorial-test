# Databricks notebook source
import random

# Players List
players = ['Player 1', 'Player 2', 'Player 3', 'Player 4', 'Player 5']

# Roles List
roles = ['Mafia', 'Citizen', 'Citizen', 'Citizen', 'Doctor']

# Shuffle roles
random.shuffle(roles)

# Assign roles to players
players_roles = dict(zip(players, roles))

# Game Loop
game_over = False
while not game_over:
    # Night phase (Mafia chooses player to kill)
    mafia_player = input("Mafia, choose a player to kill: ")
    if mafia_player in players:
        players.remove(mafia_player)
        del players_roles[mafia_player]
    else:
        print("Invalid player.")
        continue
    
    # Doctor phase (Doctor chooses player to save)
    doctor_player = input("Doctor, choose a player to save: ")
    if doctor_player in players:
        players.append(doctor_player)
        players_roles[doctor_player] = 'Doctor'
    else:
        print("Invalid player.")
        continue
    
    # Check if Mafia wins
    if 'Mafia' not in players_roles.values():
        print("Mafia has won!")
        game_over = True
    
    # Day phase (Players vote to eliminate a player)
    print("Day phase")
    print("Players: ", players)
    eliminate_player = input("Choose a player to eliminate: ")
    if eliminate_player in players:
        players.remove(eliminate_player)
        del players_roles[eliminate_player]
    else:
        print("Invalid player.")
        continue
    
    # Check if Citizens win
    if 'Mafia' in players_roles.values() and len(set(players_roles.values())) == 1:
        print("Citizens have won!")
        game_over = True


# COMMAND ----------

num1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2
else:
    result = "Invalid operator"

print("The result is:", result)


# COMMAND ----------


