def add_matrices():
    row_A, col_A = input('Enter size of the first matrix: ').split()
    print('Enter the first matrix:')
    A = [input().split() for _ in range(int(row_A))]
    row_B, col_B = input('Enter size of the second matrix: ').split()
    print('Enter the second matrix:')
    B = [input().split() for _ in range(int(row_B))]

    if row_A != row_B or col_A != col_B:
        print('The operation cannot be performed.')
    else:
        A = [[float(num) for num in row] for row in A]
        B = [[float(num) for num in row] for row in B]
        result = []
        for row in range(int(row_A)):
            result.append([])
            for col in range(int(col_A)):
                result[row].append(A[row][col] + B[row][col])
        print('The result is:')
        [print(*row) for row in result]


def multiply_constant():
    row_A, col_A = input('Enter size of the matrix: ').split()
    print('Enter the matrix:')
    A = [input().split() for _ in range(int(row_A))]
    const = float(input('Enter the constant: '))
    result = []
    for i, row in enumerate(A):
        result.append([])
        for col in row:
            result[i].append(float(col) * const)
    print('The result is:')
    [print(*row) for row in result]


def multiply_matrices():
    row_A, col_A = input('Enter size of the first matrix: ').split()
    print('Enter the first matrix:')
    A = [input().split() for _ in range(int(row_A))]
    row_B, col_B = input('Enter size of the second matrix: ').split()
    print('Enter the second matrix:')
    B = [input().split() for _ in range(int(row_B))]
    if col_A != row_B:
        print('The operation cannot be performed.')
    else:
        A = [[float(num) for num in row] for row in A]
        B = [[float(num) for num in row] for row in B]
        result = []
        for i in range(int(row_A)):
            result.append([])
            for j in range(int(col_B)):
                result[i].append(dot_product(A, B, i, j))
        print('The result is:')
        [print(*row) for row in result]

def dot_product(A, B, m, n):
    vector_A = A[m]
    vector_B = [sub[n] for sub in B]
    total = 0
    for i in range(len(A[m])):
        total += vector_A[i] * vector_B[i]
    return total


def transpose():
    while True:
        print('1. Main diagonal\n'
              '2. Side diagonal\n'
              '3. Vertical line\n'
              '4. Horizantal line')
        entry = input('Select a method: ')
        if entry in ('1', '2', '3', '4'):
            break
        print('Invalid entry. Try again!')
    row, col = [int(num) for num in input('Enter the matrix size: ').split()]
    print('Enter the matrix:')
    matrix = [[float(num) for num in input().split()] for _ in range(row)]
    result = [[None for _ in range(col)] for __ in range(row)]
    for i in range(row):
        for j in range(col):
            if entry == '1':
                result[i][j] = matrix[j][i]
            if entry == '2':
                result[i][j] = matrix[col - 1 - j][row - 1 - i]
            if entry == '3':
                result[i][j] = matrix[i][col - 1 - j]
            if entry == '4':
                result[i][j] = matrix[row - 1 - i][j]
    print('The result is:')
    [print(*row) for row in result]


def determinant():
    row, col = [int(num) for num in input('Enter the matrix size: ').split()]
    if row != col:
        print('The operation cannot be performed.')
        return
    print('Enter the matrix:')
    matrix = [[float(num) for num in input().split()] for _ in range(row)]
    print('The result is:')
    print(calculate_det(matrix, row))


def calculate_det(matrix, size):
    if size == 1:
        return matrix[0][0]
    elif size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    elif size == 3:
        return matrix[0][0] * matrix[1][1] * matrix[2][2] \
               + matrix[0][1] * matrix[1][2] * matrix[2][0] \
               + matrix[1][0] * matrix[2][1] * matrix[0][2] \
               - matrix[0][2] * matrix[1][1] * matrix[2][0] \
               - matrix[0][1] * matrix[1][0] * matrix[2][2] \
               - matrix[1][2] * matrix[2][1] * matrix[0][0]
    else:
        total = 0
        for i in range(size):
            total += matrix[0][i] * ((-1) ** i) * calculate_det([[row[j] for j in range(size) if j != i] for row in matrix[1:]], size - 1)
        return total


def inverse():
    row, col = [int(num) for num in input('Enter the matrix size: ').split()]
    if row != col:
        print('The operation cannot be performed.')
        return
    print('Enter the matrix:')
    matrix = [[float(num) for num in input().split()] for _ in range(row)]
    det = calculate_det(matrix, row)
    if det == 0:
        print('This matrix does not have an inverse.')
    else:
        print('The result is:')
        adj = adjoint(matrix, row)
        result = adj[:]
        for i in range(len(adj)):
            for j in range(len(adj)):
                result[i][j] = adj[i][j] / det
        [print(*row) for row in result]


def adjoint(matrix, size):
    process = [row[:] for row in matrix]
    result = [row[:] for row in matrix]
    for i in range(size):
        for j in range(size):
            result[j][i] = ((-1) ** (i + j)) * calculate_det([[row[k] for k in range(size) if k != j] for row in (process[:i] + process[i + 1:])], size - 1)
    return result


def main():
    while True:
        print('\n'
              '1. Add matrices\n'
              '2. Multiply matrix by a constant\n'
              '3. Multiply matrices\n'
              '4. Transpose matrix\n'
              '5. Calculate determinant\n'
              '6. Inverse matrix\n'
              '0. Exit\n')
        entry = input()
        if entry == '1':
            add_matrices()
        elif entry == '2':
            multiply_constant()
        elif entry == '3':
            multiply_matrices()
        elif entry == '4':
            transpose()
        elif entry == '5':
            determinant()
        elif entry == '6':
            inverse()
        elif entry == '0':
            break
        else:
            print('Invalid entry.')


main()
