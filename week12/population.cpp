//Name:  James Yu
//Email:  james.yu66@myhunter.cuny.edu
//Date: November 25, 2023

#include <iostream>
using namespace std;

int main(){
    int year;
    float pop = 325.7;
    int cYear = 2017;
    cout << "Please enter the number of years: ";
    cin >> year;
    for (int i = 0; i < year; i++)
    {
        cout << "Year " << cYear << "   " << pop << endl;
        pop = pop + ((12.4/1000)* pop) - ((8.4/1000) * pop);
        cYear++;
    }
    
}