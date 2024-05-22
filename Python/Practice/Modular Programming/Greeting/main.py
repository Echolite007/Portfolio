import greetings as grt

def main():
    # Get name of user 
    name = input("Name: ")
    grt.hello(name)
    print("Thank you for using this program!")
    grt.bye(name)

main()