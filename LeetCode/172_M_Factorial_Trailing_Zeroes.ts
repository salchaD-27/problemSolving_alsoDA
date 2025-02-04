// function fact(n: number): number{
//     if(n==0 || n==1){return 1}
//     return n*fact(n-1)
// }
// function trailingZeroes(n: number): number {
//     let count:number=0
//     let strN: string = fact(n).toString()
//     for(let i=strN.length-1; i>=0; i--){
//         if(strN[i]=='0'){count++}
//         else{break;}
//     }
//     return count
// };

function trailingZeroes(n: number): number {
    let count = 0;
    while (n >= 5) {
        n = Math.floor(n / 5);
        count += n;
    }
    return count;
}
