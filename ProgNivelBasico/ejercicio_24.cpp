// Example program
#include <iostream>
#include <string.h>
using namespace std;

int main()
{
    char texto[100];
    cout << "Ingrese un texto: ";
    cin.getline(texto, 100);
    int i = 0;
    while(texto[i] != 0){
        if(texto[i] == ' '){
            texto[i] = '-';
        }
        cout << texto[i];
        i++;
    }
}