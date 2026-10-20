'''
================
Exercise 1
================

The dictionary shows currency exchange rates

Modify the code to:
- Look up the current rate for converting USD to EUR. Update the dictionary to reflect new data.
- Look up the current rate for converting JPY to EUR. Include the new entry in the dictionary
- Try to use a list instead of a tuple as the key and observe what happens
'''

exchange_rates = {
    ("USD", "EUR"): 0.93,
    ("EUR", "GBP"): 0.86,
    ("USD", "JPY"): 151.7
}

# Update the current rate for USD to EUR
exchange_rates[("USD", "EUR")] = 0.95

# Add a new rate for JPY to EUR
exchange_rates[("JPY", "EUR")] = 0.0062

print("Updated exchange rates:")
print(exchange_rates)

# Try using a list as a dictionary key
exchange_rates[["USD", "CAD"]] = 1.36