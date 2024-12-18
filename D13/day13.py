import time
from sympy import Matrix
from sympy.matrices.normalforms import smith_normal_form

start_time = time.time()

fileinput = 'day13_input'
with open(fileinput, 'r') as file:
	them_lines = [line.strip() for line in file]
A = []; B = []; P = []
#Such versatile and robust handling of input strings I could cry
for line in them_lines:
	if "Button A" in line: 
		temp = line.split(",")
		x = int(temp[0].split("+")[1])
		y = int(temp[1].split("+")[1])
		A.append([x,y])
	elif "Button B" in line: 
		temp = line.split(",")
		x = int(temp[0].split("+")[1])
		y = int(temp[1].split("+")[1])
		B.append([x,y])
	elif "Prize" in line:
		temp = line.split(",")
		x = int(temp[0].split("=")[1])
		y = int(temp[1].split("=")[1])
		P.append([x,y])

# P = xA + yB
# (P1,P2) = x(A1,A2) + y(B1,B2)
#->
# P1 = x*A1 + y*B1
# P2 = x*A2 + y*B2

j = 3
AA = A[j]
BB = B[j]
PP = P[j]

#Matrix form [[P1],[P2]] = M*[[x],[y]]
#Where M = [[A1,B1],[A2,B2]]
MM = [[AA[0],BB[0]],[AA[1],BB[1]]]
#So determinant of the coefficient matrix is D = A1*B2-A2*B1
#If determinant != 0, it can be inverted
#So (x,y) = M^-1 * P
print(MM)
#Then, we have the expected solution lattice L = {xA + yB | x,y ∈ Z}
#And go for smith normal for for the integer matrix M so that UMV = D and uh
#https://en.wikipedia.org/wiki/Smith_normal_form algorithm stolen from here

#Identity matrix function for size m
def createidentity(size):
	I = []
	for y in range(size):
		row = []
		for x in range(size):
			if x == y: row.append(1)
			else: row.append(0)
		I.append(row)
	return I

#Matrix multiplication:
def mmult(a,b):
	product = []
	for ay in range(len(a)):
		interprod = []
		#for ax in range(len(a[ay])):
		for bx in range(len(b[0])):
			intersum = 0
			for by in range(len(b)):
				intersum += a[ay][by] * b[by][bx]
			interprod.append(intersum)
		product.append(interprod)
	return product

#For an n x n matrix multiply row x by value
def rowscaling(A,B,row,value):
	#make identity matrix
	matrix_size = len(A)
	C = createidentity(matrix_size)
	C[row][row] = value
	print(C)
	print("A:",A)
	print("B:",B)
	A = mmult(A,C)
	B = mmult(B,C)
	return A,B

#For an n x n matrix add value times row1 to row2
def rowaddition(A,B,row,col,value):
	#make identity matrix
	matrix_size = len(A)
	C = createidentity(matrix_size)
	C[row][col] = value
	print(C)
	print("A:",A)
	print("B:",B)
	A = mmult(C,A)
	B = mmult(B,C)
	return A,B
	

# 1 0    0 1    1*0+0*1
# 0 1    1 0

U = [[1,0],[0,1]] #identity matrix
V = [[1,0],[0,1]] #identity matrix


print(rowscaling(MM,U,0,1/15))

#Whatever, the end result is (x',y')^T = V(x,y)^T and P' = UP when looked up
print(smith_normal_form(Matrix(MM)))
quit()

D = AA[0]*BB[1]-AA[1]*BB[0]
print(D)
xx = (PP[0]*BB[1]-PP[1]*BB[0])/D
yy = (PP[1]*AA[0]-PP[0]*AA[1])/D

quit()
for k in range(10):
	print(xx+k*BB[1], yy-k*BB[0])
	print([xx+k*BB[1]*aa for aa in AA])

quit()
i = 1
variations = P[i][0] // A[i][0]
for x in range(variations+1):
	temp = (P[i][0] - x * A[i][0]) 
	print( temp, "%", B[i][0], temp % B[i][0] )
quit()


print("Answer (part1): ",costs1)
print("Answer (part2): ",costs2)
print("--- %s seconds ---" % (time.time() - start_time))
