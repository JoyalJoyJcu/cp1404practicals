def main():
    """Gets a score from the user and evaluates it."""
    score = float(input("Enter score: "))
    calculate_score(score)

def calculate_score(score):
    """Evaluates the score and prints a message based on its value."""
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")

main()
