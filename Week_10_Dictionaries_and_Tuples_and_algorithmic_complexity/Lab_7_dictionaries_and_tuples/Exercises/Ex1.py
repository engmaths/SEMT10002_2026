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

exchange_rates[("USD", "EUR")] = 0.91

print(exchange_rates)

