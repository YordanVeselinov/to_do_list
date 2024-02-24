import time


def add_task():
    task = input("Enter your task: ")
    with open("list_of_to_do.txt", "a") as file:
        file.write(task + "\n")
        print("Task added successfully!")

    while True:
        answer_to_add_more = input("Do you want more tasks? (Y or N): ").lower()

        if answer_to_add_more == "n":
            break
        elif answer_to_add_more == "y":
            add_task()
        else:
            print("Invalid answer, please enter 'Y' or 'N'!")


def show_tasks():
    with open("list_of_to_do.txt") as file:
        list_of_tasks = file.readlines()
        for line in list_of_tasks:
            number_of_task = list_of_tasks.index(line) + 1
            print(f"{number_of_task}. " + line[:-1])

    time.sleep(1)
    print()


def delete_task():
    show_tasks()
    number_of_task_to_remove = int(input("Which task do you want to remove, enter the number of the task: ")) - 1

    orig_lines = [line.strip() for line in open('list_of_to_do.txt').readlines()]
    new_lines = [line for line in orig_lines if orig_lines.index(line) != number_of_task_to_remove]

    with open('list_of_to_do.txt', 'w') as fp:
        print(*new_lines, sep='\n', file=fp)

    print("This is your new To Do List!")
    show_tasks()


print("--- Welcome to my console To Do List! ---")

while True:
    print(f"1. Add a task")
    print(f"2. Remove a task")
    print(f"3. View all tasks")
    print(f"4. Exit")

    choice = input("Enter the number corresponding to the action (1-4): \n")

    if choice == "4":
        print("Are you sure you want to exit? ")
        answer = input("Select Yes or No ( Y or N ): ").lower()
        if answer == "y":
            break
        elif answer == "n":
            continue
        else:
            print("Invalid answer, please try again!")
    elif choice == "1":
        add_task()
    elif choice == "2":
        delete_task()
    elif choice == "3":
        show_tasks()
    else:
        print("Invalid number! Please enter number between 1 and 4.\n")
        time.sleep(2)
