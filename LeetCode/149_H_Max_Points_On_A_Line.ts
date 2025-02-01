// function maxPoints(points: number[][]): number {
//     if(points.length===1){return 1;}
//     points.sort((a, b) => a[0] - b[0]);
//     let lastSlope: number = (points[1][1]-points[0][1])/(points[1][0]-points[0][0])
//     let lastSlopePoints: number = 2
//     let ans: number =2;
//     let i:number;
//     for(i=2; i<points.length; i++){
//         let tempLastSlope: number = (points[i][1]-points[i-1][1])/(points[i][0]-points[i-1][0]);
//         if(tempLastSlope===lastSlope){lastSlopePoints++;}
//         else{
//             lastSlope=tempLastSlope;
//             lastSlopePoints=2;
//         }
//         ans=(ans>lastSlopePoints?ans:lastSlope);
//     }
//     return ans+2;
// };

function getGCD(a: number, b: number): number{return b === 0 ? a : getGCD(b, a % b);}
function maxPoints(points: number[][]): number {
    if (points.length === 1) return 1;
    points.sort((a, b) => a[0] - b[0]);
    let ans = 2;
    let i: number, j: number;
    for (i = 0; i < points.length; i++) {
        let count = 1;
        let slopeMap = new Map<string, number>();
        for (j = i + 1; j < points.length; j++) {
            let dx = points[j][0] - points[i][0];
            let dy = points[j][1] - points[i][1];
            let gcd = getGCD(dx, dy);
            let slope = `${dy / gcd}/${dx / gcd}`;
            slopeMap.set(slope, (slopeMap.get(slope) || 1) + 1);
            count = Math.max(count, slopeMap.get(slope) || 1);
        }
        ans = Math.max(ans, count);
    }
    return ans;
}