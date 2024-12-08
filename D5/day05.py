import re 
import time
start_time = time.time()

rules_file = 'day05_input_1'
fileinput = 'day05_input_2'

chars = []

def checkvalidity(line):
	for i,num in enumerate(line):
		#Check for numbers before on the left side of relevant rule
		for j,n in enumerate(line[i:]):
			if num in righthand_rules and n in righthand_rules[num]:
				return False, (i,j+i)
				
		#Check for numbers before on the right side of relevant rule
		for j,n in enumerate(line[:i]):
			if num in lefthand_rules and n in lefthand_rules[num]:
				return False, (i,j)
	return True, (0,0)

# Read the file content into a variable
with open(rules_file, 'r') as file:
	rules = [line.strip().split("|") for line in file]

# Read the file content into a variable
with open(fileinput, 'r') as file:
	lines = [line.strip().split(",") for line in file]


lefthand_rules = {}
righthand_rules = {}
for rule in rules:
	lefthand = rule[0]
	righthand = rule[1]
	if lefthand in lefthand_rules and lefthand:
		lefthand_rules[lefthand].append(righthand)
	elif lefthand:
		lefthand_rules[lefthand] = [righthand]

	if righthand in righthand_rules and righthand:
		righthand_rules[righthand].append(lefthand)
	elif righthand:
		righthand_rules[righthand] = [lefthand]

#part 1
correct_lines = []
incorrect_lines = []
for line in lines:
	valid,offenders = checkvalidity(line)
	if valid: correct_lines.append(line)
	else: 
		while not valid:
			valid,offenders = checkvalidity(line)
			a = line[offenders[0]]
			line[offenders[0]] = line[offenders[1]]
			line[offenders[1]] = a
		incorrect_lines.append(line)

total = 0
for line in correct_lines:
	total += int(line[len(line)//2])

total2 = 0
for line in incorrect_lines:
	total2 += int(line[len(line)//2])



print("Added total (part1): ", total)
print("Added total (part2): ", total2)
print("--- %s seconds ---" % (time.time() - start_time))
