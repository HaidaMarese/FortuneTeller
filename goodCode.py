class FortuneTeller:
    def __init__(self):
        # Initializes the fortune-teller with options for past, present, and future
        self.options = {
            'past': self.tell_past,
            'present': self.tell_present,
            'future': self.tell_future
        }

    @staticmethod
    def tell_past():
        """Prints a message about the past"""
        print("You have overcome great challenges in your past.")

    @staticmethod
    def tell_present():
        """Prints a message about the present"""
        print("You are about to experience a surprising turn of events today.")

    @staticmethod
    def tell_future():
        """Prints a message about the future"""
        print("Your future holds great opportunities.")

    @staticmethod
    def tell_invalid():
        """Prints a message for invalid input"""
        print("Invalid choice. Please choose past, present, or future.")

    def start(self):
        """Starts the fortune-teller interaction"""
        print("Welcome to the Fortune Teller!")
        while True:
            choice = input("Would you like to know about your past, present, or future? (Type 'exit' to quit): ").lower()
            if choice == 'exit':
                break
            self.options.get(choice, self.tell_invalid)()
