def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)
    else:
        return price

# Prompt user for input
try:
    price = float(input("Enter the original price: R"))
    discount = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(price, discount)

    if discount >= 20:
        print(f"Discount applied! Final price: R{final_price:.2f}")
    else:
        print(f"No discount applied. Price remains: R{price:.2f}")

except ValueError:
    print("Please enter valid numeric values.")
