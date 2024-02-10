# Problem ------------------------------
125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/description/?envType=study-plan-v2&envId=top-interview-150

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.


Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 


# Solution -----------------------------
class Solution:
    def isPalindrome(self, s: str) -> bool:
  
        s = re.sub('[^a-zA-Z]', ' ', s)
        s = s.replace(" ","")
        s = s.lower()

        if len(s) ==1:
            return True

        if len(s) ==2:
            h1_ = s[0]
            h2_ = s[1]
            print("s2",s)

            if h1_ == h2_:
                return True 


        mid = len(s)//2
        h1 = s[:mid]
        h2 = s[mid+1:]
        reversed_list = h2[::-1]


        print(h1)
        print(reversed_list)
        
        if h1 == reversed_list:
            return True
        
