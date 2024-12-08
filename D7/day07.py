import re 
import time
start_time = time.time()

fileinput = 'day07_input'
solutions = []
inputs = []
with open(fileinput, 'r') as file:
	lines = [line.strip() for line in file]
for line in lines:
	s, i = line.split(":")
	solutions.append(int(s))
	inputs.append([int(j) for j in i.strip().split(" ")])


def do_the_needful(operator, leftside, rightside):
	if operator == "*": return leftside * rightside
	if operator == "+": return leftside + rightside
	if operator == "||": return int(str(leftside) + str(rightside))

def valid_solution_exists(solution,nums,operators):
		operator_slots = len(nums)-1
		total_tries = len(operators)**operator_slots
		for j in range(total_tries):
			subtotal = nums[0]
			for k in range(operator_slots):
				chosen_operator = (j // len(operators)**k) % len(operators)
				subtotal = do_the_needful(operators[chosen_operator], subtotal, nums[k+1])
			if solution == subtotal: return True
		return False

##### MAIN #####
total_part1 = 0
operators = ["*","+"]
for i in range(len(solutions)):
	solution = solutions[i]
	nums = inputs[i]
	if valid_solution_exists(solution, nums, operators): 
		print("Valid solution found for", solution, nums,"!")
		total_part1 += solution

total_part2 = 0
operators = ["*","+","||"]
for i in range(len(solutions)):
	solution = solutions[i]
	nums = inputs[i]
	if valid_solution_exists(solution, nums, operators): 
		print("Valid solution found for", solution, nums,"!")
		total_part2 += solution



print("total of equations with valid solutions (part1): ", total_part1)
print("total of equations with valid solutions using extended set of operators (part2): ", total_part2)
print("--- %s seconds ---" % (time.time() - start_time))
