prices =[10,20,30]
discount = 10
final_prices = []
for price in prices:
    final_price = price - (price * discount / 100)
    final_prices.append(final_price)
print(final_prices)  # Output: [9.0, 18.0, 27.0]