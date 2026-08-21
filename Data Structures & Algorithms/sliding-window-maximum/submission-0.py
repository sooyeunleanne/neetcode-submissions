from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dq = deque() #store indices
        res = []

        for i in range(len(nums)):
            # remove smallest element from window:
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            # add current index in the deque:
            dq.append(i)

            # remove out of window index:
            if dq[0] == i - k:
                dq.popleft()
            
            # record result if window is valid:
            if i >= k - 1:
                res.append(nums[dq[0]])
        
        return res

