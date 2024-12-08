file_path = 'day02_input'

# Read the file content into a variable
with open(file_path, 'r') as file:
    lines = [line.strip() for line in file]


def is_safe(numbers):
	direction = ""
	previous=numbers[0]
	for l in numbers[1:]:
		if previous > l and previous-l <= 3 and direction != "up":
			direction = "down"
		elif previous < l and l-previous <= 3 and direction != "down":
			direction = "up"
		else:
			return False
		previous = l
	return True

safe=0
for line in lines:
	numbers=[int(a) for a in line.split(" ")]
	errors = 0
	isdone = is_safe(numbers)
	if isdone:
		safe += 1
	else:
		for i in range(len(numbers)):
			isdone = is_safe(numbers[:i] + numbers[i+1:])
			if isdone:
				safe += 1
				break


print("Number of safe lines: ", safe)
#print("Similarity: ", similarity)
