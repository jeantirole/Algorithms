#--------------------- Problem
https://leetcode.com/problems/maximal-network-rank/description/

1615. Maximal Network Rank

There is an infrastructure of n cities with some number of roads connecting these cities. Each roads[i] = [ai, bi] indicates that there is a bidirectional road between cities ai and bi.

The network rank of two different cities is defined as the total number of directly connected roads to either city. If a road is directly connected to both cities, it is only counted once.

The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities.

Given the integer n and the array roads, return the maximal network rank of the entire infrastructure.

 
Example 1:

Input: n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
Output: 4
Explanation: The network rank of cities 0 and 1 is 4 as there are 4 roads that are connected to either 0 or 1. The road between 0 and 1 is only counted once.


#--------------------- Solution

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        g=[[False]*n for _ in range(n)]
        for x,y in roads:
            g[x][y]=g[y][x]=True

        ans=0
        for i in range(n):
            for j in range(n):
                if i==j:
                    continue

                cur=0
                for k in range(n):
                    if k!=i and k!=j:
                        if g[i][k]:
                            cur+=1

                        if g[j][k]:
                             cur+=1

                if g[i][j]:
                    cur+=1

                ans=max(cur,ans)

        return ans             
