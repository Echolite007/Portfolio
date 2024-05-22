# Dictionary of cities with temperatures in Fahrenheit 
cities_in_F = {
    "Los Angeles": 100,
    "New York": 32, 
    "Boston": 75,
}

# Dictionary of cities with temperatures in Celsius converted from list of cities with temperatures in Fahrenheit using Dictionary Comprehension
cities_in_C = {key: round(((value-32) / (5/9)), 1) for (key,value) in cities_in_F.items()}
print(cities_in_C)