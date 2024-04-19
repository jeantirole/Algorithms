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

s = "bcabc"
#Output: "abc"
from collections import defaultdict
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
         D[char] = asci_n
      
a = sorted(D.items(), key=lambda item: item[1])
     
    
