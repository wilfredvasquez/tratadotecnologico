// Example program
#include <iostream>
#include <string>
using namespace std;

int main()
{
    int num, cont=0;
    
    cout << "Introduzca el nro. a evaluar: ";
    cin >> num;
    for(int i = 2; i < num; i++){
        if(num % i == 0){
            cout << i << " es diviso de " << num << endl;
            cont = 1;
        }
    }
    if(cont == 0){
        cout << "El numero no tiene divisores";
    }
}