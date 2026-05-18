class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        leftmax=height[left]
        rightmax=height[right]
        water=0
        while left<right:
            if height[left]<height[right]:
                left+=1
                if height[left]<leftmax:
                    water+=leftmax-height[left]
                else:
                    leftmax=height[left]
            else:
                right-=1
                if height[right]<rightmax:
                    water+=rightmax-height[right]
                else:
                    rightmax=height[right]
        return water