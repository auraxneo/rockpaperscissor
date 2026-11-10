import random

rock='''[[[]]]'''
paper='''||||'''
scissors='''><><><><><><><><><><>'''
input_value = input("choose. type 0 for rock, 1 for paper, 2 for scissors:\n")
if input_value == "0":
    print("You chose rock:")
    print(rock)
elif input_value == "1":
    print("You chose paper:")
    print(paper)
elif input_value == "2":
    print("You chose scissors:")
    print(scissors)
print("computer choice:")
print(random.choice([rock, paper, scissors]))
if input_value == "0" and random.choice([rock, paper, scissors])==rock:
    print("draw")
elif input_value == "0" and random.choice([rock, paper, scissors])==paper:
    print("you lose")
elif input_value == "0" and random.choice([rock, paper, scissors])==scissors:
    print("you win")
elif input_value == "1" and random.choice([rock, paper, scissors])==rock:
    print("you win")
elif input_value == "1" and random.choice([rock, paper, scissors])==paper:
    print("draw")
elif input_value == "1" and random.choice([rock, paper, scissors])==scissors:
    print("you lose")
elif input_value == "2" and random.choice([rock, paper, scissors])==rock:
    print("you lose")
elif input_value == "2" and random.choice([rock, paper, scissors])==paper:
    print("you win")
elif input_value == "2" and random.choice([rock, paper, scissors])==scissors:
    print("draw")
