function twoSum(numbers: number[], target: number): number[] {
	for(let i=0; i<numbers.length-1; i++){
		let temp=target-numbers[i]
		for(let j=i+1; j<numbers.length; j++){
			if(numbers[j]==temp){return [i+1, j+1]}
		}
	}
};