import time
start_time = time.time()

fileinput = 'day10_input'
symbols = []
with open(fileinput, 'r') as file:
	top_map = [[int(height) for height in line.strip() ] for line in file]

zeros = [] # [[y1,x1],[y2,x2]...]
for i,line in enumerate(top_map):
	for j,elevation in enumerate(line):
		if elevation == 0: zeros.append([i,j])


def find_paths(location):
	y = location[0]
	x = location[1]
	paths = []
	if x < len(top_map[0])-1 and top_map[y][x+1] == top_map[y][x]+1: paths.append([y,x+1])
	if x > 0 and top_map[y][x-1] == top_map[y][x]+1: paths.append([y,x-1])
	if y < len(top_map)-1 and top_map[y+1][x] == top_map[y][x]+1: paths.append([y+1,x])
	if y > 0 and top_map[y-1][x] == top_map[y][x]+1: paths.append([y-1,x])
	return paths

scores1 = []
scores2 = []
for zero in zeros:
	y = zero[0]
	x = zero[1]
	#time.sleep(1)
	print("Starting a new trailhead:")
	print(zero, " - ", top_map[y][x])

	scores1.append(0)
	paths = find_paths(zero)
	while len(paths) > 0:

		if top_map[paths[0][0]][paths[0][1]] == 9:
			scored = []
			scores2.append(len(paths))
			for path in paths:
				if path in scored: continue
				scored.append(path)
				scores1[-1] += 1
				print("Gave score to ",path)
			print("Total part1 score for this trailhead: ", scores1[-1])
			print("Total part2 score for this trailhead:", scores2[-1])


		new_paths = []
		for path in paths:
			new_paths += find_paths(path)

		paths = new_paths
		#time.sleep(0.01)


print("Total sum of trailhead scores (part1): ", sum(scores1))
print("Total sum of trailhead scores (part2): ", sum(scores2))
print("--- %s seconds ---" % (time.time() - start_time))
