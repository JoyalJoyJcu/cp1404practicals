from unreliable_car import UnreliableCar


def main():
    """Test the UnreliableCar class."""
    # Create instances of UnreliableCar
    reliable_car = UnreliableCar("ReliableCar", 100, 90)
    unreliable_car = UnreliableCar("UnreliableCar", 100, 30)

    print("Testing ReliableCar:")
    for i in range(1, 6):  # Test 5 times
        distance_driven = reliable_car.drive(20)
        print(f"Attempt {i}: Drove {distance_driven} km, fuel remaining: {reliable_car.fuel}")

    print("\nTesting UnreliableCar:")
    for i in range(1, 6):  # Test 5 times
        distance_driven = unreliable_car.drive(20)
        print(f"Attempt {i}: Drove {distance_driven} km, fuel remaining: {unreliable_car.fuel}")


if __name__ == "__main__":
    main()
