import pytest


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        list = ["" for row in range(numRows)]
        row = 0
        rowDelta = 1
        for c in s:
            list[row] += c
            if row == 0:
                rowDelta = 1
            elif row == numRows - 1:
                rowDelta = -1
            row = row + rowDelta
        return "".join(list)


test_data = [
    ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
    ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
    ("A", 1, "A"),
]


@pytest.mark.parametrize("s,num_rows,expected", test_data)
def test_all(s, num_rows, expected):
    assert expected == Solution().convert(s, num_rows)
