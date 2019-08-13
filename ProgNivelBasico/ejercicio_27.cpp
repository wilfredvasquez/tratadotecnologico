// Example program
#include <iostream>
#include <string.h>
using namespace std;

int main()
{
    char password[10] = "QWER.1234";
    char password2[20];
    int check;
    for (int i = 0; i < 3; i++){
        check = 0;
        cout << "Inserte el password: ";
        cin >> password2;
        for (int j = 0; j < 10; j++){
            if(password[j] != password2[j] || strlen(password2) > strlen(password)){
                check = 1;
            }
        }
        if(check == 0){
            cout << "Acceso Permitido";
            break;
        }
    }
    if(check == 1){
        cout << "Acceso Denegado";
    }
}