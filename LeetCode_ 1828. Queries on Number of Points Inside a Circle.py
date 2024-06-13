#-- Pb 
https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/description/


#-- Sol
class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        import numpy as np 

        def cal(x,y,r):
            cnt = 0
            for point in points:
                distance = np.sqrt((point[0]-x)**2 + (point[1] - y)**2)
                
                if distance <= r : 
                    cnt+=1
            return cnt    
        
        #--- 
        output = []
        for que in queries:
            x,y,z = que[0],que[1],que[2]
            result = cal(x,y,z)
            output.append(result)
        
        return output

#-- Optimized Sol
    return [sum((x-a)**2 + (y-b)**2 <= r**2 for x,y in points) for a,b,r in queries]

