#include <iostream>

using namespace std;

int main(void)
{
    bool loop = true;

    while (loop == true)
    {
        string command;
        cout << "To exit type (E/e)\nOperator (+ - * /): ";
        cin >> command;

        if (command == "+")
        {
            double x, y, z;
            cout << "Enter first value: ";
            cin >> x;

            cout << "Enter second value: ";
            cin >> y;

            z = x + y;

            cout << "Sum: " << z << endl;
        }
        else if (command == "-")
        {
            double x, y, z;
            cout << "Enter first value: ";
            cin >> x;

            cout << "Enter second value: ";
            cin >> y;

            z = x - y;

            cout << "Difference: " << z << endl;
        }
        else if (command == "*")
        {
            double x, y, z;
            cout << "Enter first value: ";
            cin >> x;

            cout << "Enter second value: ";
            cin >> y;

            z = x * y;

            cout << "Product: " << z << endl;
        }
        else if (command == "/")
        {
            double x, y, z;
            cout << "Enter first value: ";
            cin >> x;

            cout << "Enter second value: ";
            cin >> y;

            z = x / y;

            cout << "Quotient: " << z << endl;
        }
        else if (command == "E" || command == "e")
        {
            loop = false;
        }
        else
        {
            cout << "Please enter a valid command" << endl;
        }
    }

    return 0;
}