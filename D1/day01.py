file_path = 'day01_input'

# Read the file content into a variable
with open(file_path, 'r') as file:
    file_content = file.read()

numbers1=[]
numbers2=[]
for line in file_content.split('\n'):
	temp = line.split(";")
	if len(temp) > 1:
		numbers1.append(int(temp[0]))
		numbers2.append(int(temp[1]))

sorted_numbers1 = sorted(numbers1)
sorted_numbers2 = sorted(numbers2)

###########################################

similarity_list = []
difference = []
for i in range(len(sorted_numbers1)):
	matches = 0
	for rightside in sorted_numbers2:
		if sorted_numbers1[i] == rightside:
			matches += 1
	
	similarity_list.append(sorted_numbers1[i] * matches)

	juttu = int(sorted_numbers2[i]) - int(sorted_numbers1[i])
	difference.append(abs(juttu))

distance = 0
for value in difference:
	distance += value

similarity = 0
for value in similarity_list:
	similarity += value


print("Distance: ", distance)
print("Similarity: ", similarity)
