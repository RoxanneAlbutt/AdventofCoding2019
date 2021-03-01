# --- Day 2: 1202 Program Alarm ---
# 28 Feb 2021

import fileinput
from pathlib import Path

inputfilename = Path(__file__).stem + "_input.txt"

def get_input(filename):
    with open(filename) as file:
        return(list(map(int, file.read().split(","))))


def instruction_code1(address, memory):
    memory[memory[address+3]] = memory[memory[address+1]] + memory[memory[address+2]]


def instruction_code2(address, memory):
    memory[memory[address+3]] = int(memory[memory[address+1]]) * int(memory[memory[address+2]])


def process_instructions(memory):
    for address in range(0,len(memory),4):
        if memory[address + 3] <= len(memory):
            if int(memory[address]) == 1:
                    instruction_code1(address, memory)

            elif int(memory[address]) == 2:
                    instruction_code2(address, memory)

            elif int(memory[address]) == 99:
                return memory[0]
        else: return 0

    return memory[0]


def test_inputs():
    master_memory = get_input(inputfilename)

    temp_memory = []
    for i in range(0, len(master_memory)):
        temp_memory.append(master_memory[i])

    for noun in range(100):
        for verb in range(100):
            temp_memory[1] = noun
            temp_memory[2] = verb

            if process_instructions(temp_memory) == 19690720:
                print(100 * noun + verb)
                break

            temp_memory = []
            for i in range(0, len(master_memory)):
                temp_memory.append(master_memory[i])


test_inputs()

