def getNeighbours(grid, r, c):
    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr, nc = r+dr, c+dc
        if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] != W:
            yield (nr, nc)

def buildPath(cameFrom, goal):
    path, node = [], goal
    while node in cameFrom: path.append(node); node = cameFrom[node]
    path.append(node); path.reverse(); return path

def runAstar(grid, start, goal, hFn):
    openSet, cameFrom, gScore, visited, steps = [], {}, {start: 0}, set(), []
    heapq.heappush(openSet, (0, 0, start))
    while openSet:
        _, g, cur = heapq.heappop(openSet)
        if cur in visited: continue
        visited.add(cur)
        steps.append((frozenset(item[2] for item in openSet), frozenset(visited), None))
        if cur == goal:
            steps.append((frozenset(), frozenset(visited), buildPath(cameFrom, goal))); return steps
        for nb in getNeighbours(grid, *cur):
            newG = g + 1
            if newG < gScore.get(nb, float("inf")):
                gScore[nb] = newG; cameFrom[nb] = cur
                heapq.heappush(openSet, (newG + hFn(nb, goal), newG, nb))
    steps.append((frozenset(), frozenset(visited), [])); return steps
