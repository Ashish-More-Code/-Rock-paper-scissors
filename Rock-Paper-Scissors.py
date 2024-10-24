import random
comp_list=["Rock","Paper","Scissor"]
computer_action=random.choice(comp_list)
print("""
Enter your choice!
1: Rock
2: Scissor
3: Paper
""")
uch=int(input("Enter the choice(1/2/3)"))
u={1:"Rock",2:"Scissor",3:"Paper"}
map_user_action=u[uch]
if computer_action== map_user_action:
    print("Its Tie!")
elif map_user_action=="Rock":
    if computer_action=="Paper":
        print("you lose!")
    else:
        print("you win")
elif map_user_action=="Paper":
    if computer_action=="Scissor":
        print("you lose!")
    else:
        print("you win")
elif map_user_action=="Scissor":
    if computer_action=="Rock":
        print("you lose!")
    else:
        print("you win")
print(computer_action)
