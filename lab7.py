def sort_matrix_by_row(matrix):
    # iterating over each row of matrix
    for i in range(len(matrix)):
        # iterating over each element in row
        for j in range(len(matrix[i])):
            # find the index of the minimum element in the remaining unsorted elements
            min_index = j
            for k in range(j+1, len(matrix[i])):
                if matrix[i][k] < matrix[i][min_index]:
                    min_index = k
            # swap the current element with the minimum element, if necessary
            if min_index != j:
                matrix[i][j], matrix[i][min_index] = matrix[i][min_index], matrix[i][j]
    # return the sorted matrix
    return matrix

def sort_rectangles(title):
    # Initialize the rectangles list with the given records
    rectangles = [ 
        {"ID": "Rect1", "Length": 40, "Breadth": 25, "Color": "red"}, {"ID": "Rect2", "Length": 30, "Breadth": 20, "Color": "blue"}, 
        {"ID": "Rect3", "Length": 70, "Breadth": 45, "Color": "green"}, {"ID": "Rect4", "Length": 20, "Breadth": 10, "Color": "purple"}
    ]
    # Getting length of list
    n = len(rectangles)
    # Iterate over the list from index 1 to n-1
    for i in range(1, n):
        # Initialize a variable j to the current index i
        j = i
        # Enter a while loop that checks whether j is greater than 0 and whether
        # the value of the current rectangle at the given title field is less than
        # the value of the previous rectangle at the same title field
        while j > 0 and rectangles[j][title] < rectangles[j-1][title]:
            # Swap the positions of the two rectangles using tuple unpacking
            rectangles[j], rectangles[j-1] = rectangles[j-1], rectangles[j]
            # Decrementing value of j by 1
            j -= 1
    # Return the sorted rectangles list
    return rectangles


matrix = [[5,8,1],[6,7,3],[5,4,9]]
sorted_matrix = sort_matrix_by_row(matrix)
print(sorted_matrix)

matrix1 = [['banana', 'apple', 'pear'],
          ['dog', 'cat', 'bird'],
          ['chocolate', 'vanilla', 'strawberry']]
sorted_matrix1 = sort_matrix_by_row(matrix1)
print(sorted_matrix1)

print(sort_rectangles("ID"))
print(sort_rectangles("Length"))
print(sort_rectangles("Breadth"))
print(sort_rectangles("Color"))



