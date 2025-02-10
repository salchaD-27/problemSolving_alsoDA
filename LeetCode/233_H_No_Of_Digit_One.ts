function countDigitOne(n: number): number {
    let count = 0;
    let factor = 1;
    while (factor <= n) {
        let higher = Math.floor(n / (factor * 10));
        let current = Math.floor((n / factor) % 10);
        let lower = n % factor;
        if (current === 0) {count += higher * factor;}
        else if (current === 1) {count += higher * factor + lower + 1;}
        else{count += (higher + 1) * factor;}
        factor *= 10;
    }
    return count;
}