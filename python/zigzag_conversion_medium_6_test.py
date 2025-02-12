import pytest


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        list = []
        for row in range(numRows):
            list.append("")
        row = 0
        goingUpwards = False
        for c in s:
            list[row] += c
            if row == 0:
                goingUpwards = False
                row = row + 1
            elif row == numRows - 1:
                goingUpwards = True
                row = row - 1
            elif goingUpwards:
                row = row - 1
            elif not goingUpwards:
                row = row + 1
        out = ""
        for sub in list:
            out += sub
        return out


test_data = [
    ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
    ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
    ("A", 1, "A"),
]


@pytest.mark.parametrize("s,num_rows,expected", test_data)
def test_all(s, num_rows, expected):
    assert expected == Solution().convert(s, num_rows)
