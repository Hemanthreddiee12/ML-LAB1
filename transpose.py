def transpose_matrix(matrix):
    transposed_matrix = [list(row) for row in zip(*matrix)]
    return transposed_matrix

def get_matrix_input():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    matrix = []

    for i in range(rows):
        row = [float(input(f"Enter element {i + 1},{j + 1}: ")) for j in range(cols)]
        matrix.append(row)

    return matrix

def display_matrix(matrix):
    for row in matrix:
        print(row)

def main():
    input_matrix = get_matrix_input()
    transposed_matrix = transpose_matrix(input_matrix)

    print("\nOriginal Matrix:")
    display_matrix(input_matrix)
    
    print("\nTransposed Matrix:")
    display_matrix(transposed_matrix)

if __name__ == "__main__":
    main()
