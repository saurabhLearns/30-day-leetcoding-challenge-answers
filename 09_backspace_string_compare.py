#contest url : https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-2/3291/
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        S_changed, T_changed = '', ''
        
        for i in range(len(S)):
            if S[i] == '#':
                S_changed = S_changed[:-1]
            else:
                S_changed+= S[i]
                
        for i in range(len(T)):
            if T[i] == '#':
                T_changed = T_changed[:-1]
            else:
                T_changed+= T[i]

        if S_changed == T_changed:
            return True
        else:
            return False
        