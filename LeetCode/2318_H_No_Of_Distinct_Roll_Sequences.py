def gcd(a, b):
    for i in range(a if a<b else b, 0, -1): 
        if(a%i==0 and b%i==0): return i

def formSeq(arr, valsToAdd):
    if(valsToAdd==0): return 1
    
    eligibleVals=[1,2,3,4,5,6]
    for val in eligibleVals:
        if (gcd(val, arr[-1]) != 1 or (len(arr) >= 3 and arr[-3] == val)): eligibleVals.remove(val)
    for val in eligibleVals:
        formSeq(arr.append(val), valsToAdd-1)

def distinctSequences(n):
    validSeqCount=0
    for i in range(1, 7):
        validSeq=[]
        validSeq.append(i)
        validSeqCount+=formSeq(validSeq, n-1)
    return validSeqCount


# print(distinctSequences(6))