import time

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
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    else:
        print("Invalid number! Please enter number between 1 and 4.\n")
        time.sleep(2)

