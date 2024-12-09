import time
start_time = time.time()

fileinput = 'day09_input'
symbols = []
with open(fileinput, 'r') as file:
	for line in file:
		diskmap = line.strip()

filesystem = []
idnum = 0
infile = True
for number in diskmap:
	if infile: filesystem += [str(idnum) for x in range(int(number))]; idnum += 1
	else: filesystem += ["." for x in range(int(number))]
	infile = not infile
filesystem += ["." for x in range(10)] #stuff the end for good measure

def do_part_1(fs):
	allocated = 0
	for i,index in enumerate(fs[::-1]):
		if len(fs)-i-2 <= allocated: break
		if index != ".":
			for j,idx2 in enumerate(fs[allocated:]):
				current_index = allocated+j
				if idx2 == ".": 
					allocated = current_index
					fs[current_index] = index
					fs[-i-1] = "."
					#print(['{0: <6}'.format(str(x)) for x in fs[allocated//20*20:allocated//20*20+20]])
					#time.sleep(0.01)
					break
		#print("Shuffling ",index)
	return fs

checksum=0
part_1_system = do_part_1(filesystem.copy())
for i,index in enumerate(part_1_system):
	if index != ".": checksum += i*int(index)

######## PART 2 #########
def get_chunk_size(fs_chunk):
	for i,nugget in enumerate(fs_chunk): 
		if nugget != fs_chunk[0]: return i
	return 9

lowest_fileid = 10000
for i,index in enumerate(filesystem[::-1]):
	#From end towards beginning if there's a change between list entries, check file length
	if index != filesystem[-i] and filesystem[-i] != ".":
		filesize = 0
		file_id = filesystem[-i]
		filesize = get_chunk_size(filesystem[-i:-i+10])
		if int(file_id) >= int(lowest_fileid): continue
		#Find a suitable position from as early in the filesystem as possible
		doprint = False
		for j,idx2 in enumerate(filesystem[:-i+1]):
			if filesystem[j-1] != idx2 and idx2 == ".":
				freespace = get_chunk_size(filesystem[j:j+10])
				if freespace >= filesize:
					if int(file_id) < 4010: doprint = True #Do be da debug
					if doprint: print("Filling ", filesize, "spaces (file", file_id,"):")
					if doprint: print(['{0: <6}'.format(str(x)) for x in filesystem[j-2:j+18]])
					if doprint: print(['{0: <6}'.format(str(x)) for x in filesystem[-i-2:-i+18]])
					for k,_ in enumerate(filesystem[j:j+filesize]): filesystem[j+k] = file_id
					for k,_ in enumerate(filesystem[-i:-i+filesize]): filesystem[-i+k] = "."
					if doprint: print("after")
					if doprint: print(['{0: <6}'.format(str(x)) for x in filesystem[j-2:j+18]])
					if doprint: print(['{0: <6}'.format(str(x)) for x in filesystem[-i-2:-i+18]])
					if doprint: time.sleep(1)
					lowest_fileid = file_id
					break
checksum2=0
for i,index in enumerate(filesystem):
	if index != ".": checksum2 += i*int(index)

print("checksum (part1): ", checksum)
print("checksum (part2): ", checksum2)
print("--- %s seconds ---" % (time.time() - start_time))
