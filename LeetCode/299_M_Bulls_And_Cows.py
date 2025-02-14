# func getHint(secret string, guess string) string {
# 	x:=0
# 	bulls= make([]int, 0)
# 	y:=0
# 	for i:=0; i<len(secret); i++{
# 		if(secret[i]==guess[i]){
# 			x++
# 			bulls = append(bulls, i)
# 		}
# 	}
# 	for i:=0; i<len(secret); i++{if(!slices.Contains(bulls, i) && string.Contains(secret, guess[i])){y++}}
# 	return x+'A'+y+'B'
# }

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        x, y = 0, 0
        secrets = list(secret)
        guesses = list(guess) 
        for i in range(len(secrets)):
            if secrets[i] == guesses[i]:
                x += 1
                secrets[i] = guesses[i] = None
        for i in range(len(secrets)):
            if secrets[i] is not None and secrets[i] in guesses:
                y += 1
                guesses[guesses.index(secrets[i])] = None
        return f"{x}A{y}B"