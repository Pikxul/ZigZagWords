# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
# (you may want to display this pattern in a fixed font for better legibility)
#  Example :
#  Input: s = "PAYPALISHIRING", numRows = 4
#  Output: "PINALSIGYAHRPI"
#  Explanation:
#  P     I    N
#  A   L S  I G
#  Y A   H R
#  P     I


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
    
        rows = [""] * numRows
        index, step = 0,1

        for char in s:
            rows[index] += char

            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1

            index += step

        return "".join(rows)