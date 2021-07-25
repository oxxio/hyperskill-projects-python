
def fill_matrix(matrix, input_var, option=0):

    for row in range(input_var[0]):
        if option == 1:
            row_input = [int(x) for x in input().split(" ")]
        else:
            row_input = [float(x) for x in input().split(" ")]
        matrix.append(row_input)

    return

def add_matrix(matrix_a, matrix_b, matrix_out, input_var):

    for row_n in range(int(input_var[0])):
        new_row = []
        for column_n in range(int(input_var[1])):
            new_row.append(matrix_a[row_n][column_n] + matrix_b[row_n][column_n])
        matrix_out.append(new_row)

    return

def print_matrix(matrix):

    print("The result is:")
    for col in matrix:
        print(*col)

    return

def multi_matrix_constant(matrix_a, const, matrix_out, input_var):

    for row_n in range(int(input_var[0])):
        new_row = []
        for column_n in range(int(input_var[1])):
            new_row.append(matrix_a[row_n][column_n] * const)
        matrix_out.append(new_row)

    return

def multi_matrix(matrix_a, matrix_b):

    rows = len(matrix_a)       # number of rows in first matrix
    cols = len(matrix_b[0])    # number of columns in second matrix

    # matrix m by n filled by 0
    matrix_out = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            for k in range(len(matrix_b)):
                matrix_out[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return matrix_out

def main_diagonal(matrix):

    rows = len(matrix)       # number of rows in matrix
    cols = len(matrix[0])    # number of columns in matrix

    # matrix m by n filled by 0
    matrix_out = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            matrix_out[i][j] = matrix[j][i]

    return matrix_out

def side_diagonal(matrix):

    rows = len(matrix)       # number of rows in matrix
    cols = len(matrix[0])    # number of columns in matrix

    # matrix m by n filled by 0
    matrix_out = [[0 for _ in range(cols)] for _ in range(rows)]

    matrix_out = main_diagonal(matrix)

    for i in reversed(range(rows)):
        matrix[rows-i-1] = matrix_out[i][::-1]

    return matrix

def vertical_line(matrix):

    rows = len(matrix)       # number of rows in matrix
    cols = len(matrix[0])    # number of columns in matrix

    for i in range(rows):
        matrix[i] = matrix[i][::-1]

    return matrix

def horizontal_line(matrix):

    rows = len(matrix)       # number of rows in matrix
    cols = len(matrix[0])    # number of columns in matrix

    # matrix m by n filled by 0
    matrix_out = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        matrix_out[rows-i-1] = matrix[i][::]

    return matrix_out

def get_matrix_minor(matrix, i, j):

    return [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]

def calculate_determinant(matrix):

    rows = len(matrix)       # number of rows in matrix

    matrix_det = 0

    if rows == 1:
        return matrix[0][0]

    if rows == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

    for c in range(rows):
        matrix_det += ((-1) ** c) * matrix[0][c] * calculate_determinant(get_matrix_minor(matrix, 0, c))

    return matrix_det

def zeros_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        matrix.append([])
        for j in range(cols):
            if j == i:
                matrix[-1].append(1.0)
            else:
                matrix[-1].append(0.0)
    return matrix

def inverse_matrix(AM):

    n = len(AM)

    IM = zeros_matrix(n, n)

    fd = 0  # fd stands for focus diagonal OR the current diagonal
    fdScaler = 1. / AM[fd][fd]

    for j in range(n):  # using j to indicate cycling thru columns
        AM[fd][j] = fdScaler * AM[fd][j]
        IM[fd][j] = fdScaler * IM[fd][j]

    indices = list(range(n))

    for i in indices[0:fd] + indices[fd + 1:]:  # *** skip row with fd in it.
        crScaler = AM[i][fd]  # cr stands for "current row".
        for j in range(n):  # cr - crScaler * fdRow, but one element at a time.
            AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
            IM[i][j] = IM[i][j] - crScaler * IM[fd][j]

    indices = list(range(n))  # to allow flexible row referencing ***
    # We've already run for fd = 0, now let's run for fd = 1 to the last fd
    for fd in range(1, n):  # fd stands for focus diagonal
        fdScaler = 1.0 / AM[fd][fd]
        # FIRST: scale fd row with fd inverse.
        for j in range(n):  # Use j to indicate column looping.
            AM[fd][j] *= fdScaler
            IM[fd][j] *= fdScaler

        # SECOND: operate on all rows except fd row.
        for i in indices[:fd] + indices[fd + 1:]:  # *** skip row with fd in it.
            crScaler = AM[i][fd]  # cr stands for "current row".
            for j in range(n):  # cr - crScaler * fdRow, but one element at a time.
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
                IM[i][j] = IM[i][j] - crScaler * IM[fd][j]

    print("The result is:")
    print_matrix(IM)

    return IM

if __name__ == '__main__':

    choice = ""
    while True:

        fir_mtx    = []
        sec_mtx    = []
        output_mtx = []

        print("1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
        print("4. Transpose matrix")
        print("5. Calculate a determinant")
        print("6. Inverse matrix")
        print("0. Exit")
        choice = int(input("Your choice:"))

        if choice == 0:
            break

        elif choice == 1:
            fir_mtx_input = [int(x) for x in input("Enter size of first matrix:").split(" ")]
            print("Enter first matrix:")
            fill_matrix(fir_mtx, fir_mtx_input)

            sec_mtx_input = [int(x) for x in input("Enter size of second matrix:").split(" ")]
            print("Enter second matrix:")
            fill_matrix(sec_mtx, sec_mtx_input)

            if fir_mtx_input[0] == sec_mtx_input[0] and\
                    fir_mtx_input[1] == sec_mtx_input[1]:

                add_matrix(fir_mtx, sec_mtx, output_mtx, fir_mtx_input)
                print_matrix(output_mtx)
            else:
                print("ERROR")

        elif choice == 2:
            fir_mtx_input = [int(x) for x in input().split()]
            fill_matrix(fir_mtx, fir_mtx_input)

            constant = int(input())
            multi_matrix_constant(fir_mtx, constant, output_mtx, fir_mtx_input)
            print_matrix(output_mtx)

        elif choice == 3:
            fir_mtx_input = [int(x) for x in input("Enter size of first matrix:").split(" ")]
            print("Enter first matrix:")
            fill_matrix(fir_mtx, fir_mtx_input)

            sec_mtx_input = [int(x) for x in input("Enter size of second matrix:").split(" ")]
            print("Enter second matrix:")
            fill_matrix(sec_mtx, sec_mtx_input)

            if fir_mtx_input[1] != sec_mtx_input[0]:
                print("The operation cannot be performed.\n")
            else:
                output_mtx = multi_matrix(fir_mtx, sec_mtx)
                print_matrix(output_mtx)

        elif choice == 4:
            print("1. Main diagonal")
            print("2. Side diagonal")
            print("3. Vertical line")
            print("4. Horizontal line")

            choice = int(input("Your choice:"))

            fir_mtx_input = [int(x) for x in input("Enter matrix size:").split(" ")]
            print("Enter matrix:")
            fill_matrix(fir_mtx, fir_mtx_input)

            if choice == 1:
                output_mtx = main_diagonal(fir_mtx)
            elif choice == 2:
                output_mtx = side_diagonal(fir_mtx)
            elif choice == 3:
                output_mtx = vertical_line(fir_mtx)
            elif choice == 4:
                output_mtx = horizontal_line(fir_mtx)

            print_matrix(output_mtx)

        elif choice == 5:

            fir_mtx_input = [int(x) for x in input("Enter size of first matrix:").split(" ")]
            print("Enter first matrix:")
            fill_matrix(fir_mtx, fir_mtx_input)

            matrix_det = calculate_determinant(fir_mtx)
            print("The result is:")
            print(matrix_det)

        elif choice == 6:

            fir_mtx_input = [int(x) for x in input("Enter size of first matrix:").split(" ")]
            print("Enter matrix:")
            fill_matrix(fir_mtx, fir_mtx_input)

            inverse_matrix(fir_mtx)
