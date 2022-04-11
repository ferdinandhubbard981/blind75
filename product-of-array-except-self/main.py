from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [None]*len(nums)
        output[0] = 1
        # mult by all element to the left of each element
        for idx in range(len(nums))[1:]:
            output[idx] = output[idx-1] * nums[idx-1]
        # mult by all element to the right of each element
        multiplier: int = 1
        iteration = list(range(len(nums)))
        iteration.reverse()
        for idx in iteration:
            output[idx] *= multiplier
            multiplier *= nums[idx]
        # order 2O(n)
        return output
            
            
if __name__ == "__main__":
    input = [1,2,3,4]
    print(Solution.productExceptSelf(Solution, input))