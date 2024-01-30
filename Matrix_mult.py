def is_matrix_multiplicable(matrix_a, matrix_b):
    return len(matrix_a[0]) == len(matrix_b)

def matrix_multiply(matrix_a, matrix_b):
    if not is_matrix_multiplicable(matrix_a, matrix_b):
        return None

    result_matrix = [[0] * len(matrix_b[0]) for _ in range(len(matrix_a))]

    for i in range(len(matrix_a)):
        for j in range(len(matrix_b[0])):
            for k in range(len(matrix_b)):
                result_matrix[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return result_matrix

def get_matrix_input(rows, cols):
    matrix = []

    for i in range(rows):
        row = [float(input(f"Enter element {i + 1},{j + 1}: ")) for j in range(cols)]
        matrix.append(row)

    return matrix

def display_matrix(matrix):
    for row in matrix:
        print(row)

def main():
    rows_a = int(input("Enter the number of rows for matrix A: "))
    cols_a = int(input("Enter the number of columns for matrix A: "))
    matrix_a = get_matrix_input(rows_a, cols_a)

    rows_b = int(input("Enter the number of rows for matrix B: "))
    cols_b = int(input("Enter the number of columns for matrix B: "))
    matrix_b = get_matrix_input(rows_b, cols_b)

    result_matrix = matrix_multiply(matrix_a, matrix_b)

    if result_matrix is not None:
        print("Resultant Matrix:")
        display_matrix(result_matrix)
    else:
        print("Error: Matrices are not multipliable.")

if __name__ == "__main__":
    main()
