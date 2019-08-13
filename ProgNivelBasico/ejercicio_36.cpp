// Example program
#include <iostream>
#include <string.h>
#include <math.h>
using namespace std;

float raizCubica(float a){
    float result;
    result = pow(a, 1/3);
    return result;
}

int main()
{
    float a, resultado;
    cout << "Ingrese numero a calcular su raiz cubica: ";
    cin >> a;
    resultado = raizCubica(a);
    cout << "La raiz cubica de "<< a << " es: " << resultado;
}