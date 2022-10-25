class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:

        for i in range(len(nums)):
            print(nums[i])
            nums[i] = nums[i]**2
            print(nums[i])
        nums.sort()
        return nums


answer = Solution
hey = answer.sortedSquares(Solution, [-4, -1, 0, 3, 10])
print(hey)
