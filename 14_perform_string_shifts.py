#contest url : https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3299/

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        
        def rotateLeft(word, d): 
            leftfirst = word[0 : d] 
            leftsecond = word[d :] 
            return (leftsecond + leftfirst)

        def rotateRight(word, d):
            rightfirst = word[0 : len(word)-d] 
            rightsecond = word[len(word)-d : ] 
            return (rightsecond + rightfirst)
        
        for i in range (len(shift)):
            d = shift[i][1]%len(s)
            if shift[i][0] == 1:
                s = rotateRight(s, d)
            else:
                s = rotateLeft(s, d)
        
        return s