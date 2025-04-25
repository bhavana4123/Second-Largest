class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        self.arr = arr
        if len(arr)<2:
            return None
        first = second = float('-inf')
        for num in arr:
            if num>first:
                second = first
                first = num
            elif first>num>second:
                second = num
        return second if second!= float('-inf') else -1
num = Solution()
print(num.getSecondLargest([4,4,3,2,1]))