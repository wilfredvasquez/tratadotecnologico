// Example program
#include <iostream>
#include <string>
using namespace std;

int main()
{
    float num;
    int contador = 0;

    cout << "Introduzca un nro.: ";
    cin >> num;
    while(num > 1){  
        num = num / 10;
        contador ++;
    }
    cout << "El numero tiene "<< contador << " enteras";
}