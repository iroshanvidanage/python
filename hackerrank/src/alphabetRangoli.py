def string_style(rownum, charac):
    if charac == 1:
        return chr(97 + rownum)
    return chr(97 + rownum) + '-' + string_style(rownum - 1, charac - 1) + '-' + chr(97 + rownum)


def print_rangoli(n):
    width = 4 * n - 3  # width = 4n-3 sequence (columns)
    for i in range(1, 2 * n):  # number of rows = 2n-1
        # n=character number
        # i=row number
        # ith row from 1 to n and reverse from n+1 to 2n-1
        print(string_style(n - 1, i if i <= n else 2 * n - i).center(width, '-'))


"""
def get_chars(i, n):
    if n == 1:
        return chr(97 + i)
    return chr(97 + i) + '-' + get_chars(i - 1, n - 1) + '-' + chr(97 + i)
"""


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
