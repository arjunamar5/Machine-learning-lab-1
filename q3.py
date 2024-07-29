def matrix_multiply(A, B):
    
    size = len(A)
    # Create a result matrix filled with zeros
    result = [[0] * size for _ in range(size)]

    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += A[i][k] * B[k][j]

    return result

def matrix_power(A, m):
    
    if not A or len(A) != len(A[0]):
        raise ValueError("A must be a square matrix")
    if not isinstance(m, int):
        raise ValueError("m must be an integer")

    size = len(A)
    # Initialize the result as the identity matrix
    result = [[1 if i == j else 0 for j in range(size)] for i in range(size)]

    for _ in range(m):
        result = matrix_multiply(result, A)

    return result

def get_matrix_from_user(size):
    
    matrix = []
    print(f"Enter the elements of the {size}x{size} matrix row by row (space-separated):")
    for i in range(size):
        row = list(map(float, input(f"Row {i + 1}: ").strip().split()))
        if len(row) != size:
            raise ValueError(f"Row {i + 1} must contain exactly {size} elements.")
        matrix.append(row)
    return matrix

def main():
    # Get matrix size from the user
    size = int(input("Enter the size of the square matrix (n for an n x n matrix): "))
    
    # Get the matrix from user input
    A = get_matrix_from_user(size)

    # Get the power from user input
    m = int(input("Enter the exponent m (a non-negative integer): "))
    if m < 0:
        raise ValueError("m must be a non-negative integer")

    # Calculate A^m
    result = matrix_power(A, m)

    # Display the result
    print(f"A^{m}:")
    for row in result:
        print(row)

if __name__ == "__main__":
    main()
