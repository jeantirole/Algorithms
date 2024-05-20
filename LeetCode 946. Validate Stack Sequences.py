#--- Pb 
946. Validate Stack Sequences
Medium


Example 1:

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4),
pop() -> 4,
push(5),
pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
Example 2:

Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.






#--- Sol 
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        a = deque([])
        j = 0
        for i in range(len(pushed)):
            a.appendleft(pushed[i])
            while(a and a[0] == popped[j]):
                a.popleft()
                j+=1
        return not a
