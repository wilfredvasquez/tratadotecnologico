// Example program
#include <iostream>
#include <string>
using namespace std;

int main()
{
    float num, suma = 0;
    int contador = 0;
    
    do{
        cout << "Introduzca un nro.: ";
        cin >> num;
        if (num >=0){
            suma = suma + num;
            contador = contador + 1;
            cout << "Has introducido " << contador << " numeros y su suma es: " << suma << endl;
        }
    }while(num >= 0);
}