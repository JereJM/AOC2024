import time

start_time = time.time()

inputfile = 'day17_input'
with open(inputfile, 'r') as file:
	lines = [line for line in file]

#I'll just accept this now
registers = {}
program = []
for line in lines:
	if "Register A" in line: 
		_,initial_value = [ val.strip() for val in line.split(":")]
		registers["A"] = int(initial_value)
	elif "Register B" in line: 
		_,initial_value = [ val.strip() for val in line.split(":")]
		registers["B"] = int(initial_value)
	elif "Register C" in line:
		_,initial_value = [ val.strip() for val in line.split(":")]
		registers["C"] = int(initial_value)
	elif "Program" in line:
		_,p = [ val.strip() for val in line.split(":")]
		program = [int(thing) for thing in p.strip().split(",")]

print("initialized registers:",registers)
print("program:",program)

def combo(operand,registers):
	if operand in [0,1,2,3]: return operand
	if operand == 4: return registers["A"]
	if operand == 5: return registers["B"]
	if operand == 6: return registers["C"]
	else: print("Invalid program!"); quit()

def ops(opcode,operand,registers):
	jumpto=False
	output=[]
	halt=False
	if opcode == 0: registers["A"] = registers["A"] // (2**combo(operand,registers)) #adv
	elif opcode == 1: registers["B"] = registers["B"] ^ operand #bxl
	elif opcode == 2: registers["B"] = combo(operand,registers) % 8 #bst
	elif opcode == 3: jumpto = operand if registers["A"] else False #jnz
	elif opcode == 4: registers["B"] = registers["B"] ^ registers["C"] #bxc
	elif opcode == 5: output.append(combo(operand,registers) % 8) #out
	elif opcode == 6: registers["B"] = registers["A"] // (2**combo(operand,registers)) #bdv
	elif opcode == 7: registers["C"] = registers["A"] // (2**combo(operand,registers)) #cdv
	else: print("invalid opcode!");halt=True
	return registers,output,jumpto,halt

def main(program,registers):
	i=0
	output = []
	while i < len(program):
		opcode = program[i]
		operand = program[i+1]
		#print("opcode:",opcode,"operand:",operand)
		registers,out,jump,halt = ops(opcode,operand,registers)
		if halt: return False
		if out: output += out
		#print(i,registers)
		if jump is not False: i = jump;
		else: i += 2
		#time.sleep(2)
	#print("run ended by reaching register",i,"- output:")
	#for out in output:
	#	print(str(out)+",",end="")
	#print("")
	return output

part1 = main(program,registers)

register_a_value = 0
output = []
while True:
	registers["A"] = register_a_value
	output = main(program,registers)
	print(register_a_value, output)
	if program == output: break #God
	divisor = 100
	if len(output) == len(program): #HACK TIME. I guess it works
		for i in range(len(output)):
			if output[-(i+1)] == program[-(i+1)]: divisor *= 10
			else: break
	register_a_value = int((register_a_value+1)*(1+1/divisor))

print("program output (part1):",part1)
print("required value for register A to make program output itself (part2):",register_a_value)
print("--- %s seconds ---" % (time.time() - start_time))
