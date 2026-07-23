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

def matvec(A, v):
    result = []
    
    for row in A:
        total = 0
        
        for i in range(len(v)):
            total += row[i] * v[i]
            
        result.append(total)
        
    return result 

A = [
    [1, 2],
    [3, 4]
    
]

v = [5, 6]
print(matvec(A, v))