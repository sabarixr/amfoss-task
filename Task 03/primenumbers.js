const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Enter the value of n: ', (n) => {
  n = parseInt(n);

  if (isNaN(n) || n <= 0) {
    console.log('Error: n must be a positive integer');
    rl.close();
    return;
  }

  console.log(`\nPrime numbers up to ${n}:`);

  if (n >= 2) {
    console.log(2);
  }

  for (let num = 3; num <= n; num += 2) {
    let isPrime = true;
    for (let i = 3; i * i <= num; i += 2) {
      if (num % i === 0) {
        isPrime = false;
        break;
      }
    }
    if (isPrime) {
      console.log(num);
    }
  }

  rl.close();
});

