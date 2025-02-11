function inStr(s: string, part: string): boolean{
    let L:number=0, R:number=part.length-1
    while(R<s.length){
        let temp=s.slice(L,R+1)
        if(temp===part){return true}
        L++
        R++
    }
    return false
}
function removeOccurrences(s: string, part: string): string {
    while(inStr(s, part)){
        let L:number=0, R:number=part.length-1
        while(R<s.length){
            let temp=s.slice(L,R+1)
            if(temp===part){
                s=s.slice(0, L) + s.slice(R+1, s.length)
                break;
            }
            L++
            R++
        }
    }
    return s;
};