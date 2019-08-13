// Example program
#include <iostream>
#include <string.h>
#include <math.h>
using namespace std;

float solucionRC1(float a, float b, float c){
    float raiz, sol1;
    raiz = b*b - 4*a*c;
    sol1 = (-b + pow(raiz, 1/2)) / (2*a);
    return sol1;
}
float solucionRC2(float a, float b, float c){
    float raiz, sol2;
    raiz = b*b - 4*a*c;
    sol2 = (-b - pow(raiz, 1/2)) / (2*a);
    return sol2;
}
int existeSolucionRC(float a, float b, float c){
    float raiz;
    raiz = b*b - 4*a*c;
    if (raiz < 0){
        return 0;
    }else{
        return 1;
    }
}

int main()
{
    float a, b, c;
    int hasSol;
    cout << "Ingrese los coeficientes de la ecuacion de segundo grado" << endl;
    cout << "Ingrese a: ";
    cin >> a;
    cout << "Ingrese b: ";
    cin >> b;
    cout << "Ingrese c: ";
    cin >> c;
    hasSol = existeSolucionRC(a, b, c);
    if(hasSol == 1){
        cout << "Raiz nro. 1: " << solucionRC1(a, b, c) << endl;
        cout << "Raiz nro. 2: " << solucionRC2(a, b, c);
    }else{
        cout << "No tiene solucion";
    }
}