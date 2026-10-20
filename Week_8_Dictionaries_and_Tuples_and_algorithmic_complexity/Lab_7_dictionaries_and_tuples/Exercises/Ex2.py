'''
================
Exercise 2
================

The dictionary shows supermarket inventory data.

Each product name maps to a dictionary of properties. The product’s barcode and supplier are stored as a tuple under 'product info'.

Add a new product entry using the same structure.

Update the stock of apples after selling 5 units.

Print the barcode number for bread. 

Why should barcode and supplier be stored as an immutable data type, but stock and price be stored as a mutable data type?
'''

inventory = {
    "apple": {"price": 0.50, 
              "stock": 120, 
              "product info": ("123456789012", "FreshFarm Ltd")},
    "bread": {"price": 1.20, 
              "stock": 40, 
              "product info": ("1278274389030", "Wonderfarm")},
}

