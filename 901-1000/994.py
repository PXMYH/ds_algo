import collections

class Solution(object):
    def orangesRotting(self, grid):
        R, C = len(grid), len(grid[0])

        # queue - all starting cells with rotting oranges
        queue = collections.deque()
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 2:
                    queue.append((r, c, 0))

        def neighbors(r, c):
            for nr, nc in ((r-1,c),(r,c-1),(r+1,c),(r,c+1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        d = 0
        while queue:
            r, c, d = queue.popleft()
            for nr, nc in neighbors(r, c):
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append((nr, nc, d+1))

        if any(1 in row for row in grid):
            return -1
        return d


# driver code
grid_1 = [[2,1,1],[1,1,0],[0,1,1]]
grid_2 = [[2,1,1],[0,1,1],[1,0,1]]
grid_3 = [[0,2]]
s = Solution()
time_to_rot_1 = s.orangesRotting(grid_1)
time_to_rot_2 = s.orangesRotting(grid_2)
time_to_rot_3 = s.orangesRotting(grid_3)

print(f"It takes {time_to_rot_1} minutes to rot the oranges in {grid_1}")
print(f"It takes {time_to_rot_2} minutes to rot the oranges in {grid_2}")
print(f"It takes {time_to_rot_3} minutes to rot the oranges in {grid_3}")
