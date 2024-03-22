# Problem -------------------------------------
https://leetcode.com/problems/baseball-game/

682. Baseball Game

You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

An integer x.
Record a new score of x.
'+'.
Record a new score that is the sum of the previous two scores.
'D'.
Record a new score that is the double of the previous score.
'C'.
Invalidate the previous score, removing it from the record.
Return the sum of all the scores on the record after applying all the operations.

The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.

 
Example 1:

Input: ops = ["5","2","C","D","+"]
Output: 30
Explanation:
"5" - Add 5 to the record, record is now [5].
"2" - Add 2 to the record, record is now [5, 2].
"C" - Invalidate and remove the previous score, record is now [5].
"D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
"+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
The total sum is 5 + 10 + 15 = 30.


# Solution ---------------------------------------


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


operations = ["5","2","C","D","+"]

total_sum = 0

stack_ = [0,0]

prev = 0
prev_prev = 0 

while operations:
    
    curr = operations.pop(0)

    #aa = int(curr)

    if is_int(curr):
        stack_.insert(0, int(curr) ) 
    
    if curr =='+':
        ww = prev_prev + prev
        total_sum += ww
        stack_.insert(0,ww)
        
    if curr =="D":
        tmp = 2 * prev
        total_sum += tmp
        stack_.insert(0,tmp)
    
    if curr=="C":
        stack_.pop(0)
    
    
    #--- 
    prev_prev = stack_[1]    
    prev = stack_[0]
    
    result = sum(stack_)

print(result)







