#Define an empty shopping list
shopping_list = []

while True:
    choice = input("Choose: add / remove / show / done: ").lower()

    if choice == "add":
        item = input("Enter an item: ")
        shopping_list.append(item)

    elif choice == "remove":
        item = input("Enter an item to remove: ")

        if item in shopping_list:
            shopping_list.remove(item)
        else:
            print("That item is not on your list.")

    elif choice == "show":
        for item in shopping_list:
            print(item)

    elif choice == "done":
        print("Goodbye!")
        break