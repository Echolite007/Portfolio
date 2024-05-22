def get_number(first):
    errorText = "Please enter a number"
    if first == True:
        while True:
            try: 
                return float(input("Enter first value: "))
            except ValueError: 
                print(errorText)
    else:
        while True: 
            try:
                return float(input("Enter second value: "))
            except ValueError:
                print(errorText)
class Operators: 
    def addition():
        x = get_number(True)
        y = get_number(False)
        z = x + y
        print(f"Sum: {z}")
    def subtraction(): 
        x = get_number(True)
        y = get_number(False)
        z = x - y
        print(f"Difference: {z}")
    def multiplication():
        x = get_number(True)
        y = get_number(False)
        z = x * y
        print(f"Product: {z}")
    def division(): 
        x = get_number(True)
        y = get_number(False)
        z = x / y
        print(f"Quotient: {z}")

def main(): 
    loop = True 

    while loop == True: 
        operator = str(input("To exit type (E/e)\nEnter operator (+) (-) (*) (/) : "))

        match operator: 
            case "+": 
                Operators.addition()
            case "-": 
                Operators.subtraction()
            case "*": 
                Operators.multiplication()
            case "/": 
                Operators.division()
            case "E": 
                loop = False;
            case "e": 
                loop = False;

main()