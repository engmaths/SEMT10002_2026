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
            pass    # Your code here

        elif op == 'cpy':
            pass    # Your code here

        elif op == 'call':
            pass    # Your code here

        elif op == 'ret':
            pass    # Your code here

        else:
            raise ValueError('unknown instruction: ' + str(op))

    return registers

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

'''
PART 2: Write some machine code for implementing the power function, which calculates 2^3. You should use the multiply function given in the example above to do this.
'''

P_power = []