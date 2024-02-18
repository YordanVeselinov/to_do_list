import time

print("Welcome to my console To Do List!")

while True:
    print(f"1. Add task")
    print(f"2. Remove task")
    print(f"3. View tasks")
    print(f"4. Exit")

    choice = input("Enter the number corresponding to the action (1-4): \n")

    if choice == "4":
        break
    elif choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    else:
        print("Invalid number! Please enter number between 1 and 4.\n")
        time.sleep(2)

