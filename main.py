from libz import displayMenu


def main():
    while True:
        try:
            displayMenu()
            choice = int(input("\tEnter an option [1-15]: "))
        except ValueError:
            print("\nInvalid input. Please enter only the numbers between 1 and 15.\n")
        match choice:
            case 1:
                print("You selected: View Books' Details")
            case 2:
                print("You selected: View Users' Details")
            case 3:
                print("You selected: Search Book")
            case 4:
                print("You selected: Search User")
            case 5:
                print("You selected: Lending Book")
            case 6:
                print("You selected: Return Book")
            case 7:
                print("You selected: Add New Book")
            case 8:
                print("You selected: Add New User")
            case 9:
                print("You selected: Delete Book")
            case 10:
                print("You selected: Delete User")
            case 11:
                print("You selected: View Lending History")
            case 12:
                print("You selected: View Overdue Books")
            case 13:
                print("You selected: Update Book Information")
            case 14:
                print("You selected: Update User Information")
            case 15:
                print("You selected: Exit")
                exit()
            case _:
                print("Invalid option! Please select a valid option between 1 and 15.")


if __name__ == "__main__":
    main()
