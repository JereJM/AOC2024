import time

start_time = time.time()

roomfile = 'day16_input'
maze = []
with open(roomfile, 'r') as file:
	maze += [[char for char in line.strip()] for line in file]
#Generate a second grid to keep track of visited spaces
shadow = [[ 0 for x in range(len(maze[0]))] for y in range(len(maze))]

class Path:
	def __init__(self, position, direction, score):
		self.position = position
		self.direction = direction
		self.score = score

#Find our start and end points
def find_start_end(maze):
	startpoint = [0,0]
	goal = [0,0]
	for y in range(len(maze)):
		for x in range(len(maze[y])):
			if maze[y][x] == "S": 
				startpoint = [y,x]
			if maze[y][x] == "E":
				goal = [y,x]
	return (startpoint,goal)
	
def map_direction(move):
	dydx = [0,0]
	if move == "^": dydx = [-1,0]
	elif move == ">": dydx = [0,1]
	elif move == "v": dydx = [1,0]
	elif move == "<": dydx = [0,-1]
	return dydx

def visualize_it(room,spacing):
	for line in room:
		for pos in line:
			print('{0: <{1}}'.format(pos,spacing),end="")
		print("")

def find_paths(path, space):
	y,x = path.position
	paths = []
	angle = path.direction[-1]
	if x < len(space[0])-1 and space[y][x+1] != "#": 
		scorecost = 1 if angle == ">" else 1001
		paths.append(Path([y,x+1],path.direction + [">"],path.score + scorecost))
	if x > 0 and space[y][x-1] != "#":
		scorecost = 1 if angle == "<" else 1001
		paths.append(Path([y,x-1],path.direction + ["<"],path.score + scorecost))
	if y < len(space)-1 and space[y+1][x] != "#":
		scorecost = 1 if angle == "v" else 1001
		paths.append(Path([y+1,x],path.direction + ["v"],path.score + scorecost))
	if y > 0 and space[y-1][x] != "#":
		scorecost = 1 if angle == "^" else 1001
		paths.append(Path([y-1,x],path.direction + ["^"],path.score + scorecost))
	return paths


start,end = find_start_end(maze)
paths = [Path(start,[">"],0)] #initialize the first path
shadow[start[0]][start[1]] = 0
scores = []
last_update = start_time
while len(paths) > 0:
	if time.time() - last_update > 1: print("Looking at",len(paths),"paths")
	new_paths = []
	for path in paths:
		candidates = find_paths(path,maze)
		for cand in candidates:
			y,x = cand.position
			if [y,x] == end: print("Goal reached!",cand.score); scores.append(cand); continue
			#Continue as a path if first or lowest scored at position
			if shadow[y][x] == 0 or shadow[y][x] >= cand.score-1000:
				new_paths.append(cand)
				if shadow[y][x] == 0 or shadow[y][x] >= cand.score: shadow[y][x] = cand.score
	paths = new_paths
	#print([[path.position,path.direction[-1],path.score] for path in paths])
	#visualize_it(maze,1)
	#time.sleep(0.5)

#Re-walk the victory walk(s) for the part 2
best = min([c.score for c in scores])
walkable = []
for c in scores:
	if c.score == best: walkable.append(c)

#re-create shadow and use it to mark the walked path
shadow = [[ 0 for x in range(len(maze[0]))] for y in range(len(maze))]
for path in walkable:
	y,x = start
	shadow[y][x] = 1
	for step in path.direction[1:]:
		dy,dx = map_direction(step)
		y,x = y+dy,x+dx
		shadow[y][x]=1
visualize_it(shadow,1)
score = sum([sum([x for x in y]) for y in shadow])

print("all recorded scores:",[c.score for c in scores])
print("Smallest attainable score (part1):",best)
print("amount of tiles traversed by all tied best paths (part2):",score)
print("--- %s seconds ---" % (time.time() - start_time))
