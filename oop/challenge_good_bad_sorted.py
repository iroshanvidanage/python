
def good_bad_sorted(sequence):
    '''
        Args:
            sequence    | An iterable consisting of str objects.
                        |> Convert all strings possible into int objects.
                        |> Any string that cannot be converted into an int will remain a string.
                        |> Example: ['N/A', '21', '42', 'MISSING']
        Returns:
            A (2)tuple of lists consisting of good and bad data. (good: list, bad: list)

        Implement this function such that it returns a tuple containing good and bad data.

        Good Data:
            All strings representing numbers must be converted into int objects.
            All even numbers returned in descending order.
            All odd numbers are removed.

            Examples:

            >>> sequence = '100 85 37 50 N/A 66'.split()
            >>> good_bad_sorted(squence)[0]
            [100, 66 50]

            >>> sequence = '1 2 1 4 N/A 1'.split()
            >>> good_bad_sorted(squence)[0]
            [4, 2]

        Bad Data:
            Any string which doesn't convert into an int is considered bad data.
            Bad data must be sorted alphabetically in ascending order.

            Examples:

            >>> sequence = '1 2 1 4 N/A MISSING 1'.split()
            >>> good_bad_sorted(squence)[1]
            ['MISSING', 'N/A']
        
        Results:
            Once complete, this function returns a tuple containing two lists objects.
            The first list contains good data.
            The second list contains bad data.

            >>> sequence = '2 3 4 5 MISSING 42'.split()
            >>> good_bad_sorted(squence)
            ([42, 4, 2], ['MISSING'])
    '''
    good = []
    bad = []

    for _ in sequence:
        if _.isnumeric():
            if int(_) % 2 == 0:
                good.append(int(_))
        else:
            bad.append(_)
    
    good.sort(reverse=True)
    bad.sort()

    return (good, bad)


if __name__ == '__main__':
    print(good_bad_sorted('2 3 4 5 8 MISSING N/A 42'.split()))