//Name:  James Yu
//Email:  james.yu66@myhunter.cuny.edu
//Date: November 25, 2023

#include <iostream>
using namespace std;

int main(){
    int year;
    cout << "Enter year: ";
    cin >> year;
    while (year > 2018){
        cout << "Year must be 2018 or earlier: ";
        cin >> year;
    }
    cout << "You entered: " << year;
}