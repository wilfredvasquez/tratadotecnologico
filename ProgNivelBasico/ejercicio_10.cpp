// Example program
#include <iostream>
#include <string>
using namespace std;

int main()
{
    float dato1, dato2;
    cout << "Introduzca el valor del nro 1: ";
    cin >> dato1;
    cout << "Introduzca el valor del nro 2: ";
    cin >> dato2;
    if (dato2 == 0){
        cout << "Error: No se puede dividir entre 0";
    }
    else{
        cout << "El resultado de la division es: "<< dato1 / dato2;
    }
}