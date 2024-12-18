import time
start_time = time.time()

fileinput = 'day12_input'
with open(fileinput, 'r') as file:
	farmland = [[ letter for letter in line.strip()] for line in file]
shadow = [[0 for x in y] for y in farmland ]

def find_more_of_the_same(location):
	y = location[0]
	x = location[1]
	left = right = up = False #Special booleans for inner edge detection later
	matches = [] #Any square of same type as location
	fences = [] #Any space between locations that borders different types
	corners = 0
	if x < len(farmland[0])-1 and farmland[y][x+1] == farmland[y][x]: matches.append([y,x+1]); right = True
	else: fences += [0]
	if x > 0 and farmland[y][x-1] == farmland[y][x]: matches.append([y,x-1]); left = True
	else: fences += [2]
	if y < len(farmland)-1 and farmland[y+1][x] == farmland[y][x]: matches.append([y+1,x])
	else: fences += [1]
	if y > 0 and farmland[y-1][x] == farmland[y][x]: matches.append([y-1,x]); up = True
	else: fences += [3]

	if not left and up and x > 0 and farmland[y-1][x-1] == farmland[y][x]: corners += 1; print(location," inner corner to the up left") #special case for inside corners
	if left and not up and x > 0 and y > 0 and farmland[y-1][x-1] == farmland[y][x]: corners += 1; print(location," inner corner to the up left") #special case for inside corners
	if not right and up and x < len(farmland[0])-1 and farmland[y-1][x+1] == farmland[y][x]: corners += 1; print(location," inner corner to the up right") #special case for inside corners
	if right and not up and x < len(farmland[0])-1 and y > 0 and farmland[y-1][x+1] == farmland[y][x]: corners += 1; print(location," inner corner to the up right") #special case for inside corners
		
	
	for i,fence in enumerate(fences):
		for j,fence2 in enumerate(fences[i+1:]):
			if abs(fence-fence2) % 3 <=1:
				print(location,":",fence,"-",fence2,"is a corner eh")
				corners += 1
	return [matches,len(fences),corners]

def find_total_farm_areas(farmland):
	farm_areas=[]
	for y,line in enumerate(farmland):
		for x,character in enumerate(farmland):
			if shadow[y][x] > 0: continue
			print("Starting new search from [",y,",",x,"]")
			matches, fences, corners = find_more_of_the_same([y,x])
			found_area = [[y,x]] #Already mapped area
			unexplored = [] #Newly found area that requires more searching

			# Find the area
			while len(matches) > 0:
				for match in matches:
					if match in found_area: continue
					unexplored.append(match)
					found_area.append(match)
					#print(match, "is a newly found patch")
				
				matches.clear()
				for spot in unexplored:
					new_matches, new_fences, new_corners = find_more_of_the_same(spot)
					matches += new_matches
					fences += new_fences
					corners += new_corners
				unexplored.clear()

			
			print("Area mapped!")
			print("area:",found_area,"fence length:",fences,"corners/sides:",corners)
			
			for y1,x1 in found_area:
				shadow[y1][x1] = 1
			farm_areas.append([fences,corners,found_area])
	return farm_areas

lands = find_total_farm_areas(farmland)
areas = []
print(lands[0][1])
#Cost calculation etc
costs1 = costs2 = 0
for patch in lands:
	areas.append(len(patch))
	costs1 += patch[0]*len(patch[2])
	costs2 += patch[1]*len(patch[2])
print("found",len(lands),"distinct plots")

print("Answer (part1): ",costs1)
print("Answer (part2): ",costs2)
print("--- %s seconds ---" % (time.time() - start_time))
