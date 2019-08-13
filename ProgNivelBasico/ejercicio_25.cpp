// Example program
#include <iostream>
#include <string>
using namespace std;

int main()
{
    float numeros[10], repetidos[10];
    int m = 0;
    for (int i = 0; i < 10; i++){
        cout << "Introduzca un valor: ";
        cin >> numeros[i];
        for(int j = 0; j < i; j++){
            if(numeros[j] == numeros[i]){
                repetidos[m] = numeros[i];
                m++;
            }
        }
    }
    for(int i = 0; i < 10;i++){
        cout << numeros[i] << " ; ";
    }
    cout << endl << "Los numeros repetidos son: ";
    for (int i = 0; i < m; i ++){
        cout << repetidos[i] << " ; ";
    }
}