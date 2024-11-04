def name_game():
    try:
        # user input
        name = input("Enter your name: ")

        # check if the input is empty
        if not name.strip():
            raise ValueError("No input detected. Please enter a valid name.")

        # check if the input is purely alphabetical (no numbers, special characters)
        if not name.isalpha():
            raise ValueError("Invalid input. Name should contain only letters.")

        print("Here's your name, letter by letter:")
        for letter in name:
            print(letter)

    except ValueError as e:
        print("Error:", e)

    finally:
        print("Thank you for using the name game.")

name_game()