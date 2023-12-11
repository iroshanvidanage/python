import numpy


def edit_distance(str_1, str_2):
    # Computes the edit distances of the two strings

    ln_str_1 = len(str_1)
    ln_str_2 = len(str_2)

    # Initialize the matrix
    matrix = numpy.zeros((ln_str_1 + 1, ln_str_2 + 1))
    for _ in range(ln_str_2 + 1):
        matrix[0][_] = _

    for _ in range(ln_str_1 + 1):
        matrix[_][0] = _

    # Filling the matrix
    for i in range(1, ln_str_1 + 1):
        for j in range(1, ln_str_2 + 1):
            insertion = matrix[i][j - 1] + 1
            deletion = matrix[i - 1][j] + 1
            mismatch = matrix[i - 1][j - 1] + 1
            match = matrix[i - 1][j - 1]

            if str_1[i - 1] == str_2[j - 1]:
                matrix[i][j] = min(insertion, deletion, match)

            if str_1[i - 1] != str_2[j - 1]:
                matrix[i][j] = min(insertion, deletion, mismatch)

    return int(matrix[ln_str_1][ln_str_2]), matrix


def optimal_alignment(matrix, str_1, str_2, top, bottom, i, j):
    # Finds the optimal alignment of the two strings given the edit matrix

    if i == 0 and j == 0:
        return ' '.join(top[::-1]), ' '.join(bottom[::-1])

    if i > 0 and matrix[i][j] == matrix[i - 1][j] + 1:
        top.append(f'|{str_1[i - 1]}|')
        bottom.append('|-|')
        return optimal_alignment(matrix, str_1, str_2, top, bottom, i - 1, j)

    elif j > 0 and matrix[i][j] == matrix[i][j - 1] + 1:
        top.append('|-|')
        bottom.append(f'|{str_1[i - 1]}|')
        return optimal_alignment(matrix, str_1, str_2, top, bottom, i, j - 1)

    else:
        top.append(f'|{str_1[i - 1]}|')
        bottom.append(f'|{str_1[i - 1]}|')
        return optimal_alignment(matrix, str_1, str_2, top, bottom, i - 1, j - 1)


str1, str2 = input(), input()
distance_to_edit, matrix_to_edit = edit_distance(str_1=str1, str_2=str2)

# top_final, bottom_final = optimal_alignment(matrix=matrix_to_edit, str_1=str1, str_2=str2, top=[], bottom=[], i=len(str1), j=len(str2))

# print(f'Editing distance : {distance_to_edit}')
# print(f'Optimal alignment :\n{top_final}\n{bottom_final}')
print(f'{distance_to_edit}')
