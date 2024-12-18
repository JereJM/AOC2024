import time

start_time = time.time()

roomfile = 'day15_input'
warehouse = []
with open(roomfile, 'r') as file:
	warehouse += [[char for char in line.strip()] for line in file]
widehouse = []
for line in warehouse:
	newline = []
	for char in line:
		if char == "#": newline += ["#","#"]
		elif char == "O": newline += ["[","]"]
		elif char == ".": newline += [".","."]
		elif char == "@": newline += ["@","."]
	widehouse.append(newline)
movefile = 'day15_input_2'
moves = ""
with open(movefile, 'r') as file:
	for line in file:
		moves += line.strip() 

def check_free_movement_2(room,location,direction):
	y = location[0]
	x = location[1]
	dy = direction[0]
	dx = direction[1]
	to_move = [[y,x]]
	if room[y+dy][x+dx] == ".": return (True,to_move)
	if room[y+dy][x+dx] == "#": return (False,[])
	if room[y+dy][x+dx] == "O":
		to_move.append([y+dy,x+dx])
		new_barrels = [[y+dy,x+dx]]
		while len(new_barrels) > 0:
			#bx and by stand for BARREL_X AND BARREL_Y
			#this loop searches through the barrel chain
			#and stops with a return if it encounters walls ahead anywhere
			newest_barrels = []
			for by,bx in new_barrels:
				check_position = room[by+dy][bx+dx]
				if check_position == "O": 
					newest_barrels.append([by+dy,bx+dx])
				elif check_position == "#": return (False,[])
			if newest_barrels: to_move += newest_barrels
			new_barrels = newest_barrels
	if room[y+dy][x+dx] in ["[","]"]:
		bdy,bdx = map_direction(room[y+dy][x+dx])
		to_move.append([y+dy,x+dx])
		to_move.append([y+dy+bdy,x+dx+bdx])
		new_barrels = [[y+dy,x+dx],[y+dy+bdy,x+dx+bdx]]
		while len(new_barrels) > 0:
			#bx and by stand for BARREL_X AND BARREL_Y
			#this loop searches through the barrel chain
			#and stops with a return if it encounters walls ahead anywhere
			newest_barrels = []
			for by,bx in new_barrels:
				check_position = room[by+dy][bx+dx]
				if check_position in ["[","]"] and [by+dy,bx+dx] not in to_move: 
					bdy,bdx = map_direction(check_position)
					newest_barrels.append([by+dy,bx+dx])
					newest_barrels.append([by+dy+bdy,bx+dx+bdx])
				elif check_position == "#": return (False,[])
				
			new_barrels.clear()
			for barrel in newest_barrels:
				if barrel not in to_move: 
					to_move.append(barrel)
					new_barrels.append(barrel)
	return (True,to_move)

def visualize_it(room):
	for line in room:
		for pos in line:
			print(pos,end="")
		print("")

def map_direction(move):
	dydx = [0,0]
	if move == "^": dydx = [-1,0]
	elif move == ">": dydx = [0,1]
	elif move == "v": dydx = [1,0]
	elif move == "<": dydx = [0,-1]
	elif move == "[": dydx = [0,1]
	elif move == "]": dydx = [0,-1]
	return dydx

def main_simulation(play_area,moveset,visualize):
	#Start by finding our robot
	robot_location = [0,0]
	for y in range(len(play_area)):
		for x in range(len(play_area[y])):
			if play_area[y][x] == "@": robot_location = [y,x]

	for move in moves:
		direction = map_direction(move)
		ok_to_move,movables = check_free_movement_2(play_area,robot_location,direction)
		if ok_to_move:
			y,x = robot_location
			#Move the stack of items that you have to move like this:
			# @OoOo. -> @OoO.o -> @Oo.Oo -> @O.oOo -> @.OoOo -> .@OoOo
			#Basically, whatever the direction, just iterate from end to start
			for my,mx in reversed(movables):
				dy,dx = direction
				play_area[my+dy][mx+dx] = play_area[my][mx]
				play_area[my][mx] = "."
			robot_location = [y+direction[0],x+direction[1]]
		if visualize:
			visualize_it(play_area)
			print(robot_location,move,direction)
			time.sleep(0.1)

	#End by calculating GPS score
	gps_score = 0
	for y in range(len(play_area)):
		area_width = len(play_area[y])
		for x in range(area_width):
			if play_area[y][x] in ["O","["]: gps_score += 100*y+x
	return gps_score

######## DOWN HERE THE MAGIC HAPPENS #########
part1 = main_simulation(warehouse,moves,False)
part2 = main_simulation(widehouse,moves,True)

print("GPS score after robot has finished doing its movement routine (part1):",part1)
print("GPS score after robot has finished doing its movement routine (part2):",part2)
print("--- %s seconds ---" % (time.time() - start_time))
