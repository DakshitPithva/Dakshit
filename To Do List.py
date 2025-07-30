# Making To Do List : 
to_Do_list =[]

def showmenu():
    print("Welcome TO TO Do List")
    print("Add Your Task")
    print("Remove Your Task")
    print("Save Your Task")
    print("View Your Task")

def add_task():
    task = str(input("Enter The Task"))
    to_Do_list.append(task)
    print("Your Task Is Entered")

def save_task():
    with open("task.txt","w") as file :
        for task in to_Do_list:
            file.write(task + "\n")
        print("Your Task Saved")

def view_task():

    if not  to_Do_list :
        print("\n No Task Yet")
    else:
        print("Here Your Task")
        for i,task in enumerate(to_Do_list,start=1):
            print(f"{i},{task}")

def remove_task():
    view_task()
    rem_num = int(input("Enter The Task Number To Remove "))
    remove = to_Do_list.pop(rem_num - 1)
    print(f"{remove} Task Has Removed.")

# Main Loop 
while True:
    showmenu()
    user = int(input("Choose The Number 1-4"))

    if user == 1:
        add_task()
    elif user == 2:
        remove_task()
    elif user == 3:
        save_task()
    elif user == 4:
        view_task()
    else:
        print("Entered Number Beetween 1 to 4")
     
 