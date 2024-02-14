import random


money = 0
health = 100

print("All commands:\n- rob\n- status\n- buy")

while True:

    if health < 25 and health > 10:
        print("You are low on health. Consider buying a medkit.")
    elif health <= 10 and health > 0:
        print("You are critical injured. Medkit is crucial!")
    elif health < 1:
        print("You died. Game over!")
        print(f"Here is your final statistic:\nHealth: {health}\nMoney: {money}")
        quit(0)

    risk_of_injury = random.randint(0, 10)
    money_stolen = random.randint(0,100)
    your_chance = random.randint(0, 100)
    user_input = input("> ")
    user_input = user_input.lower()

    if user_input == "rob":
        if your_chance >= 75:
            print("You've tackled a person down and ran off with %d kr" % money_stolen)
            money += money_stolen
        elif your_chance < 75 and your_chance >= 50:
            print("The person has no money, so you ran off before the police arrive")
        elif your_chance < 50:
            print("The person you tried to rob is armed with a knife. You've managed to escape, but injured. Your health is decreased by %d." % risk_of_injury)
            health -= risk_of_injury
    elif user_input == "status":
        print(f"Money: {money}\nHealth: {health}")

    elif user_input == "buy":
        print("\nWelcome to the ghetto black market for criminals! What brings you here?\n- medkit = 75 kr\n- Ticket = 500 kr\n- Leave")
        while True:
            user_buy_input = input("> ")
            user_buy_input = user_buy_input.lower()
            if user_buy_input == "medkit" and money >= 75:
                healing = random.randint(0,5)
                print("You bought a medkit and healed yourself up to", health)
                health += healing
                money -= 75

            elif user_buy_input == "ticket" and money > 499:
                print("You escaped from the country. You won the game.")
                quit(0)
            elif user_buy_input == "leave":
                print("you left the store.")
                break

            elif (user_buy_input == "medkit" and money < 75) or (user_buy_input == "ticket" and money < 499):
                print("You're poor!")



            else:
                print("Unknown command for buy:", user_buy_input)

    else:
        print("Unknown command:", user_input)
    
