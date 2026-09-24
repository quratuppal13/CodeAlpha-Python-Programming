import csv

# Hardcoded dictionary to define stock prices as required
stock_prices = {
    "AAPL": 180, 
    "TSLA": 250, 
    "MSFT": 400, 
    "GOOG": 150
}

print("--- CODEALPHA STOCK PORTFOLIO TRACKER ---")
print("Available Stocks in System:", list(stock_prices.keys()))

# Taking user inputs
stock_name = input("\nEnter Stock Name (e.g., AAPL): ").upper().strip()
try:
    quantity = int(input("Enter Quantity of Shares: "))
except ValueError:
    print("❌ Error: Quantity must be a valid integer number.")
    exit()

if stock_name in stock_prices:
    price_per_share = stock_prices[stock_name]
    total_investment = price_per_share * quantity
    
    print("\n--- Portfolio Summary ---")
    print(f"Stock: {stock_name}")
    print(f"Quantity: {quantity}")
    print(f"Total Investment Value: ${total_investment}")
    
   
    filename = "portfolio_tracker.csv"
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Stock Name", "Quantity", "Price Per Share", "Total Investment"])
        writer.writerow([stock_name, quantity, f"${price_per_share}", f"${total_investment}"])
        
    print(f"\n📊 Results successfully saved locally to '{filename}'!")
else:
    print("❌ Error: The entered stock is not available in our system dictionary.")
