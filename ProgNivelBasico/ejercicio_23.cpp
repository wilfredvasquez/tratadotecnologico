// Example program
#include <iostream>
#include <string>
using namespace std;

int main()
{
    float numeros[10];
    float suma = 0, media, max = 0, min = 9999;
    for (int i = 0; i < 10; i++){
        cout << "Introduzca un valor: ";
        cin >> numeros[i];
        suma = suma + numeros[i];
        if (numeros[i] > max){
            max = numeros[i];
        }
        if (numeros[i] < min){
            min = numeros[i];
        }
    }
    media = suma / 10;
    cout << "La suma de los numeros es: " << suma << endl;
    cout << "La media es: " << media << endl;
    cout << "El mayor valor es: " << max << endl;
    cout << "El menor valor es: " << min;
}