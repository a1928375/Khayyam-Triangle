def u_triangle(n):
    result = []
    current = [1]
    for unused in range(0, n):
        result.append(current)
        current = make_next_row(current)
    return result

def make_next_row(row):
    result = []
    prev = 0
    for e in row:
        result.append(e + prev)
        prev = e
    result.append(prev)
    return result
    
print u_triangle(3)
