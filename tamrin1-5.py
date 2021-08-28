len_triangle = int(input('enter len= '))

khayyam_triangle  = [[1 for i in range(len_triangle)] for j in range(len_triangle)]

for i in range(len_triangle):
    for j in range(1, i):
        khayyam_triangle[i][j] = khayyam_triangle[i-1][j-1] + khayyam_triangle[i-1][j]

for i in range(len_triangle):
    for j in range(i+1):
        print(khayyam_triangle[i][j], end=' ')
    print()