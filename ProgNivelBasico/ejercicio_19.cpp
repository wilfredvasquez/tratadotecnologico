// Example program
#include <iostream>
#include <string>
using namespace std;

int main()
{
    int num;
    
    cout << "Introduzca un nro.: ";
    cin >> num;
    for(int i = 0; i < 11; i++){
        cout << i << " x " << num << "= " << i * num << endl;
    }
}