from read_matrix_from_file import read_matrix_from_file

with open("data.txt", 'r') as file:
    Matrix = read_matrix_from_file(file)

print(Matrix)
print('\n')
