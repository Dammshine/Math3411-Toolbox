#include "codes.h"
#include <iostream>
#include <string>
#include "Windows.h"
using namespace std;

int main() {
    while (true) {
        cout << "Input command\n \t 1. arithmetic (ar) \n\t 2. comma \n\t 3. lz78\n";
        string command;
        cin >> command;
        system("cls");

        if (command == "ar" || command == "arithmetic" || command == "1") {
        arithmetic();
        } else if (command == "comma" || command == "2") {
            cout << "Enter code and length in following format\n111111101100110 4\n";
            string code;
            int len;
            cin >> code >> len;
            cout << commaCodeDecode(code, 4) << endl;
        } else if (command == "lz78" || command == "3") {
            lz78();
        } else {
            break;
        }
        
    }
}