// Example program
#include <iostream>
#include <string.h>
using namespace std;

int suma(int a, int b){
    return a + b;
}

int main()
{
    int num1, num2, resultado;
    cout << "Ingrese numero 1: ";
    cin >> num1;
    cout << "Ingrese numero 2: ";
    cin >> num2;
    resultado = suma(num1, num2);
    cout << "El resultado es: " << resultado;
}