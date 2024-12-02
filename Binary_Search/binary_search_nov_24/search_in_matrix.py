


def search_matrix(matrix, key):
    n = len(matrix)
    m = len(matrix[0])
    
    i, j = 0, m-1
    
    while i>=0 and j>=0 and i < n and j < m:
        if matrix[i][j] == key:
            return (i, j)
        elif matrix[i][j] > key:
            j-=1
        else:
            i+=1
    return -1