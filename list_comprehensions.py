# even_number = [i for i in range(0,10) if i % 2 == 0 ]
# odd_number = [i for i in range(0,10) if i % 2 != 0 ]
# print(even_number)
# print(odd_number)

# matrixx = [[x,y] for x in range(3,6) for y in range(7,10)]
# print(matrixx)

x = int(input())
y = int(input())
z = int(input())
n = int(input())

list_comp = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n]
print(list_comp)