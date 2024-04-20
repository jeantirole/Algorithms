316. Remove Duplicate Letters

Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is 
the smallest in lexicographical order
 among all possible results.



Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.


# Sol 
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        import string

        alpha_dict = string.ascii_lowercase
        Q = defaultdict()
        for i, al in enumerate(alpha_dict):
            Q[al] = i 

        D = defaultdict()


        min = 999999
        for point, char in enumerate(s):
            

            if char not in D.keys():
                D[char] = point
                asci_n = Q[char]
                
                if min > asci_n:
                    min = asci_n  

            else:
                asci_n = Q[char]
                
                if min > asci_n:
                    min = asci_n
                

                elif min < asci_n:
                    D[char] = point
            
            
        a = sorted(D.items(), key=lambda item: item[1])
        a_ = [str(i[0]) for i in a]
        str_ = ""
        for k in a_:
            str_ += k

        return str_        
        


# Sol 
https://leetcode.com/problems/remove-duplicate-letters/solutions/4090711/98-53-stack-and-greedy/
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set() 
        last_occ = {c: i for i, c in enumerate(s)}
        
        for i, c in enumerate(s):
            if c not in seen:
                
                while stack and c < stack[-1] and i < last_occ[stack[-1]]:
                    seen.discard(stack.pop())
                seen.add(c)
                stack.append(c)
        
        return ''.join(stack)
     
    
