class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        for i in nums:
            if i == 0:
                nums.remove(i)
                nums.append(0)
                print(nums)


answer = Solution
hey = answer.moveZeroes(Solution, [0, 1, 0, 3, 12])
print(hey)
