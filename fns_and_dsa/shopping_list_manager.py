def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            item = input("Enter the item to add: ")
            shopping_list.append(item)

        elif choice == 2:
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
            else:
                print("Item not found.")

        elif choice == 3:
            print(shopping_list)

        elif choice == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()







































^G Help         ^O Write Out    ^F Where Is     ^K Cut          ^T Execute      ^C Location     M-U Undo        M-A Set Mark    M-] To Bracket
^X Exit         ^R Read File    ^\ Replace      ^U Paste        ^J Justify      ^/ Go To Line   M-E Redo        M-6 Copy        ^B Where Was


