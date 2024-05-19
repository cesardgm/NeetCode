from typing import List

class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    # Checks whether integer list contains duplicates
    def containsDuplicates(a_list: List[int]) -> bool:
      a_set = set(a_list)
      return len(a_list) != len(a_set)

    # Reduces row, col, or box to an integer list
    def toIntegerList(a_list: List[str]) -> List[int]:
      int_list = [int(x) for x in a_list if x != "."]
      return int_list

    # Dictionary of lambda functions that generate each box within the sudoku grid
    def boxToList(board: List[List[str]], boxNum: int) -> List[int]:
      top_rows = range(0,3)
      mid_rows = range(3,6)
      bot_rows = range(6,9)

      lhs_cols = range(0,3)
      mid_cols = range(3,6)
      rhs_cols = range(6,9)

      switch = {
        0: lambda: [board[i][j] for i in top_rows for j in lhs_cols],
        1: lambda: [board[i][j] for i in top_rows for j in mid_cols],
        2: lambda: [board[i][j] for i in top_rows for j in rhs_cols],
        3: lambda: [board[i][j] for i in mid_rows for j in lhs_cols],
        4: lambda: [board[i][j] for i in mid_rows for j in mid_cols],
        5: lambda: [board[i][j] for i in mid_rows for j in rhs_cols],
        6: lambda: [board[i][j] for i in bot_rows for j in lhs_cols],
        7: lambda: [board[i][j] for i in bot_rows for j in mid_cols],
        8: lambda: [board[i][j] for i in bot_rows for j in rhs_cols],
      }

      # Given the desired box number, invoke corresponding lambda function
      box = switch[boxNum]()
      return box

    # Check rows are valid
    for row in board:
      int_row = toIntegerList(row)
      if containsDuplicates(int_row) == True:
        return False

    # Transpose board with zip() function
    columns = [list(col) for col in zip(*board)]
    # Check cols are valid
    for col in columns:
      int_col = toIntegerList(col)
      if containsDuplicates(int_col) == True:
        return False

    # Check boxes are valid
    for i in range(9):
      box = boxToList(board, i)
      int_box = toIntegerList(box)
      if containsDuplicates(int_box) == True:
        return False

    # If no objections thrown, then the board is valid
    return True
