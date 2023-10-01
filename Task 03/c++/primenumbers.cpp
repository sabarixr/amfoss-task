#include <iostream>

using namespace std;

int main() {
    int n;
    cout << "Enter the value of n: ";
    cin >> n;

    if (n <= 0 || n==1) {
        cout << "Error: n must be a positive integer and greater than one" << endl;
        return 0; 
    }
    

    cout << "\nPrime numbers up to n:" << endl;

    for (int num = 2; num <= n; num++) {
        bool isPrime = true;
        for (int divisor = 2; divisor < num; divisor++) {
            if (num % divisor == 0) {
                isPrime = false;
                break;
            }
        }
        if (isPrime) {
            cout << num << endl;
        }
    }

    return 0;
}

