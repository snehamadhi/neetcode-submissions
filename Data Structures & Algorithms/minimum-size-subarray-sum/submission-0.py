class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        win_sum=0
        min_len=float('inf')
        for right in range(len(nums)):
            win_sum+=nums[right]
            while win_sum>=target:
                min_len=min(min_len,right-left+1)
                win_sum -= nums[left]
                left += 1
        if min_len == float('inf'):
            return 0
        else:
            return min_len