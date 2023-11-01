def sort_matrix_by_row(matrix):
    # create a new empty matrix of the same size as the input matrix
    new_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    
    # loop through each row of the input matrix
    for i in range(3):
        # perform selection sort on the i-th row of the input matrix
        for j in range(3):
            min_index = j
            for k in range(j+1, 3):
                if matrix[i][k] < matrix[i][min_index]:
                    min_index = k
            # swap the minimum element with the current element
            matrix[i][j], matrix[i][min_index] = matrix[i][min_index], matrix[i][j]
        # copy the sorted i-th row of the input matrix to the i-th row of the new matrix
        new_matrix[i] = matrix[i]
    
    # return the sorted matrix
    return new_matrix

matrix = [[5,8,1], [6,7,3], [5,4,9]]
sorted_matrix = sort_matrix_by_row(matrix)
print(sorted_matrix) # output: [[1, 5, 8], [3, 6, 7], [4, 5, 9]]

