// Example program
#include <iostream>
#include <string.h>
using namespace std;

int main()
{
    int numero, fact = 1;
    cout << "Introduzca un numero: ";
    cin >> numero;
    for (int i = numero; i > 0; i--){
        fact = fact * i;
    }
    cout << "El factorial del numero es: "<< fact;
}