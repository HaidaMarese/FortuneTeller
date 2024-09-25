from goodCode import FortuneTeller  # Good version with proper class and methods
from horriblecode import val  # Horrible version with the simple function

def main():
    print("Choose the version of the Fortune Teller you want to run:")
    print("1: Good Code")
    print("2: Horrible Code")
    choice = input("Enter 1 or 2: ")

    if choice == '1':
        teller = FortuneTeller()  # Good code with proper OOP
        teller.start()
    elif choice == '2':
        val()  # Horrible code with a simple function
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()





