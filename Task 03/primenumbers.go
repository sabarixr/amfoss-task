package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	fmt.Print("Enter the value of n: ")
	scanner.Scan()
	input := scanner.Text()
	n, err := strconv.Atoi(input)

	if err != nil || n <= 0 {
		fmt.Println("Error: n must be a positive integer")
		return
	}

	fmt.Println("\nPrime numbers up to", n, ":")
	for num := 2; num <= n; num++ {
		isPrime := true
		for i := 2; i*i <= num; i++ {
			if num%i == 0 {
				isPrime = false
				break
			}
		}
		if isPrime {
			fmt.Println(num)
		}
	}
}

