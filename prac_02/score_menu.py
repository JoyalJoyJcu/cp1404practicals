""" """

def main():
    score = 0
    display_menu()
    choice = get_choice()

    while choice != "Q":

        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            show_stars(score)
        elif choice != "Q":
            print("Invalid choice.")
        choice = get_choice()
    print("Finished.")


def display_menu():
    """Display the menu options."""
    menu = "(G)et a valid score \n(P)rint result \n(S)how stars \n(Q)uit"
    print(menu)


def get_choice():
    """user's choice."""
    return input(">>> ").upper()


def get_valid_score():
    """valid score between 0 and 100."""
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score. Please enter a valid score (0-100).")
        score = int(input("Enter score: "))
    return score


def print_result(score):
    """Print the score"""
    if score == 0:
        print("Get a score first!")
    else:
        print(f"Score: {score}")


def show_stars(score):
    """Print stars corresponding to the score"""
    if score == 0:
        print("Get a score first!")
    else:
        print('*' * score)



main()
