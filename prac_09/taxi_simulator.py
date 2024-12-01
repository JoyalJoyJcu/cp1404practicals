from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    """Taxi Simulator program."""
    print("Let's drive!")
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    bill = 0.0
    current_taxi = None
    choice = ""

    while choice != "q":
        print("\nq)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").lower()

        if choice == "c":
            current_taxi = choose_taxi(taxis, current_taxi)
        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive.")
            else:
                bill += drive_taxi(current_taxi)
        elif choice != "q":
            print("Invalid option")

        print(f"Bill to date: ${bill:.2f}")

    print(f"\nTotal trip cost: ${bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def choose_taxi(taxis, current_taxi):
    """Allow user to select a taxi."""
    print("Taxis available:")
    display_taxis(taxis)

    try:
        choice = int(input("Choose taxi: "))
        if 0 <= choice < len(taxis):
            return taxis[choice]
        else:
            print("Invalid taxi choice. Taxi unchanged.")
    except ValueError:
        print("Invalid input. Please enter a number.")

    return current_taxi


def drive_taxi(taxi):
    """Drive the chosen taxi and return the trip cost."""
    try:
        distance = int(input("Drive how far? "))
        taxi.start_fare()  # Start a new fare
        distance_driven = taxi.drive(distance)
        trip_cost = taxi.get_fare()
        print(f"Your {taxi.name} trip cost you ${trip_cost:.2f}")
        return trip_cost
    except ValueError:
        print("Invalid input. Please enter a number.")
        return 0.0


def display_taxis(taxis):
    """Display a list of taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


if __name__ == "__main__":
    main()
