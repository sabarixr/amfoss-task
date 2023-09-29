use std::io;

fn main() {
    let mut input = String::new();

    println!("Enter the value of n: ");
    io::stdin()
        .read_line(&mut input)
        .expect("Failed to read line");

    let n: u32 = match input.trim().parse() {
        Ok(num) if num > 0 => num,
        _ => {
            println!("Error: n must be a positive integer");
            return;
        }
    };

    println!("\nPrime numbers up to {}:", n);

    if n >= 2 {
        println!("2");
    }

    for num in (3..=n).step_by(2) {
        let mut is_prime = true;
        for i in (3..=(num as f64).sqrt() as u32 + 1).step_by(2) {
            if num % i == 0 {
                is_prime = false;
                break;
            }
        }
        if is_prime {
            println!("{}", num);
        }
    }
}

