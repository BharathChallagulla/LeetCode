import collections


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                curr_val = board[r][c]
                if curr_val != ".":
                    if ((curr_val in row[r]) or (curr_val in col[c]) or (curr_val in squares[(r//3, c//3)])):
                        return False
                    row[r].add(curr_val)
                    col[c].add(curr_val)
                    squares[(r//3, c//3)].add(curr_val)
        return True