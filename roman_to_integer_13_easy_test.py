def roman_to_integer(s: str) -> int:
    m = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    subbable = {
        1: [5, 10],  # 1 can go before 5 and 10 to make 4 and 9
        5: [],
        10: [50, 100],  # 10 can go before 50 and 100 to make 40 and 90
        50: [],
        100: [500, 1000],  # 100 can go before 500 and 1000 to make 400 and 900
        500: [],
        1000: [],
    }
    count = 0
    i = 0
    while True:
        if i >= len(s):
            break
        v = m[s[i]]
        i += 1
        # if we are on last char then count individually and exit
        if i >= len(s):
            count += v
            break
        # check if current is subbable from next
        v_next = m[s[i]]
        if v_next in subbable[v]:
            v = v_next - v
            i += 1
        count += v

    return count


def test_simple():
    assert roman_to_integer("III") == 3


def test_more_symbols():
    assert roman_to_integer("LVIII") == 58


def test_sub_numbers():
    assert roman_to_integer("MCMXCIV") == 1994
