//Name:  James Yu
//Email:  james.yu66@myhunter.cuny.edu
//Date: November 25, 2023

#include <iostream>
using namespace std;

int main(){
    int size;
    cin >> size;
    for (int i = 1; i <= size; i++)
    {
        string star(i, '*');
        cout << star << endl;
    }
    
}