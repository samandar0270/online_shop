# number = int(input("Sonni kiriting: "))


# def printFibonacciNumbers(n):
# 	f1 = 0
# 	f2 = 1
# 	if (n < 1):
# 		return
# 	print(f1, end=" ")
# 	for x in range(1, n):
# 		if n>f2:
# 			print(f2, end=" ")
# 			next = f1 + f2
# 			f1 = f2
# 			f2 = next
# 		else:
# 			break
# print(printFibonacciNumbers(number))
#  
sum = 0
matrix = [[1,2,3,4,5],
          [1,2,3,4,5],
          [1,2,3,4,5],
          [1,2,3,4,5],
          [1,2,3,4,5]]
for i in range(5):
    for j in range(5):
        if (i == j):
            print(matrix[i][j], end = '')
            sum += matrix[i][j]
        else:
            print(' ', end = '')
    print('')
print(sum)