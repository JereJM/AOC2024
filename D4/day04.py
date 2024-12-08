import re 
import time
start_time = time.time()

file_path = 'day04_input'

chars = []
# Read the file content into a variable
with open(file_path, 'r') as file:
	for line in file:
		chars.append([character for character in line.strip()])

#Part 1
candidates = []
for y,line in enumerate(chars):
	for x,symbol in enumerate(line):
		if symbol == "X":
			if x < len(line)-3: 						candidates.append(chars[y][x]+chars[y][x+1]+chars[y][x+2]+chars[y][x+3]) 		#
			if x > 2: 									candidates.append(chars[y][x]+chars[y][x-1]+chars[y][x-2]+chars[y][x-3])		#BACKWARDS
			if y < len(chars)-3: 						candidates.append(chars[y][x]+chars[y+1][x]+chars[y+2][x]+chars[y+3][x])		#DOWN
			if y > 2: 									candidates.append(chars[y][x]+chars[y-1][x]+chars[y-2][x]+chars[y-3][x])		#UP
			if x < len(line)-3 and y < len(chars)-3: 	candidates.append(chars[y][x]+chars[y+1][x+1]+chars[y+2][x+2]+chars[y+3][x+3])	#DIAGONAL DOWN
			if x > 2 and y > 2: 						candidates.append(chars[y][x]+chars[y-1][x-1]+chars[y-2][x-2]+chars[y-3][x-3])	#DIAGONAL BACKWARDS UP
			if x < len(line)-3 and y > 2: 				candidates.append(chars[y][x]+chars[y-1][x+1]+chars[y-2][x+2]+chars[y-3][x+3])	#DIAGONAL UP
			if x > 2 and y < len(chars)-3: 				candidates.append(chars[y][x]+chars[y+1][x-1]+chars[y+2][x-2]+chars[y+3][x-3])	#DIAGONAL BACKWARDS DOWN

total=0
for candidate in candidates:
	if candidate == "XMAS":
		total += 1

#Part 2
total2=0
for y,line in enumerate(chars):
	for x,symbol in enumerate(line):
		if symbol == "A":
			if x > 0 and y > 0 and x < len(line)-1 and y < len(line)-1:
				cube = [ch[x-1:x+2] for ch in [line for line in chars[y-1:y+2]] ] #Extracts 3x3 matrix centered at the found letter
				#Rotate that shit all around
				for _ in range(4):
					cube = list(list(x) for x in zip(*cube))[::-1]
					if cube[0][0]+cube[1][1]+cube[2][2] == "MAS" and cube[2][0]+cube[1][1]+cube[0][2] == "MAS": #dummm check
						total2 += 1

print("Total amount of XMAS (part1): ", total)
print("Total amount of X-MAS (part2): ", total2)
print("--- %s seconds ---" % (time.time() - start_time))
