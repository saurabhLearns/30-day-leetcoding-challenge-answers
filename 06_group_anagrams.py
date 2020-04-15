#contest url : https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3288/
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        listAnagram = collections.defaultdict(list)
        for i in strs:
            listAnagram[tuple(sorted(i))].append(i)

        return listAnagram.values()