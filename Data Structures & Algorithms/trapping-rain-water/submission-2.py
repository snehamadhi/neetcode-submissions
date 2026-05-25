class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        leftMax=height[left]
        rightMax=height[right]
        max_water=0
        while left<right:
            if height[left]<height[right]:
                left+=1
                leftMax=max(leftMax,height[left])
                max_water+=leftMax-height[left]
            else:
                right-=1
                rightMax=max(rightMax,height[right])
                max_water+=rightMax-height[right]
        return max_water