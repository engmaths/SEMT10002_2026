# =============================================================
# Exercise 5 - The Register Machine
# =============================================================
#
# PART 1
#
# In last week's seminar, we saw that a computer program is a set
# of instructions that a CPU can execute. Let's make this idea
# concrete by building a simulation of a very simple CPU, known as
# a register machine, and programming it in a form of "machine
# code".
#
# The CPU we'll simulate is deliberately simple. It has:
#   - Three registers (blocks of memory), each holding one integer.
#   - A program (a list of instructions and data).
#   - A program counter (pc) tracking which line to execute next.
#
# For now, our machine has only five instructions (we may add more
# later):
#
#   ('inc', r)     add 1 to register r, then move to the next line
#   ('dec', r)     subtract 1 from register r, then move to the next line
#   ('jmp', n)     jump to line n (set the program counter to n)
#   ('jz', r, n)   if register r is 0, jump to line n; else next line
#   ('halt',)      stop the machine
#
# A program is a list, each element holding one instruction and
# optionally some data. For example, the program for add is:
#
#   P_add = [('jz', 1, 4),   # if r1 == 0 jump to line 4 (finished)
#            ('inc', 0),     # r0 += 1
#            ('dec', 1),     # r1 -= 1
#            ('jmp', 0),     # go back to the top
#            ('halt',)]      # stop
#
# The first element is the tuple ('jz', 1, 4): 'jz' is the
# instruction, 1 and 4 are the data. The simulator reads one
# instruction at a time (fetch), extracts the instruction (decode)
# and applies it to the data (execute).
#
# Below is a half-built simulation of this machine. We've given you
# the fetch-decode-execute cycle and the 'halt' and 'inc'
# instructions. Complete the code so that the 'add' program below
# runs and computes r0 = r0 + r1.
# =============================================================


# Simulate a minimal register machine
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

        elif op == 'dec':
            # subtract 1 from register instruction[1], then move to the next line
            pass   # Your code here

        elif op == 'jmp':
            # set the program counter to line instruction[1]
            pass   # Your code here

        elif op == 'jz':
            # if register instruction[1] is 0, jump to line instruction[2];
            # otherwise move to the next line
            pass   # Your code here

        else:
            raise ValueError('unknown instruction: ' + str(op))

    return registers


# Add register 1 to register 0, storing the result in register 0.
P_add = [('jz', 1, 4),   # if r1 == 0 jump to line 4 (finished)
         ('inc', 0),     # r0 += 1
         ('dec', 1),     # r1 -= 1
         ('jmp', 0),     # go back to the top
         ('halt',)]      # stop

registers = [5, 3, 0]
print(run(P_add, registers))


# =============================================================
# PART 2
#
# Now that we've got a working machine, we can write more programs.
#
# 1. Write a program 'subtract' that computes r0 = r0 - r1. This
#    should only be a small change from add.
#
# 2. Write a program 'copy' that copies the value in r1 into r0
#    without destroying the value in r1. This is a trickier
#    problem - think about how you can achieve it before writing code. 
#    You'll need r2.
#
# (Tip: a one-element tuple needs its comma - write ('halt',), not
#  ('halt'), or Python treats it as a plain string.)
# =============================================================

P_subtract = []

P_copy = []
