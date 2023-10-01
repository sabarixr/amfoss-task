def prime_numbers(max)
  primes = []

  for i in (2..max) do
    is_prime = true
    for j in (2..Math.sqrt(i).to_i) do
      if i % j == 0
        is_prime = false
        break
      end
    end
    primes << i if is_prime
  end

  primes
end

def first_n_primes(n)
  raise "n must be an integer" unless n.is_a? Integer
  raise "n must be greater than 0" if n <= 0

  prime_numbers(n)
end

# Input
print "Enter the value of n: "
n = gets.chomp.to_i

# Output
result = first_n_primes(n)
puts "The first #{n} prime numbers are: #{result.join(', ')}"

