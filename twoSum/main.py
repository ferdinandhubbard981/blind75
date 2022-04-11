class Solution(object):
        
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if (complement in hashmap and hashmap[complement] != i):
                return [i, hashmap[complement]]
            
def main():
    instance = Solution()
    pointers = instance.twoSum([3,2,4], 6)
    print("pointer0: %d\n\n", pointers[0])
    print("pointer1: %d\n", pointers[1])

if __name__ == '__main__':
    main()