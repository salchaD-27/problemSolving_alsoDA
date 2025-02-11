// function isUgly(num: number): boolean {
//     if (num <= 0) return false;
//     while (num % 2 === 0) num /= 2;
//     while (num % 3 === 0) num /= 3;
//     while (num % 5 === 0) num /= 5;
//     return num === 1;
// }
// function nthUglyNumber(n: number): number {
//     let numsFound = 0, i = 1;
//     while (true) {
//         if (isUgly(i)) {
//             numsFound++;
//             if (numsFound === n){return i;}
//         }
//         i++;
//     }
// }

function nthUglyNumber(n: number): number {
    const uglyNumbers = [1];
    let i2 = 0, i3 = 0, i5 = 0;
    let next2 = 2, next3 = 3, next5 = 5;
    for (let i = 1; i < n; i++) {
        const nextUgly = Math.min(next2, next3, next5);
        uglyNumbers.push(nextUgly);
        if (nextUgly === next2) {
            i2++;
            next2 = uglyNumbers[i2] * 2;
        }
        if (nextUgly === next3) {
            i3++;
            next3 = uglyNumbers[i3] * 3;
        }
        if (nextUgly === next5) {
            i5++;
            next5 = uglyNumbers[i5] * 5;
        }
    }
    return uglyNumbers[n - 1];
}