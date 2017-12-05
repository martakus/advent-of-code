def jump_increment(s):
    jump_instructions = [int(num.strip()) for num in s.strip().split('\n')]
    current_instruction = 0
    counter = 0
    while 0 <= current_instruction < len(jump_instructions):
        next_instruction = current_instruction + jump_instructions[current_instruction]
        jump_instructions[current_instruction] += 1
        counter += 1
        current_instruction = next_instruction
    return counter


def jump_conditional_increment(s):
    jump_instructions = [int(num.strip()) for num in s.strip().split('\n')]
    current_instruction = 0
    counter = 0
    while 0 <= current_instruction < len(jump_instructions):
        next_instruction = current_instruction + jump_instructions[current_instruction]
        if jump_instructions[current_instruction] >= 3:
            jump_instructions[current_instruction] -= 1
        else:
            jump_instructions[current_instruction] += 1
        counter += 1
        current_instruction = next_instruction
    return counter


if __name__ == '__main__':
    with open('inputs/input5.txt') as f:
        s = f.read()
        print jump_increment(s)
        print jump_conditional_increment(s)
