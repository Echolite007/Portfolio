def main():
    # Total amount of shares 
    shares = 1000
    # Amount of shares owned
    shares_owned = 1000

    valuation, shares, shares_issued, percentage_ownership, net_worth = raise_funding(2000000, 10, shares_owned, shares)
    print("---------------------------------------------------------------------------------------------")
    print("Seed")
    print(f"Valuation: ${valuation}")
    print(f"Shares: {shares}")
    print(f"New shares issued: {shares_issued}")
    print(f"Percentage Ownership: {percentage_ownership}%")
    print(f"Net Worth: ${net_worth}")
    valuation, shares, shares_issued, percentage_ownership, net_worth = raise_funding(10000000, 10, shares_owned, shares)
    print("---------------------------------------------------------------------------------------------")
    print("Series A")
    print(f"Valuation: ${valuation}")
    print(f"Shares: {shares}")
    print(f"New shares issued: {shares_issued}")
    print(f"Percentage Ownership: {percentage_ownership}%")
    print(f"Net Worth: ${net_worth}")
    valuation, shares, shares_issued, percentage_ownership, net_worth = raise_funding(75000000, 10, shares_owned, shares)
    print("---------------------------------------------------------------------------------------------")
    print("Series B")
    print(f"Valuation: ${valuation}")
    print(f"Shares: {shares}")
    print(f"New shares issued: {shares_issued}")
    print(f"Percentage Ownership: {percentage_ownership}%")
    print(f"Net Worth: ${net_worth}")
    valuation, shares, shares_issued, percentage_ownership, net_worth = raise_funding(375000000, 10, shares_owned, shares)
    print("---------------------------------------------------------------------------------------------")
    print("Series C")
    print(f"Valuation: ${valuation}")
    print(f"Shares: {shares}")
    print(f"New shares issued: {shares_issued}")
    print(f"Percentage Ownership: {percentage_ownership}%")
    print(f"Net Worth: ${net_worth}")
    valuation, shares, shares_issued, percentage_ownership, net_worth = raise_funding(1250000000, 10, shares_owned, shares)
    print("---------------------------------------------------------------------------------------------")
    print("Series D")
    print(f"Valuation: ${valuation}")
    print(f"Shares: {shares}")
    print(f"New shares issued: {shares_issued}")
    print(f"Percentage Ownership: {percentage_ownership}%")
    print(f"Net Worth: ${net_worth}")



def recalculate_ownership(shares_owned, shares, percent_value): 
    percentage_ownership = round(((shares_owned/shares) * 100), 2)
    net_worth = format(round(percentage_ownership * percent_value, 2), ',')
    return percentage_ownership, net_worth

def calculate_valuation(percent_value):
    valuation = format(round(percent_value * 100, 2), ',')
    return valuation

def shares_recalculation(stake, shares):
    shares_issued = round((shares * stake) / (100 - stake), 2)
    shares = shares + shares_issued
    return shares, shares_issued

def raise_funding(investment, stake, shares_owned, shares): 
    # Get new valuation
    percent_value = investment / stake 
    valuation = calculate_valuation(percent_value)
    # Get new total of shares
    shares, shares_issued = shares_recalculation(stake, shares)
    # Get new ownership
    percentage_ownership, net_worth = recalculate_ownership(shares_owned, shares, percent_value)

    return valuation, shares, shares_issued, percentage_ownership, net_worth


main()