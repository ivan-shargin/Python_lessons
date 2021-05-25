
Matrix = []

with open("data.txt", 'r') as f:
    
    size = f.readline()
    arr_size = size.split('*')
    size_n = int(arr_size[0])
    size_m = int(arr_size[1])

    for i in range(size_n):
        line = f.readline()
        line = line.split(' ')
        for j in range(size_m):
            Matrix.append(float(line[j]))

    


print(Matrix)
