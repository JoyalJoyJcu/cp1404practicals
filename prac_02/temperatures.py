"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

def main():
    menu = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            converting_celsius_to_fahrenheit()
        elif choice == "F":
            converting_fahrenheit_to_celsius()
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    print("Thank you.")

def converting_celsius_to_fahrenheit():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    return print(f"Result: {fahrenheit:.2f} F")

def converting_fahrenheit_to_celsius():
    fahrenheit = float(input("fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    return print(f"Result: {celsius:.2f}")

main()
