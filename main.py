import random
'''
1 = Rock 
-1 = Paper
0 = Scissors
'''

# This is funcation to Who Computer Choose and We Choose!

computer = random.choice([-1,0,1])
you_choice = int(input("Enter Your Choice :"))
you_dict = {1:"Rock",-1:"Paper",0:"Scissors"}
computer_dict ={1:"Rock",-1:"Paper",0:"Scissors"}
youstr = you_dict[you_choice]

print(f"Computer Choose:{computer_dict[computer]}\n You Choose:{you_dict[you_choice]}") # Print What Computer Choose and You choose

# There are Condition to Who Win the Match 
if(computer == 1 and you_choice == 1):
    print("Match Was Deaw!")
else:
    if(computer == 1 and you_choice == -1):
        print("You Win The Match!")
    elif(computer == -1 and you_choice == 1):
        print("You Loss The Match!")
    
    elif(computer == 1 and you_choice == 0):
        print("You Loss The Match!")
    elif(computer == 0 and you_choice == 1):
        print("You Win The Match!")

    elif(computer == 0 and you_choice == -1):
        print("You Loss The Match!")
    elif(computer == -1 and you_choice == 0):
        print("You Win The Match!")
    
    else:
        print("Something Went To Wrong!")


