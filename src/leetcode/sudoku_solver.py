class Solution:
    def solveSudoku(self, board):
        """
        Modify board in-place to solve the Sudoku puzzle.
        """

        # Data structures to keep track of used digits
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Initialize our records of used digits from the current board
        for r in range(9):
            for c in range(9):
                char = board[r][c]
                if char != '.':
                    d = int(char)
                    rows[r].add(d)
                    cols[c].add(d)
                    box_index = (r // 3) * 3 + (c // 3)
                    boxes[box_index].add(d)

        # Helper function to get the box index
        def box_index(r, c):
            return (r // 3) * 3 + (c // 3)

        # Backtracking function
        def backtrack(r, c):
            # If we've gone past the last column, move to next row
            if c == 9:
                r += 1
                c = 0
                # If we've filled all rows, sudoku is solved
                if r == 9:
                    return True

            # If this cell is already filled, move on to the next cell
            if board[r][c] != '.':
                return backtrack(r, c + 1)

            # Try placing digits 1 through 9
            for d in range(1, 10):
                if (
                    d not in rows[r]
                    and d not in cols[c]
                    and d not in boxes[box_index(r, c)]
                ):
                    # Place the digit
                    board[r][c] = str(d)
                    rows[r].add(d)
                    cols[c].add(d)
                    boxes[box_index(r, c)].add(d)

                    # Recurse
                    if backtrack(r, c + 1):
                        return True

                    # Undo the placement
                    board[r][c] = '.'
                    rows[r].remove(d)
                    cols[c].remove(d)
                    boxes[box_index(r, c)].remove(d)

            # If no digit 1-9 can be placed here, backtrack
            return False

        backtrack(0, 0)
