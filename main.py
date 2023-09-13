

to_do_list=[]

# Function that adds input received from the user to the list
def add_task(to_do_list):
    task=input("enter the task to be done")
    to_do_list.append(task)
    print("task added successfully")



# Function that shows the tasks in the list
def show_tasks(to_do_list):
    print("tasks to be done")
    for task in to_do_list:
        print(" -" + task)


def delete_task(to_do_list):
    task=input("Enter the task you want to delete:")
    if task in to_do_list:
        to_do_list.remove(task)
        print("The task has been deleted successfully")
    else:
        print("Task not found")

while True:
    print("\n To-Do List App" )
    print("1. add task")
    print("2.Show Tasks ")
    print("3.Delete Task ")
    print("4.Exit")
    choice = input("Your choice (1/2/3/4): ")

    if choice == "1":
        add_task(to_do_list)
    elif choice == "2":
        show_tasks(to_do_list)
    elif choice == "3":
        delete_task(to_do_list)
    elif choice == "4":
        print("Exiting the application...")
        break
    else:
        print("Invalid selection. Please try again.")































