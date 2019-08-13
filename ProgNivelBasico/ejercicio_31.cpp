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
    int max = 100, actual = 0, opcion;
    persona individuo[max];
    do{
        cout << "1.- Listar Personas" << endl;
        cout << "2.- Agregar Persona" << endl;
        cout << "3.- Actualizar Persona" << endl;
        cout << "4.- Ver Nro. de Telefono" << endl;
        cout << "5.- Salir" << endl;
        cout << "Elija una opcion --> ";
        cin >> opcion;
        if (opcion == 1){
            if(actual == 0){
                cout << "No hay personas agregadas" << endl << endl;
            }else{
                for (int i = 0; i < actual; i ++){
                    cout << individuo[i].nombre << endl << endl;
                }
            }    
        }
        if (opcion == 2){
            if (actual == max){
                cout << "No puede agregar a más personas" << endl << endl;
            }else{
                cout << "Ingrese su nombre: ";
                cin >> individuo[actual].nombre;
                cout << "Ingrese su nro telefonico: ";
                cin >> individuo[actual].telefono;
                actual ++;
                cout << endl;
            }
        }
        if (opcion == 3){
            if(actual == 0){
                cout << "No hay personas agregadas" << endl << endl;
            }else{
                char name[20];
                int found = 0;
                cout << "Ingrese el nombre de la persona: ";
                cin >> name;
                for(int i = 0; i < actual; i++){
                    if(individuo[i].nombre == name){
                        cout << "Ingrese nuevo nombre: ";
                        cin >> individuo[i].nombre;
                        cout << "Ingrese su nro telefonico: ";
                        cin >> individuo[i].telefono;
                        found = 1;
                        cout << endl;
                    }
                }
                if (found == 0){
                    cout << "Persona no encontrada" << endl << endl;
                }
            } 
        }
        if(opcion == 4){
            if(actual == 0){
                cout << "No hay personas agregadas";
            }else{
                char name[20];
                int found = 0;
                cout << "Ingrese el nombre de la persona: ";
                cin >> name;
                for(int i = 0; i < actual; i++){
                    if(individuo[i].nombre == name){
                        cout << individuo[i].telefono << endl << endl;
                        found = 1;
                    }
                }
                if (found == 0){
                    cout << "Persona no encontrada" << endl << endl;
                }
            } 
        }
        if(opcion == 5){
            cout << "Ha salido del sistema";
        }
    }while(opcion != 5);
}