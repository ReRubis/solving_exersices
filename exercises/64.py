from ast import Num
from itertools import permutations


class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        grid_m = len(grid)
        # m - columns
        grid_n = len(grid[1])
        # n - rows
        number_of_possible_moves_m = []
        number_of_possible_moves_n = []

        for i in range(0, grid_m - 1):
            number_of_possible_moves_m.append(1)

        for i in range(0, grid_n - 1):
            number_of_possible_moves_n.append(2)
        amount_of_possible_moves = number_of_possible_moves_m + number_of_possible_moves_n

        list_of_possible_combinations = list(permutations(
            amount_of_possible_moves, len(amount_of_possible_moves)))

        list_of_results = []

        for i in range(len(list_of_possible_combinations)):
            result = grid[0][0]
            moved_right = 0
            moved_down = 0

            for k in range(len(list_of_possible_combinations[i])):

                if list_of_possible_combinations[i][k] == 1:
                    moved_down += 1
                    result = result + grid[moved_down][moved_right]
                else:
                    moved_right += 1
                    result = result + grid[moved_down][moved_right]

            list_of_results.append(result)

        return min(list_of_results)


answer = Solution
hey = answer.minPathSum(Solution, [[1, 2, 3], [4, 5, 6]])
print(hey)
