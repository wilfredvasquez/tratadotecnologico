// Example program
#include <iostream>
#include <string>
using namespace std;

int main()
{
    int acum = 0, num;
    for(int i=0; i<20; i++){
        cout << "Introduzca un valor entero: ";
        cin >> num;
        acum = acum + num;
    }
    cout << "La suma total es: " << acum;
}