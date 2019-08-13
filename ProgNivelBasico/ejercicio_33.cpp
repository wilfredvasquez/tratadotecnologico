// Example program
#include <iostream>
#include <string.h>
using namespace std;

float division(float a, float b){
    float result;
    result = a / b;
    return result;
}

int main()
{
    int num1, num2;
    float resultado;
    cout << "Ingrese numero 1: ";
    cin >> num1;
    cout << "Ingrese numero 2: ";
    cin >> num2;
    if(num2 == 0){
        cout << "No se puede dividir entre 0";
    }else{
        resultado = division(num1, num2);
        cout << "El resultado es: " << resultado;
    }
}