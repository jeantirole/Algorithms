# Pb 
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]


# Sol
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        if not digits:
            return result
        
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        def backtrack(index, current_combination):
            nonlocal result
            if index == len(digits):
                result.append(current_combination)
                return
            
            digit = digits[index]
            letters = mapping[digit]
            for letter in letters:
                backtrack(index + 1, current_combination + letter)
        
        backtrack(0, "")
        return result
