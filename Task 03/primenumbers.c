#include <stdio.h>

int main() {
    int n;
    printf("Enter the value of n: ");
    scanf("%d", &n);

    if (n <= 0 || n == 1) {
        printf("Error: n must be a positive integer and greater than one\n");
        return 0;
    }

    printf("\nPrime numbers up to n:\n");

    for (int num = 2; num <= n; num++) {
        int isPrime = 1;
        for (int divisor = 2; divisor < num; divisor++) {
            if (num % divisor == 0) {
                isPrime = 0;
                break;
            }
        }
        if (isPrime) {
            printf("%d\n", num);
        }
    }

    return 0;
}

