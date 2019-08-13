// Example program
#include <iostream>
#include <string.h>
using namespace std;

int main()
{
    struct persona{
        string nombre;
        string telefono;
    };
    persona individuo[10];
    for (int i = 0; i < 10; i++){
        cout << "Ingrese su nombre: ";
        cin >> individuo[i].nombre;
        cout << "Ingrese su nro telefonico: ";
        cin >> individuo[i].telefono;
    }
    for (int i = 0; i < 10; i ++){
        if (individuo[i].telefono[0] == '6'){
            cout << individuo[i].nombre << " -- " << individuo[i].telefono << endl;
        }
    }
}