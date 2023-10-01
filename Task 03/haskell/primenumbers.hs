
isPrime :: Int -> Bool
isPrime n
    | n <= 1 = False
    | n == 2 = True
    | otherwise = all (\x -> n `mod` x /= 0) [2..isqrt n]
    where isqrt = floor . sqrt . fromIntegral

generatePrimesUpTo :: Int -> [Int]
generatePrimesUpTo n = filter isPrime [2..n]

main :: IO ()
main = do
    putStrLn "Enter the value of n: "
    input <- getLine
    let n = read input :: Int

    if n <= 0
        then putStrLn "Error: n must be a positive integer"
        else do
            let primes = generatePrimesUpTo n
            putStrLn "\nPrime numbers up to n:"
            mapM_ print primes

