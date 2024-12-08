import re 
import time
start_time = time.time()

fileinput = 'day06_input'

patrolarea = []
patrol_shadow = [] #A "Shadow" grid for keeping track of guard movements
player = {}
player_origin = {} #Permanent starting point
player_movement = {"<":[0,-1],">":[0,1],"^":[-1,0],"v":[1,0]}

def is_oob(location_to_check):
	if location_to_check[0] < 0 or location_to_check[0] >= len(patrolarea): return True
	if location_to_check[1] < 0 or location_to_check[1] >= len(patrolarea[0]): return True
	return False

def in_loop(location_to_check):
	y,x=location_to_check
	return player["dir"] in patrol_shadow[y][x]

def drawscreen():
	print("")
	for y,line in enumerate(patrolarea):
		for x,tile in enumerate(line):
			print(tile, end="")
		print("")

def is_forward_free(location_to_check):
	y,x = location_to_check
	return patrolarea[y][x] != "#"

def movecharacter():
	y,x = player["loc"]
	open_path = False
	while not open_path:
		y_temp,x_temp = player_movement[player["dir"]]
		newloc = [y+y_temp,x+x_temp]
		if is_oob(newloc): return 1
		if in_loop(newloc): return 2
		open_path = is_forward_free(newloc)
		if open_path: 
			patrolarea[y][x] = " "
			patrol_shadow[y][x].append(player["dir"])
			player["loc"] = newloc
			patrolarea[newloc[0]][newloc[1]] = player["dir"]
		else:
			if player["dir"] == "<": player["dir"] = "^"
			elif player["dir"] == "^": player["dir"] = ">"
			elif player["dir"] == ">": player["dir"] = "v"
			elif player["dir"] == "v": player["dir"] = "<"
	return 0
	
def load_map():
	patrolarea = []
	patrol_shadow = []
	#Read the whole patrol area into memory
	with open(fileinput, 'r') as file:
		lines = [line.strip() for line in file]
		for line in lines:
			patrolarea.append([char for char in line])
			patrol_shadow.append([[] for char in line])
	return patrolarea, patrol_shadow

patrolarea, patrol_shadow = load_map()

#Find "guard" from the visible patrol area AND calculate the amount of dots
startpoints = 1 #one for the player that already removes a "point" by being there
for y,line in enumerate(patrolarea):
	for x,tile in enumerate(line):
		if tile in ["v","<","^",">"]:
			player_origin={"loc":[y,x],"dir":tile}
		if tile == ".":
			startpoints += 1


player={"loc":[ player_origin["loc"][0],player_origin["loc"][1] ],"dir":player_origin["dir"]}
print("Found player ("+player["dir"]+") at [y:",player["loc"][0], ",x:",player["loc"][1],"]")
print("Points at the beginning: ",startpoints)

running = True
steps = 0
while running:
	steps +=1
	if steps % 500 == 0:
		drawscreen()
		time.sleep(0.1)
	status = movecharacter()
	if status > 0:
		running = False

endpoints = 0
for y,line in enumerate(patrolarea):
	for x,tile in enumerate(line):
		if tile == ".":
			endpoints += 1

print("moving on to part 2")

########### PART 2 ###########
loopcount = 0
for y,line in enumerate(patrolarea):
	for x,tile in enumerate(line):
		#reset map and player location
		patrolarea, patrol_shadow = load_map()
		player={"loc":[ player_origin["loc"][0],player_origin["loc"][1] ],"dir":player_origin["dir"]}

		if patrolarea[y][x] != ".": continue
		patrolarea[y][x] = "#"
		running = True
		steps = 0
		while running:
			steps +=1
			#if steps % 500 == 0:
			#	drawscreen()
			#	time.sleep(0.1)
			status = movecharacter()
			if status == 1:
				running = False
			if status == 2:
				loopcount += 1
				print("found loop by placing an obstacle at [y:",y, ",x:",x,"]")
				running = False



print("tiles visited (part1): ", startpoints - endpoints)
print("loops discovered (part1): ", loopcount)
print("--- %s seconds ---" % (time.time() - start_time))
