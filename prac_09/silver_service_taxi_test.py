from silver_service_taxi import SilverServiceTaxi


def test_silver_service_taxi():
    """Test the SilverServiceTaxi class."""
    my_taxi = SilverServiceTaxi("Fancy Taxi", 100, 2)
    my_taxi.start_fare()
    my_taxi.drive(18)
    expected_fare = my_taxi.get_fare()
    print(my_taxi)
    print(f"Expected fare: ${expected_fare:.2f}")
    assert abs(expected_fare - 48.78) < 0.01, f"Expected 48.78, but got {expected_fare}"
    assert "plus flagfall of $4.50" in str(my_taxi), "Flagfall charge missing in string"


if __name__ == "__main__":
    test_silver_service_taxi()
