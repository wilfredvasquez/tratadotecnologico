// Example program
#include <iostream>
#include <string>
using namespace std;

int main()
{
    int num;
    do{
        cout << "Introduzca el valor del nro: ";
        cin >> num;
        if(num !=0){
            if(num % 2 == 0){
                cout << "El numero es par" << endl;
            }
            else{
                cout << "El numero es impar" << endl;
            }
        }
    }while(num != 0);
}