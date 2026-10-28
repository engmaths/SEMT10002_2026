'''
Last week, we completed a simple simulation of a minimal CPU. We then wrote some machine code to implement some basic functions -- add, subtract and copy. 
Today, we'll extend that model by adding the ability to define and call functions. To do this, we'll need to define the instructions 'call', which can be used to call a function
and 'ret' which signifies when a function should return. 

Before we do that, we'll need to add two more functions to our basic instruction set. These are defined below. 

Next, we need to add 'call' and 'ret'. We saw in last week's seminar how a CPU handles function calls -- when a function is called, we store the line of code we need to return to, 
and then set the program counter to the line corresponding to the start of the function body. When a function returns, we need to set the program counter back to whatever it was before
the function is called plus one. Most CPUs store the return address of a function in a data structure known as a stack -- these are first-in-last-out structures. We can use a Python list as a stack, 
by using the built-in .pop() method. Calling .pop on a list will remove and return the last value in the list.

PART 1: Add the following instructions to your CPU instruction set. 

('set', r', v)  sets register r to have value v
('cpy', r1, r2) copies the value from r1 into r2
('call', n)     adds the value (pc+1) to the call stack and sets the program counter to n
('ret',)        sets the program counter to the top value of the stack. 


If you've done this correctly, should be able to run the program "P_MULTIPLY" to calculate 6 x 7, storing the result in register 0.
'''

def run(program, registers, max_steps=10000):

    # program counter - which line we're on
    pc = 0
    # number of lines executed
    steps = 0
    stack = []

    while pc < len(program):
        steps += 1
        if steps > max_steps:
            raise RuntimeError('step limit exceeded - is your program looping forever?')

        # fetch the next instruction
        instruction = program[pc]
        # decode the instruction
        op = instruction[0]

        if op == 'halt':
            break

        elif op == 'inc':
            # get the target register
            register = instruction[1]
            # add one to it
            registers[register] = registers[register] + 1
            # move to the next line
            pc += 1

        elif instruction[0] == 'dec':
            register = instruction[1]
            registers[register] = registers[register] - 1
            pc +=1

        elif instruction[0] == 'jmp':
            pc = instruction[1]

        elif instruction[0] == 'jz':
            register = instruction[1]
            if registers[register] == 0:
                pc = instruction[2]
            else:
                pc += 1

        elif op == 'set':
            registers[instruction[1]] = instruction[2]
            pc += 1

        elif op == 'cpy':
            registers[instruction[2]] = registers[instruction[1]]
            pc +=1

        elif op == 'call':
            stack.append(pc+1) #We go to the __next__ line when we return
            pc = instruction[1]

        elif op == 'ret':
            if not stack:
                raise RuntimeError('ret with empty call stack')
            pc = stack.pop()

        else:
            raise ValueError('unknown instruction: ' + str(op))

    return registers

P_add = [('jz', 1, 4), ('inc', 0), ('dec', 1), ('jmp', 0), ('halt')] #This 'program' adds whatever is in register 1 (3) to register 0 (5).
P_subtract = [('jz', 1, 4), ('dec', 0), ('dec', 1), ('jmp', 0), ('halt',)] #This 'program' subtracts whatever is in register 1 (3) from register (0).
P_copy = [('jz', 0, 5), ('dec', 0), ('inc', 1), ('inc', 2), , ('jmp', 0), ('jz', 1, 9), ('dec', 1), ('inc', 0), , ('jmp', 5), ('halt',)]

P_multiply = [
    ('set', 1, 6),     #  0   caller: put arguments in r1, r2
    ('set', 2, 7),     #  1
    ('call', 4),       #  2   call multiply (its first line is 4)
    ('halt',),         #  3   <- control returns here, answer in r0
    # ---------- multiply ----------
    ('set', 0, 0),     #  4   r0 = 0                (running total)
    ('jz', 2, 13),     #  5   outer: if r2 == 0, done
    ('cpy', 1, 10),    #  6   r10 = r1              (fresh copy of the addend)
    ('jz', 10, 11),    #  7   inner: if r10 == 0, exit inner loop
    ('inc', 0),        #  8   r0 += 1
    ('dec', 10),       #  9   r10 -= 1
    ('jmp', 7),        # 10   back to inner
    ('dec', 2),        # 11   r2 -= 1
    ('jmp', 5),        # 12   back to outer
    ('ret',),          # 13   return — answer is in r0
]

registers = [0] * 32
run(P_multiply, registers)
print(registers)
'''
PART 2: Write some machine code for implementing the power function, which calculates 2^3. You should use the multiply function given in the example above to do this.
'''

P_power = [
    ('set', 20, 2), #  0 - Set register 20 to 2
    ('set', 21, 3), # 1 - Set register 21 to 3 -- this should calculate 2^3
    ('call', 4), # 2 - Call power function (line 4)
    ('halt',),   # 3 - If we get here, the program is done.
    # --- power --- #
    ('set', 22, 1), # 4 - r22 = 1
    ('jz', 21, 12), # 5 - If register 21 is zero, return. Result is in register 0.
    ('dec', 21), # 6 - Reduce register 21 by one
    ('cpy', 20, 1),# 7 - Copy value being raised into register twenty
    ('cpy', 22, 2), # 8 - Copy accumulated value into register 2
    ('call', 13), # 9 - Multiply r20 x r22, storing result in r0
    ('cpy', 0, 22), # 10 - Copy result to register r22
    ('jmp', 5), # 11 - 
    ('ret', ), # 12
    # --- multiply --- #
    ('set', 0, 0),     #  13 / 4   r0 = 0                (running total)
    ('jz', 2, 22),     #   14 / 5   outer: if r2 == 0, done
    ('cpy', 1, 10),    #  15 / 6   r10 = r1              (fresh copy of the addend)
    ('jz', 10, 20),    #  16 / 7   inner: if r10 == 0, exit inner loop
    ('inc', 0),        #  17 / 8   r0 += 1
    ('dec', 10),       #  18 / 9   r10 -= 1
    ('jmp', 16),        # 19 / 10   back to inner
    ('dec', 2),        # 20 / 11   r2 -= 1
    ('jmp', 14),        # 21 / 12   back to outer
    ('ret',),          # 22 / 13   return — answer is in r0
]

registers = [0] * 32
run(P_power, registers)
print(registers)