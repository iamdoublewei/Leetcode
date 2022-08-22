'''
Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

 

Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it was not in the typed output.
 

Constraints:

1 <= name.length, typed.length <= 1000
name and typed consist of only lowercase English letters.
'''

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = j = 0
        pre = name[0]
        
        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                pre = name[i]
                i += 1
                j += 1
            elif typed[j] == pre:
                j += 1
            else:
                return False
            
        if i < len(name):
            return False
        
        while j < len(typed):
            if typed[j] != pre:
                return False
            else:
                j += 1
            
        return True