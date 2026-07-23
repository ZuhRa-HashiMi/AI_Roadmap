def transpose(A):
    rows = len(A)
    cols = len(A[0])
    
    result = []
    for col in range(cols):
        new_row = []
        
        for row in range(rows):
            new_row.append(A[row][col])
            
        result.append(new_row)
        
    return result 

A = [
    [1, 2, 3],
    [4, 5, 6]
]

print(transpose(A))