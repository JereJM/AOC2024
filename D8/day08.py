import time
start_time = time.time()

fileinput = 'day08_input'
symbols = []
with open(fileinput, 'r') as file:
	symbols = [[sym for sym in line.strip()] for line in file]

#Generate a dictionary of all antenna locations separated by frequency
antennas = {}
for i,row in enumerate(symbols):
	for j,sym in enumerate(row):
		if sym != ".":
			if sym in antennas.keys(): antennas[sym].append([i,j])
			else: antennas[sym] = [[i,j]]

def place_antinode(own_loc, other_loc, area_map, apply_resonance):
	if apply_resonance:
		added_antinodes = 0

		#Immediately apply resonance points under self if not already there
		if area_map[own_loc[0]][own_loc[1]] != "#": area_map[own_loc[0]][own_loc[1]] = "#"; added_antinodes += 1
		if area_map[other_loc[0]][other_loc[1]] != "#": area_map[other_loc[0]][other_loc[1]] = "#"; added_antinodes += 1

		delta_y = own_loc[0]-other_loc[0]
		delta_x = own_loc[1]-other_loc[1]
		y = own_loc[0]
		x = own_loc[1]
		within_bounds = True
		while within_bounds:
			y += delta_y
			x += delta_x
			within_bounds = y >= 0 and y < len(area_map) and x >= 0 and x < len(area_map[0])
			if within_bounds and area_map[y][x] != "#":
				area_map[y][x] = "#"
				print(own_loc, other_loc, "->", y, x)
				added_antinodes += 1
		return added_antinodes
	else:
		y = (2*own_loc[0])-other_loc[0]
		x = (2*own_loc[1])-other_loc[1]
		within_bounds = y >= 0 and y < len(area_map) and x >= 0 and x < len(area_map[0])
		if within_bounds and area_map[y][x] != "#":
			area_map[y][x] = "#"
			return 1
		else: return 0

#Generate antinode locations for PART 1
antinode_count_1 = 0
part1_map = [x[:] for x in symbols] #Copy list
for antennatype in antennas.items():
	atype = antennatype[0]
	locs = antennatype[1]
	#print("Creating antinodes for antenna frequency",atype)
	for i,loc1 in enumerate(locs):
		for loc2 in locs[i+1:]:
			antinode_count_1 += place_antinode(loc1,loc2,part1_map,False)
			antinode_count_1 += place_antinode(loc2,loc1,part1_map,False)
	
#Generate antinode locations for PART 2
antinode_count_2 = 0
part2_map = [x[:] for x in symbols] #Copy list
for antennatype in antennas.items():
	atype = antennatype[0]
	locs = antennatype[1]
	print("Creating antinodes for antenna frequency",atype)
	for i,loc1 in enumerate(locs):
		for loc2 in locs[i+1:]:
			antinode_count_2 += place_antinode(loc1,loc2,part2_map,True)
			antinode_count_2 += place_antinode(loc2,loc1,part2_map,True)
	
for i,row in enumerate(part2_map):
	for j,sym in enumerate(row):
		print(sym, end="")
	print("")

print("total amount of unique antinodes on visible area (part1): ", antinode_count_1)
print("total amount of unique resonant antinodes on visible area (part2): ", antinode_count_2)
print("--- %s seconds ---" % (time.time() - start_time))
