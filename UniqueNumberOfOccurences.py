"""
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

 

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
 

Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000

"""

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        # [1, 1, 2, 4, 4, 4, 7, 7, 7, 7]
        # 1 = 2
        # 2 = 1
        # 4 = 3
        # 7 = 4

        
        numMap = {}
        
        for n in arr:
            if n not in numMap:
                numMap[n] = 1
            else:
                numMap[n] += 1
        
        freq = []
        curr_count = 0

        for number in numMap:
            freq.append(numMap[number])
        
        freq.sort()
        curr_freq = 0
        for freq in freq:
            if freq == curr_freq:
                return False
            else:
                curr_freq = freq
        return True