// Example program
#include <iostream>
#include <string>
using namespace std;

int main()
{
    int num;
    char letra;
    
    cout << "Introduzca un caracter: ";
    cin >> letra;
    cout << "Introduzca el nro. de veces a repetir: ";
    cin >> num;
    for(int i = 0; i < num; i++){
        cout << letra;
    }
}