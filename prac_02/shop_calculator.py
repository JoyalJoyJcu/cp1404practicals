
DISCOUNT = 0.9
DISCOUNT_THRESHOLD = 100

def main():
    total_price = 0
    num_items = get_num_items()

    for i in range(num_items):
        price = get_price()
        total_price += price

    if total_price > DISCOUNT_THRESHOLD:
        total_price *= DISCOUNT

    print(f"Total price for {num_items} items is ${total_price:.2f}")


def get_price():
    price = float(input("Price of item: "))
    while price < 0:
        print("Price cannot be negative. Please enter a valid price.")
        price = float(input("Price of item: "))
    return price


def get_num_items():
    num_items = int(input("Number of items: "))
    while num_items < 0:
        print("Invalid number of items!")
        num_items = int(input("Number of items: "))
    return num_items


main()


