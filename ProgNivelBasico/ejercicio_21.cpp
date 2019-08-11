// Example program
#include <iostream>
#include <string>
using namespace std;

int main()
{
    int num[20];

    for (int i=0; i < 20; i++){
        cout << "Introduzca un nro.: ";
        cin >> num[i];
    }
    for (int i=0; i < 10; i++){
        cout << num[i] << " ";
    }
}