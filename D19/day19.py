import time

start_time = time.time()

towelfile = 'day19_input'
designfile = 'day19_input_2'
towels = []
designs = []
with open(towelfile, 'r') as file:
	#Towels of type: [concatenated string, amount of such string, [string]]
	#where the aim is to in future add new towels to the concatenated string
	#keep track of how many of the same concatenated string already exist
	#and also list at least one possible list of all individual towels in the concatenated string
	towels = [[t.strip(),1,[t.strip()]] for i,t in enumerate(file.read().split(","))]
with open(designfile, 'r') as file:
	designs = [line.strip() for line in file]

def findnext(design,towels):
	matches = []
	for towel in towels:
		if design.startswith(towel[0]): matches.append(towel)
	return matches

def hell(design,partial,towels):
	added_partial = []
	for pattern in partial:
		begin_at = len(pattern[0])
		results = findnext(design[begin_at:],towels)
		for result in results:
			#Long story short for the following 2 lines:
			#We check if the pattern after adding "result" appears already in the added_partial list
			#And if so, append the pattern's occurence amount to the added_partial's
			#Theory being that if we have the same pattern twice, we only need to know how many different ways we
			#may have ended up there, and then just assume that all future splits from that string
			#exist that many times in the full list of all possible variations
			temp = [ p[0] for p in added_partial]
			if pattern[0] + result[0] in temp: i=temp.index(pattern[0] + result[0]); added_partial[i][1] += pattern[1]; continue

			added_partial.append([pattern[0] + result[0],pattern[1],pattern[2] + result[2]])
	return added_partial


completeable = 0
variations = 0
for design in designs:
	partial = findnext(design,towels)
	completed = False
	while partial:
		new_partial = hell(design,partial,towels)
		#Go from end to start for in-place popping action
		k = len(new_partial)
		for i,p in enumerate(new_partial[::-1]):
			idx = k-i-1
			if p[0] == design:
				variations += p[1]
				completed = True
				new_partial.pop(idx)
		partial = new_partial
	if completed: completeable += 1



print("Amount of possible/completeable designs (part1):",completeable)
print("Total amount of completeable variations of all designs (part2):",variations)
print("--- %s seconds ---" % (time.time() - start_time))
