// Example program
#include <iostream>
#include <string.h>
using namespace std;

int main()
{
    char numeros[20];
    cout << "Inserte un numero: ";
    cin >> numeros;
    int tam = strlen(numeros);
    int j = tam - 1, check = 0;
    for (int i = 0; i < tam; i ++){
        if(numeros[i] != numeros[j]){
            check = 1;
        }
        j--;
    }
    if(check == 0){
        cout << "El numero es capicua";
    }
    else{
        cout << "El numero no es capicua";
    }
}