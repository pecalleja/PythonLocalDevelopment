from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_not_under_attack(row, col):
            return not (cols[col] or hill[row - col] or dale[row + col])

        def place_queen(row, col):
            queens.add((row, col))
            cols[col] = 1
            hill[row - col] = 1
            dale[row + col] = 1

        def remove_queen(row, col):
            queens.remove((row, col))
            cols[col] = 0
            hill[row - col] = 0
            dale[row + col] = 0

        def add_solution():
            solution = []
            for _, col in sorted(queens):
                solution.append('.' * col + 'Q' + '.' * (n - col - 1))
            output.append(solution)

        def backtrack(row):
            for col in range(n):
                if is_not_under_attack(row, col):
                    place_queen(row, col)
                    if row + 1 == n:
                        add_solution()
                    else:
                        backtrack(row + 1)
                    remove_queen(row, col)

        cols = [0] * n
        hill = [0] * (2 * n - 1)
        dale = [0] * (2 * n - 1)
        queens = set()
        output = []
        backtrack(0)
        return output
