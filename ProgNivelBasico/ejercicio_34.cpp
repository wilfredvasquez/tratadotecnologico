// Example program
#include <iostream>
#include <string.h>
using namespace std;

int letraRepetida(int a, char b){
    for(int i = 0; i < a; i++){
        cout << b;
    }    
}

int main()
{
    int num1;
    char letra;
    cout << "Ingrese la letra: ";
    cin >> letra;
    cout << "Indique las veces a repetir: ";
    cin >> num1;
    letraRepetida(num1, letra);
}