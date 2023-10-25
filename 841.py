rooms =[[1,3],[3,0,1],[2],[0]]
from collections import deque

n = len(rooms)
seen = deque()
num =0 
visited = [False for i in range(n)]
visited[0]  = True
seen.append(0)
while seen:
    neighborhood= seen.popleft()
    if rooms[neighborhood]:
        for x in rooms[neighborhood]:
            if visited[x] == False and x not in seen:
                seen.append(x)
                visited[x] = True

print(all(visited))