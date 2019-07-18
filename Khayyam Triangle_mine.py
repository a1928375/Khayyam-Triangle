def triangle(n):
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        rowsbefore = triangle(n-1)
        i = 1
        currentrow = [1] * n
        while i < len(rowsbefore[-1]):
            currentrow[i] = rowsbefore[-1][i-1] + rowsbefore[-1][i]
            i = i + 1
        return rowsbefore + [currentrow]

print triangle(3)
