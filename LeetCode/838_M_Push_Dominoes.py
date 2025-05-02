class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        forces = [0] * n        
        # left to right
        force = 0
        for i in range(n):
            if dominoes[i] == 'R': force = n
            elif dominoes[i] == 'L': force = 0
            else: force = max(force - 1, 0)
            forces[i] += force # right force +ve
        # right to left
        force = 0
        for i in range(n - 1, -1, -1):
            if dominoes[i] == 'L': force = n
            elif dominoes[i] == 'R': force = 0
            else: force = max(force - 1, 0)
            forces[i] -= force  # left force -ve
        result = []
        for f in forces:
            if f == 0: result.append('.')
            elif f > 0: result.append('R')
            else: result.append('L')
        return ''.join(result)