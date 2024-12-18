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

# P1 = n*A1 + m*B1
# P2 = n*A2 + m*B2

# n = (B1*P2 - B2*P1) / ( A2*B1 - A1*B2 )
# m = (A2*P1 - A1*P2) / ( A2*B1 - A1*B2 )

def do_it_all_but_with_offset(offset):
	tokens_needed = 0
	for machine in range(len(A)):
		A1 = A[machine][0]
		A2 = A[machine][1]
		B1 = B[machine][0]
		B2 = B[machine][1]
		P1 = P[machine][0]+offset
		P2 = P[machine][1]+offset
		lowest = 0
		a_presses = (B1*P2 - B2*P1) / ( A2*B1 - A1*B2 )
		b_presses = (A2*P1 - A1*P2) / ( A2*B1 - A1*B2 )
		if a_presses.is_integer(): 
			a_presses = int(a_presses)
			b_presses = int(b_presses)
			token_cost=a_presses*a_cost+b_presses*b_cost
			if token_cost < lowest or lowest == 0: lowest = token_cost
		if False:
			for buttonpresses in range(0,estimate*100):
				curr_x = BA[0] * buttonpresses
				curr_y = BA[1] * buttonpresses
				#print("Checking at",[curr_x,curr_y],"after",buttonpresses,"button presses.")
				needed_x = (Prize[0] - curr_x) // BB[0]
				needed_y = (Prize[1] - curr_y) // BB[1]
				if (
					(Prize[0] - curr_x) % BB[0] == 0 and 
					needed_x == needed_y and
					needed_x >= 0
					):
					print("["+str(machine)+"] Goal reachable by",buttonpresses,"presses of Button A, and",needed_x,"presses of Button B.")
					token_cost=buttonpresses*a_cost+needed_x*b_cost
					print("score:",token_cost)
					if token_cost < lowest or lowest == 0: lowest = token_cost
		tokens_needed += lowest
		#time.sleep(5)
	return tokens_needed

a_cost = 3
b_cost = 1
part1 = do_it_all_but_with_offset(0)
part2 = do_it_all_but_with_offset(10000000000000)



print("Minimum amount of tokens needed to win every winnable game (part1): ",part1)
print("Minimum amount of tokens needed to win every winnable game (part2): ",part2)
print("--- %s seconds ---" % (time.time() - start_time))
