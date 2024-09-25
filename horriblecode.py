def val():
    user_input = input("Type 1 for past, 2 for present, and 3 for future: ")

    if user_input == '1':
        print("You have lived a life with struggle yet persevered.")
    elif user_input == '2':
        print("Today will bring you great luck.")
    elif user_input == '3':
        print("There is great fortune in your future.")
    else:
        print("Invalid input.")

