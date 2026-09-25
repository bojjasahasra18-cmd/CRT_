def diagonalSort(mat):
    rows = len(mat)
    cols = len(mat[0])

    for start in range(cols):
        values = []
        i = 0
        j = start

        while i < rows and j < cols:
            values.append(mat[i][j])
            i += 1
            j += 1

        values.sort()

        i = 0
        j = start
        k = 0

        while i < rows and j < cols:
            mat[i][j] = values[k]
            i += 1
            j += 1
            k += 1

    for start in range(1, rows):
        values = []
        i = start
        j = 0

        while i < rows and j < cols:
            values.append(mat[i][j])
            i += 1
            j += 1

        values.sort()

        i = start
        j = 0
        k = 0

        while i < rows and j < cols:
            mat[i][j] = values[k]
            i += 1
            j += 1
            k += 1

    return mat


if __name__ == '__main__':
    m, n = map(int, input().split())
    mat = []

    for i in range(m):
        mat.append(list(map(int, input().split())))

    result = diagonalSort(mat)

    for row in result:
        print(*row)