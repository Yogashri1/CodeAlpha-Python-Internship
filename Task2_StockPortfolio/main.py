stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 170,
    "MSFT": 420,
    "AMZN": 190
}

print("=" * 40)
print("     STOCK PORTFOLIO TRACKER")
print("=" * 40)

name = input("Enter stock name: ").upper().strip()

if name in stocks:
    qty = int(input("Enter quantity: "))

    price = stocks[name]
    total = price * qty

    print("\nStock:", name)
    print("Price per Share: $", price)
    print("Quantity:", qty)
    print("Total Investment: $", total)

    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("-----------------------\n")
        file.write(f"Stock: {name}\n")
        file.write(f"Price per Share: ${price}\n")
        file.write(f"Quantity: {qty}\n")
        file.write(f"Total Investment: ${total}\n")

    print("\nPortfolio saved to portfolio.txt")

else:
    print("\nStock not found in the predefined list.")
