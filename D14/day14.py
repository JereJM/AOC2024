import time
from sympy import Matrix
from sympy.matrices.normalforms import smith_normal_form

start_time = time.time()

#First case of having to become the OOPer
class Robot:
  def __init__(self, position, velocity):
    self.position = position
    self.velocity = velocity

fileinput = 'day14_input'
with open(fileinput, 'r') as file:
	lines = [line.strip() for line in file]

robots = []
for line in lines:
	p,v = line.split(" ")
	position = [int(pos) for pos in p.split("=")[1].split(",")]
	velocity = [int(vel) for vel in v.split("=")[1].split(",")]
	robots.append(Robot(position,velocity))

#All robots are not read into a list of robot objects with position and velocity. Next "simulate"

def timestep(robot,duration,room_dimensions):
	#robots = instance of class Robot
	#duration = time in seconds
	#room_dimensions = [x,y]
	pos_x = ( robot.position[0] + robot.velocity[0] * duration + room_dimensions[0] ) % room_dimensions[0]
	pos_y = ( robot.position[1] + robot.velocity[1] * duration + room_dimensions[1] ) % room_dimensions[1]
	robot.position = [pos_x,pos_y]
	return robot

def visualize_it(robots,room_dimensions,elapsed):
	room_map = [[0 for x in range(room_dimensions[0])] for y in range(room_dimensions[1])]
	for robot in robots:
		x,y = robot.position
		room_map[int(y)][int(x)] += 1
	for line in room_map:
		for pos in line:
			if pos == 0: print(".",end="")
			else: print(pos,end="")
		print("")
	print("Time:",elapsed)


elapsed = 0
room = [101,103]
first_step = 78
for robot in robots:
	robot = timestep(robot,first_step,room)
elapsed += first_step

step = 103
goal_time = 10000
while elapsed < goal_time:
	for robot in robots:
		robot = timestep(robot,step,room)
	elapsed += step
	visualize_it(robots,room,elapsed)
	time.sleep(0.1)

#Calculate safety factor
quadrants = [0,0,0,0]
for robot in robots:
	if robot.position[0] < room[0] // 2 and robot.position[1] < room[1] // 2: quadrants[0] += 1 #upper left
	elif robot.position[0] > room[0] // 2 and robot.position[1] < room[1] // 2: quadrants[1] += 1 #upper right
	elif robot.position[0] < room[0] // 2 and robot.position[1] > room[1] // 2: quadrants[2] += 1 #lower left
	elif robot.position[0] > room[0] // 2 and robot.position[1] > room[1] // 2: quadrants[3] += 1 #lower right

print(quadrants)
factor = quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]

print("Safety factor after 100 seconds of robot movement (part1): ",factor)
print("--- %s seconds ---" % (time.time() - start_time))
