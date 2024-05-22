import operations as ops

def main(): 
    loop = True 

    while loop == True: 
        operator = str(input("To exit type (E/e)\nEnter operator (+) (-) (*) (/) : "))

        match operator: 
            case "+": 
                ops.Operators.addition()
            case "-": 
                ops.Operators.subtraction()
            case "*": 
                ops.Operators.multiplication()
            case "/": 
                ops.Operators.division()
            case "E": 
                loop = False;
            case "e": 
                loop = False;

main()