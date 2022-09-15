# ACCEPTED
import math
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # n r
        # 1 1
        # 2 2
        # 3 3
        # 4 

        # find num combinations
        # for every combination:
            # find all permutations
        total = 0
        numcombinations = (int)((n- n%2) / 2) + 1 
        for i in range(numcombinations):
            numOfTwos = i
            arrLen = n - i
            numPermutations = comb(arrLen, numOfTwos)
            total += numPermutations
            # number of twos choose len
        return total

def comb(n, r):
    return (int)(math.factorial(n) / (math.factorial(n-r)* math.factorial(r)))

def main():
    instance = Solution()
    input = 3
    print(instance.climbStairs(input))

if __name__ == "__main__":
    main()