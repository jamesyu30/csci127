//Name:  James Yu
//Email:  james.yu66@myhunter.cuny.edu
//Date: November 25, 2023

#include <iostream>
using namespace std;

int main(){
    cout << "Enter month (as a number): ";
    int month;
    cin >> month;
    if (month < 3 or month > 11){
        cout << "Happy Winter";
    }
    else if (month >= 3 and month < 7){
        cout << "Happy Spring";
    }
    else if (month >= 7 and month < 9){
        cout << "Happy Summer";
    }
    else{
        cout << "Happy Fall";
    }
}
