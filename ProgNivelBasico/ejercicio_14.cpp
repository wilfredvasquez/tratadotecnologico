// Example program
#include <iostream>
#include <string>
using namespace std;

int main()
{
    float max = 0, min = 9999, num;
    for(int i=0; i<20; i++){
        cout << "Introduzca un valor entero: ";
        cin >> num;
        if(num > max){
            max = num;
        }
        if(num < min){
            min = num;
        }
    }
    cout << "El valor maximo ingresado es: " << max << endl;
    cout << "El valor minimo ingresado es: " << min;
}