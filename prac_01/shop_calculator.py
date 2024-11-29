total_price = 0
DISCOUNT = 0.9
DISCOUNT_THRESHOLD = 100

num_items = int(input("Number of items: "))
while num_items < 0:
    print("Invalid number of items!")
    num_items = int(input("Number of items: "))

for i in range(num_items):
    price = float(input("Price of item: "))
    while price < 0:
        print("Price cannot be negative. Please enter a valid price.")
        price = float(input("Price of item: "))
    total_price += price

if total_price > DISCOUNT_THRESHOLD:
    total_price *= DISCOUNT

print(f"Total price for {num_items} items is ${total_price:.2f}")


