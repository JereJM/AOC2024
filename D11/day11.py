import time
import threading
start_time = time.time()

fileinput = 'day11_input'
symbols = []
with open(fileinput, 'r') as file:
	series = [[int(number),1] for number in file.read().strip().split(" ")]

def check_a_number(number):
	numstr = str(number)
	numlen = len(numstr)
	if number == 0: result = [1]
	elif numlen % 2 == 0: result = [int(numstr[:numlen//2]),int(numstr[numlen//2:])]
	else: result = [number*2024]
	return result

# This dictionary holds the following information: key = unique number existing in the
# "stone row". Value = amount of occurrences of this number within the row
# Thus, dictionary_of_occurrences['4'] = 24 means there are currently 24 stones with
# the number '4' etched on them. They all behave exactly the same, so we only need to
# check the number once, and multiply the resulting new numbers by occurrence amount 24
def order_into_dictionary(list_of_numbers):
	dictionary_of_occurrences = {}
	for num in list_of_numbers: 
		key = str(num[0])
		occurrences = num[1]
		if key in dictionary_of_occurrences.keys(): dictionary_of_occurrences[key] += occurrences
		else: dictionary_of_occurrences[key] = occurrences
	return dictionary_of_occurrences

def blink(dictionary_of_occurrences):
	series = []
	for num in dictionary_of_occurrences.keys():
		key = num
		value = int(key)
		occurrences = dictionary_of_occurrences[key]
		results = check_a_number(value)
		for result in results:
			series.append( [result,occurrences] )
	return series

# Series of format [[number,occurrences],[number,occurrences]...[number,occurrences]]
# Where number is any number obtained by "blinking", and occurrences it the amount of
# inherited instances of the same number. As in, as the stones split, there eventually
# happen to be multiple of the same number somewhere along the list. This amount of
# occurrences is usually stored in the dictionary, but must also be passed through
# each blink within the list.
print(series)

##### main loop here #####
unique = order_into_dictionary(series)
total_loops = 1000
part1stones = 0
part2stones = 0
for i in range(total_loops):
	print("loop",i+1)
	series = blink(unique)
	unique = order_into_dictionary(series)
	if i+1 == 25: part1stones = sum(unique.values())
	if i+1 == 75: part2stones = sum(unique.values())
## main loop ends here! ##

print("Amount of stones after 25 blinks (part1): ", part1stones)
print("Amount of stones after 75 blinks (part2): ", part2stones)
print("Amount of stones after", total_loops,"blinks ( :D ): ", sum(unique.values()))
print("--- %s seconds ---" % (time.time() - start_time))
