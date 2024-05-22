# Time invested
investment_time = int(input("Time invested (terms): "))
# Get initial investment 
invested_capital = float(input("Initial investment ($): "))
# Get compound interest rate
compound_interest = float(input("Interest rate for each term (%): "))
# Get additional investment after each term
additional_investment = float(input("Additional investment after each term ($): "))
# Compound of additional investment 
additional_investment_compound = float(input("Compound interest on additional investment (%): "))
# Calculate final equity 
equity = invested_capital * ((compound_interest / 100) + 1)**(investment_time)
# Interest of additional investments
for term in range(1, investment_time + 1):
    additional_investment = additional_investment * ((additional_investment_compound / 100) + 1)
    equity += additional_investment * ((compound_interest / 100) + 1)**(investment_time - term)
    

print(f"Final equity: ${format(round(equity, 2), ',')}")