def print_formatted1(number):
    # x = bin(number)
    x = f'{number:b}'  # string formatting to convert bases
    w = len(x)  # length of the binary

    [print(f'{_:{w}d} {_:{w}o} {_:{w}x} {_:{w}b}') for _ in range(1, number + 1)]

    # print(x, w)


def print_formatted2(number):
    x = f'{number:b}'  # string formatting to convert bases
    width = len(x)  # length of the binary

    for number in range(5, 12):
        for base in 'dXob':
            print('{0:{width}{base}}'.format(number, base=base, width=width), end=' ')


def print_formatted2(number, base='dXob'):
    x = f'{number:b}'  # string formatting to convert bases
    width = len(x)  # length of the binary

    for i in range(1, number+1):
        for bse in str(base):
            print('{0:{width}{base}}'.format(i, base=bse, width=width), end=' ')  # here the number is formatted
            # for 0
        print()


if __name__ == '__main__':
    # n = int(input())
    print_formatted2(number=10)

    """
    d - decimal
    o - octal
    X - hex
    b - binary
    """
