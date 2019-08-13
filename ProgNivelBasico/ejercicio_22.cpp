// Example program
#include <iostream>
#include <string.h>
using namespace std;

int main()
{
    char texto[100];
    cout << "Ingrese un texto: ";
    cin >> texto;
    int tam = strlen(texto);
    char inv_texto[tam];
    for (int i = 0; i < strlen(texto); i++){
        inv_texto[tam-1] = texto[i];
        tam--;
        cout << texto[i];
    }
    cout << " --- ";
    for(int i=0; i < strlen(texto); i++){
        cout << inv_texto[i];
    }    
}