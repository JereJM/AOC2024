import re 
import time
start_time = time.time()

file_path = 'day03_input'

# Read the file content into a variable
with open(file_path, 'r') as file:
    puzzleinput = file.read()

valid_operations = re.findall("mul\([0-9]+,[0-9]+\)|do(?:n't)?\(\)",puzzleinput)

total = 0
part2total = 0
part2active = True
for operation in valid_operations:
	if operation == "do()": part2active = True; continue
	if operation == "don't()": part2active = False; continue
	a,b = operation[4:-1].split(",")
	product = int(a) * int(b)
	if part2active: part2total += product
	total += product
	#print(a, " * ", b, " = ", product)

print("Total product (part1): ", total)
print("Total product (part2): ", part2total)
print("--- %s seconds ---" % (time.time() - start_time))
