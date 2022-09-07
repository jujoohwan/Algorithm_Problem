#include <iostream>
using namespace std;


int main(){
    int a = 10;
    int &anothor_a = a;

    int b = 3;
    anothor_a = b;

    cout << a << b << anothor_a << endl;
}