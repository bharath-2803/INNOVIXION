def print_tasks(tasks):
    print("Here is your to-do list:")
    for task in tasks:
        print(f"- {task}")

def add_task(tasks):
    task = input("Enter the task you want to add: ")
    tasks.append(task)
    print(f"{task} has been added to your to-do list.")
def delete_task(tasks):
    task = input("Enter the task you want to delete: ")
    if task in tasks:
        tasks.remove(task)
        print(f"{task} has been deleted from your to-do list.")
    else:
        print(f"{task} is not in your to-do list.")

def manage_tasks():
    tasks = []
    while True:
        print("\nTo-do list menu:")
        print("1. Print tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Quit")

        option = input("Enter the number of your option: ")

        if option == "1":
            print_tasks(tasks)
        elif option == "2":
            add_task(tasks)
        elif option == "3":
            delete_task(tasks)
        elif option == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

manage_tasks()