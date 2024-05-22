store = [("shirts", 20.00),
         ("pants", 25.00),
         ("jacket", 50.00),
         ("socks", 10.00),
         ]

# Objective: Convert prices to Euros 

# Map function
to_euros = lambda data: (data[0], data[1] * 0.90)

# Create new iterable 
store_in_euros = map(to_euros, store)

for item in store_in_euros:
    print(item)

