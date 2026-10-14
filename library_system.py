books = [
    {"title": "Python Programming", "available": True},
    {"title": "Data Structures", "available": True},
    {"title": "Machine Learning", "available": True},
    {"title": "Artificial Intelligence", "available": True},
    {"title": "Database Management", "available": True}
]


def show_books():
    print("\nAvailable Books:")
    for i, book in enumerate(books, 1):
        status = "Available" if book["available"] else "Reserved"
        print(f"{i}. {book['title']} - {status}")


def recommend_books():
    print("\nRecommended Books:")
    print("1. Python Programming")
    print("2. Data Structures")
    print("3. Machine Learning")


def reserve_book():
    show_books()

    try:
        choice = int(input("\nEnter book number to reserve: "))

        if 1 <= choice <= len(books):
            book = books[choice - 1]

            if book["available"]:
                book["available"] = False
                print(f"\n'{book['title']}' reserved successfully!")
            else:
                print("\nThis book is already reserved.")
        else:
            print("\nInvalid book number.")

    except ValueError:
        print("\nPlease enter a number.")


def return_book():
    show_books()

    try:
        choice = int(input("\nEnter book number to return: "))

        if 1 <= choice <= len(books):
            book = books[choice - 1]

            if not book["available"]:
                book["available"] = True
                print(f"\n'{book['title']}' returned successfully!")
            else:
                print("\nThis book is already available.")
        else:
            print("\nInvalid book number.")

    except ValueError:
        print("\nPlease enter a number.")


def main():
    while True:
        print("\n==============================")
        print(" LIBRARY BOOK SYSTEM")
        print("==============================")
        print("1. Show Books")
        print("2. Recommend Books")
        print("3. Reserve Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

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


if __name__ == "__main__":
    main()
