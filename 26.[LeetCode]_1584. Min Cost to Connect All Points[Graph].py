#------------------ Problem 
# 1554.Min Cost to Connect All Points 
# https://leetcode.com/problems/min-cost-to-connect-all-points/description/






#------------------ Solution
# should be updated
# Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20

points = [[0,0],[2,2],[3,10],[5,2],[7,0]]

result= []
for i in range(len(points)):
    p = points[i]
    x = p[0]
    y = p[1]
    
    min = 999999999999
    smallest_ = 0 
    for k in range(len(points)):
        
        x_ = points[k][0]
        y_ = points[k][1]

        distance = abs(x - x_) + abs(y - y_)
        
        if distance > 0:
            if distance < min:
                min = distance
                
                smallest_ = k 
               
    #---
    result.append([i,smallest_,min])
                

for i in range(result.__len__()):
    edge = result[i]

    for k in range(result.__len__()):
        if i != k:
            
            if sorted(edge[0:2]) == (result[k][0:2]):
                print(k)
                _ = result.pop(k)
                

print("result : ", result)
