# Problem -----------------------------------

https://leetcode.com/problems/decode-string/description/

394. Decode String

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"


# Solution --------------------------------------
https://leetcode.com/problems/decode-string/solutions/1834124/394-decode-string/


    for value in s:
        if value is "[":
            stack.append(value)
        elif value is "]":
            # get encoded string
            while stack and stack[-1]!='[':
                res.append(stack.pop())
            stack.pop()  
            # get the number k
            while stack:
                if stack[-1].isnumeric(): 
                    number.append(stack.pop())
                else:
                    break
            # decode string and add it back to the stack
            number = number[::-1]
            iterator = int("".join(number))
            res = res[::-1] * iterator
            stack.extend(res) 
            # reset all variables for next run
            res = []
            number = []
        else:
            stack.append(value)
    return "".join(stack)
            
