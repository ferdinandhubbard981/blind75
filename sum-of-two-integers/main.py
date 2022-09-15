

from codecs import charmap_build


class Solution(object):
    def getXBinDigit(self, x: int, num: int):
        return (num >> x) & 1

    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        rval = 0
        carryVal = 0
        for i in range(10):

            # if three 1's then rval and carry
            # if two ones then carry
            # if 1 one then rval
            bit1, bit2 = self.getXBinDigit(i, a), self.getXBinDigit(i, b) 
            if bit1 & bit2 & carryVal:
                rval = rval | 1 << i
                carryVal = 1
            elif bit1 & bit2 | bit1 & carryVal | bit2 & carryVal:
                carryVal = 1
            elif bit1 | bit2 | carryVal:
                rval = rval | 1 << i
                carryVal = 0
        return rval

        


def main():
    instance = Solution()
    print(instance.getSum(-5, -5))

if __name__ == "__main__":
    main()