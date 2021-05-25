from str_into_floatArr import str_into_floatArr

def read_matrix_from_file(file):
    """ Function reads 2D matrix form file and returns it.
        It reads the size of matrix from the first line of the file.
        It expects that the size is writen like 'size_n*size_m'.
        Then the function reads size_n lines and from each line
        extracts size_m float numbers - elements of Matrix.
    """
    Matrix = []

    #The block below gets size of matrix
    size = file.readline()
    size = size.split('*')
    size_n = int(size[0])
    size_m = int(size[1])

    #The block below gets elements of Matrix size_n * size_m
    for i in range(size_n):
        line = file.readline()
        floatArr = str_into_floatArr(line, size_m)
        for j in range(size_m):
            Matrix.append(floatArr[j])

    return Matrix
