function digitsSum(n: number): number {
    let ans = 0;
    while (n > 0) {
        ans += n % 10;
        n = Math.floor(n / 10);
    }
    return ans;
}
function maximumSum(nums: number[]): number {
    let sum: number = -1;
    let map = new Map<number, number[]>();
    for (let num of nums) {
        let sumDigits = digitsSum(num);
        if (!map.has(sumDigits)) {map.set(sumDigits, []);}
        map.get(sumDigits)!.push(num);
    }
    for (let values of map.values()) {
        if (values.length > 1) {
            values.sort((a, b) => b - a); 
            sum = Math.max(sum, values[0] + values[1]);
        }
    }
    return sum;
}