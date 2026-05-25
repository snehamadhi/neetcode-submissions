class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        max_val=0
        while l<r:
            width=r-l
            height=min(heights[l],heights[r])
            cur_val=width*height
            max_val=max(cur_val,max_val)

            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return max_val