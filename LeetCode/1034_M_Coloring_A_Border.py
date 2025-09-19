class Solution:
    def colorBorder(self, grid, r0, c0, color):
        m, n = len(grid), len(grid[0])
        bfs, component, border = [[r0, c0]], set([(r0, c0)]), set()
        for r0, c0 in bfs:
            for i, j in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                r, c = r0 + i, c0 + j
                if 0 <= r < m and 0 <= c < n and grid[r][c] == grid[r0][c0]:
                    if (r, c) not in component:
                        bfs.append([r, c])
                        component.add((r, c))
                else: border.add((r0, c0))
        for x, y in border: grid[x][y] = color
        return grid