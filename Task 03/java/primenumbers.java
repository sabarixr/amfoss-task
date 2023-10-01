import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class PrimeNumbers {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the value of n: ");
        int n = scanner.nextInt();

        if (n <= 0) {
            System.out.println("Error: n must be a positive integer");
            return;
        }

        List<Integer> primes = new ArrayList<>();

        for (int num = 2; num <= n; num++) {
            boolean isPrime = true;
            for (int divisor = 2; divisor * divisor <= num; divisor++) {
                if (num % divisor == 0) {
                    isPrime = false;
                    break;
                }
            }
            if (isPrime) {
                primes.add(num);
            }
        }

        System.out.println("\nPrime numbers up to n:");
        for (int prime : primes) {
            System.out.println(prime);
        }
    }
}

