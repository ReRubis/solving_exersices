class Solution:
    def rotate(self, nums: list[int], k: int) -> None:

        for i in range(k):
            number_to_move = nums.pop(len(nums)-1)
            nums.insert(0, number_to_move)

        return nums


answer = Solution
hey = answer.rotate(Solution, [1, 2, 3, 4, 5, 6, 7], 3)
print(hey)
