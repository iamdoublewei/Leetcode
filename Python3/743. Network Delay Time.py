'''
There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

Note:
N will be in the range [1, 100].
K will be in the range [1, N].
The length of times will be in the range [1, 6000].
All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 1 <= w <= 100.
'''

class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        graph = collections.defaultdict(list)
        for (u, v, w) in times:
            graph[u].append([v, w])
        minpq, visited = [[0, K]], {}
        visited = {}
        while minpq:
            dis, node = heapq.heappop(minpq)
            if node in visited: continue
            visited[node] = dis
            for v, w in graph[node]:
                if v not in visited:
                    heapq.heappush(minpq, [dis + w, v])
        return max(visited.values()) if len(visited) == N else -1