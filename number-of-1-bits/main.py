# ACCEPTED
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # for every bit in number
            # shift to the right by i bits
            # if result & 1 then    
                # hammingweight++
        hammingWeight = 0
        for i in range(32):
            if  (n >> i) & 1:
                hammingWeight += 1
        return hammingWeight

        

def main():
    num = 7
    instance = Solution()
    result = instance.hammingWeight(num)
    print(result)

if __name__ == "__main__":
    main()