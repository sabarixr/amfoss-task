document.getElementById('primebtn').addEventListener('click', function() {
    let n = parseInt(document.getElementById('noInput').value);
    
    for (let s = 2; s <= n; s++) {
        let isPrime = true;
        
        for (let q = 2; q <= (s / 2) + 1;) {
            if (s % q == 0 && s != q)  {
                isPrime = false;
                break;
            }
        }
        
        if (isPrime) {
            console.log(s);
        }
    }
});
