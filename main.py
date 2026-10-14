
# Library Book Recommendation & Reservation System

books = [
    ["Python Programming", True],
    ["Data Structures", True],
    ["Machine Learning", True],
    ["Artificial Intelligence", True],
    ["Database Management", True]
]


def show_books():
    print("\n--- BOOKS ---")

    for i in range(len(books)):
        if books[i][1]:
            status = "Available"
        else:
            status = "Reserved"

        print(i + 1, ".", books[i][0], "-", status)


def recommend_books():
    print("\n--- RECOMMENDED BOOKS ---")
    print("1. Python Programming")
    print("2. Data Structures")
    print("3. Machine Learning")


def reserve_book():
    show_books()

    choice = input("\nEnter book number to reserve: ")

    if choice.isdigit():
        number = int(choice)

        if number >= 1 and number <= len(books):
            if books[number - 1][1]:
                books[number - 1][1] = False
                print("\nBook reserved successfully!")
            else:
                print("\nBook is already reserved.")
        else:
            print("\nInvalid book number.")
    else:
        print("\nPlease enter a number.")


def return_book():
    show_books()

    choice = input("\nEnter book number to return: ")

    if choice.isdigit():
        number = int(choice)

        if number >= 1 and number <= len(books):
            if not books[number - 1][1]:
                books[number - 1][1] = True
                print("\nBook returned successfully!")
            else:
                print("\nBook is already available.")
        else:
            print("\nInvalid book number.")
    else:
        print("\nPlease enter a number.")


# Main Menu
while True:

    print("\n==============================")
    print("     LIBRARY BOOK SYSTEM")
    print("==============================")
    print("1. Show Books")
    print("2. Recommend Books")
    print("3. Reserve Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_books()

    elif choice == "2":
        recommend_books()

    elif choice == "3":
        reserve_book()

    elif choice == "4":
        return_book()

    elif choice == "5":
        print("\nThank you for using Library Book System!")
        break

    else:
        print("\nInvalid choice. Please enter 1 to 5.")
