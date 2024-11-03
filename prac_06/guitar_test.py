from prac_06.guitar import Guitar

def main():
    """Test the get_age and is_vintage methods of the Guitar class."""

    guitar1 = Guitar("Gibson L-5 CES", 1924, 16035.40)
    guitar2 = Guitar("Another Guitar", 2015, 1512.9)

    print(f"{guitar1.name} get_age() - Expected 100. Got {guitar1.get_age()}")
    print(f"{guitar2.name} get_age() - Expected 9. Got {guitar2.get_age()}")

    print(f"{guitar1.name} is_vintage() - Expected True. Got {guitar1.is_vintage()}")
    print(f"{guitar2.name} is_vintage() - Expected False. Got {guitar2.is_vintage()}")


main()
