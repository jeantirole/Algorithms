#--- Pb 
2610. Convert an Array Into a 2D Array With Conditions

You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:

The 2D array should contain only the elements of the array nums.
Each row in the 2D array contains distinct integers.
The number of rows in the 2D array should be minimal.
Return the resulting array. If there are multiple answers, return any of them.

Note that the 2D array can have a different number of elements on each row.

#--- Sol 
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        import numpy as np 
        import collections

        dict_ = collections.defaultdict()
        row_ = [] 
        matrix_ = []
      
        while True:
            len_ = len(nums)
            for _ in range(len_):    
                
                n = nums.pop(0)
                print(n)
                if n not in dict_.keys():
                    dict_[n] = 1
                    row_.append(n)
                elif n in dict_.keys():
                    nums.append(n)
                
            #--
            matrix_.append(row_)

            # init
            row_ = []
            dict_ = collections.defaultdict()

            #print(matrix_)
            if len(nums) == 0 :
                break

        return matrix_

#--- Points
1. 배열에 for문으로 접근하였을 때, for n in nums: 와 같이,, for문이 실행되면서 nums 의 데이터가 버퍼에 위치한 인덱스를 기준으로 실행된다. 
  따라서 nums.pop(0)을 사용하였을 때, pop 이후의 0 index 가 아니라, 1 index 를 버퍼에서 가져오면서 순서대로 데이터 조회가 되지 않는다. 
2. for 문이 아니라, for _ in range(len(nums)): 를 활용해서 전체적인 반복횟수(초기에 조회하고 싶은 양 만큼의 값만 정해줌) 에다가 실행을 시켰다. 
3. stack 풀이법으로 풀었음 

                
    
        
        
