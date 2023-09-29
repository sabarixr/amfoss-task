defmodule PrimeNumbers do
  def is_prime(2), do: true
  def is_prime(n) when n <= 1 or rem(n, 2) == 0, do: false
  def is_prime(n) do
    is_prime(n, 3)
  end

  defp is_prime(n, divisor) when divisor * divisor > n, do: true
  defp is_prime(n, divisor) when rem(n, divisor) == 0, do: false
  defp is_prime(n, divisor) do
    is_prime(n, divisor + 2)
  end

  def find_primes_upto(n) when n < 2, do: []
  def find_primes_upto(n) do
    Enum.filter(2..n, &is_prime/1)
  end
end

IO.puts("Enter a number (n):")
n_input = IO.gets("")

# Remove the trailing newline character from the input
n = String.trim(n_input) |> String.to_integer()

if n < 2 do
  IO.puts("There are no prime numbers less than 2.")
else
  prime_numbers = PrimeNumbers.find_primes_upto(n)
  IO.puts("Prime numbers up to #{n}: #{inspect(prime_numbers)}")
end

