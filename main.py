'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

 

class PhoneBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number):
        self.contacts[name] = phone_number
        print("Added {} with phone number {} to the phone book.".format(name, phone_number))

    def search_contact(self, name):
        if name in self.contacts:
            return self.contacts[name]
        else:
            return "Contact not found."

def main():
    phone_book = PhoneBook()

    while True:
        print("\nPhone Book Management System")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()  # Convert to string and then remove leading/trailing spaces

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            phone_book.add_contact(name, phone_number)

        elif choice == '2':
            name = input("Enter name to search: ")
            result = phone_book.search_contact(name)
            print("Search result:", result)

        elif choice == '3':
            print("Exiting the Phone Book Management System.")
            break

        else:
            print("Invalid choice. Please enter a valid choice.")


if __name__ == "__main__":
    main()

