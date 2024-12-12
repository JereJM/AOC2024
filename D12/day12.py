import time
start_time = time.time()

fileinput = 'day12_input'
with open(fileinput, 'r') as file:
	farmland = [[ letter for letter in line.strip()] for line in file]
shadow = [[0 for x in y] for y in farmland ]

def find_more_of_the_same(location):
	y = location[0]
	x = location[1]
	matches = []
	if x < len(farmland[0])-1 and farmland[y][x+1] == farmland[y][x]: matches.append([y,x+1])
	if x > 0 and farmland[y][x-1] == farmland[y][x]: matches.append([y,x-1])
	if y < len(farmland)-1 and farmland[y+1][x] == farmland[y][x]: matches.append([y+1,x])
	if y > 0 and farmland[y-1][x] == farmland[y][x]: matches.append([y-1,x])
	return [matches,fences]

def find_total_farm_areas(farmland):
	farm_areas=[]
	for y,line in enumerate(farmland):
		for x,character in enumerate(farmland):
			if shadow[y][x] > 0: continue
			print("Starting new search from [",y,",",x,"]")
			matches = find_more_of_the_same([y,x])
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
					matches += find_more_of_the_same(spot)
				unexplored.clear()

			
			print("Area mapped!")
			print(found_area)
			for y1,x1 in found_area:
				shadow[y1][x1] = 1
			farm_areas.append(found_area)
	return farm_areas

lands = find_total_farm_areas(farmland)
areas = []
for patch in lands:
	areas.append(len(patch))
print("found",len(lands),"distinct plots")
print("land areas of the "areas)

print("Answer (part1): ")
print("Answer (part2): ")
print("--- %s seconds ---" % (time.time() - start_time))
