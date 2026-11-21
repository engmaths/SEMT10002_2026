'''
Last week we gave our machine the ability to call functions. But writing machine code by hand is
painful: when we reused multiply inside power, every jump target in multiply had to be renumbered,
because the function had moved. Let's give ourselves the ability to instead write in assembly language,
by writing a function to convert from assembly into machine code.

Our assembly language has a few simple rules:

- One instruction per line: the instruction name, then its operands, separated by spaces.
- Anything after a # is a comment. Blank lines are ignored.
- A line that is just  name:  is a label. It names the line number of the NEXT instruction.
  It does not become an instruction itself.
- Operands come in three kinds, and you can tell which is which from how they are written:
      r5      a register
      20      a constant (only used by set)
      done    a label (the target of jmp, jz or call)

Here is our add program in assembly:

    add:
        jz r1 done # finished if r1 is 0
        inc r0 # add to r0
        dec r1 # sub from r1
        jmp add # jump back to the start.
    done:
        halt

Notice that  jz r1 done  refers to a label that hasn't appeared yet. You can't know which line
"done" is on until you've read past it. That's why an assembler makes two passes over the code:

  Pass 1: walk through the lines, counting instructions, and record the line number
          each label refers to, e.g. {'add': 0, 'done': 4}.
  Pass 2: walk through again and build one tuple per instruction, turning  r1  into 1,  20  into
          20, and each label into the number you recorded in pass 1.

PART 1: Write the function convert_assembly_to_machine_code(assembly), which takes a string of
assembly and returns a list of instruction tuples that run() can execute.

If you've done this correctly, assembling add_assy and multiply_assy should give exactly the same
tuples as P_add and P_multiply from previous weeks. 

Can you then re-write subtract in assembly?
You should be able to convert it to machine code and run the resulting machine code to confirm your
code is working.
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

P_add = [('jz', 1, 4), ('inc', 0), ('dec', 1), ('jmp', 0), ('halt',)] #This 'program' adds whatever is in register 1 (3) to register 0 (5).
P_subtract = [('jz', 1, 4), ('dec', 0), ('dec', 1), ('jmp', 0), ('halt',)] #This 'program' subtracts whatever is in register 1 (3) from register (0).

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

add_assy = '''
add:
    jz r1 done # finished if r1 is 0
    inc r0 # add to r0
    dec r1 # sub from r1
    jmp add # jump back to the start.
done:
    halt
'''

multiply_assy = '''
        set r1 6
        set r2 7
        call multiply
        halt
multiply:
        set r0 0
mul_outer:
        jz r2 mul_done
        cpy r1 r10
mul_inner:
        jz r10 mul_next
        inc r0
        dec r10
        jmp mul_inner
mul_next:
        dec r2
        jmp mul_outer
mul_done:
        ret
'''

def convert_assembly_to_machine_code(assembly_code):
    # your code goes here
    return []

add_correct = convert_assembly_to_machine_code(add_assy) == P_add
mul_correct = convert_assembly_to_machine_code(multiply_assy) == P_multiply

print("Add correct:", add_correct)
print("Mul correct:", mul_correct)

sub_assy = '''
'''

registers = [0] * 32
registers[0] = 5
registers[1] = 3

registers = run(convert_assembly_to_machine_code(sub_assy), registers)

sub_correct = registers[0] == 2
print("Sub correct:", sub_correct)

'''
PART 2: Add a comparison instruction to run():

('cmp', ra, rb, rd)   sets register rd to 0 if register ra > register rb, otherwise sets rd to 1

Notice that cmp uses 0 to mean "true". That's because jz jumps when a register is zero. 
So we can then implement 'if' by first working out a flag with cmp,
then jz on it.

    cmp r1 r2 r3      # r3 = 0 if r1 > r2
    jz r3 bigger      # so jump if r1 > r2

You'll also need to tell your assembler that cmp is a valid instruction. 

PART 3: cmp only gives us "greater than". Using cmp and the other instructions, write assembly
programs for the remaining comparisons. Each program should compare r1 with r2 and leave the
result in r0, using the same convention as cmp: r0 is 0 if the comparison is true, and anything
else if it is false.

  (a) r1 < r2
  (b) r1 <= r2
  (c) r1 >= r2

STRETCH:
  (d) r1 == r2. 
'''