def read_binary_file(file_path):
    """Reads a binary file and returns its content."""
    with open(file_path, 'rb') as file:
        return file.read()

def hex_to_instruction(hex_code):
    """Maps hex code to specific operations."""
    instruction_set = {
        0x01: 'LOAD',     # LOAD register, address
        0x02: 'STORE',    # STORE register, address
        0x03: 'ADD',      # ADD reg1, reg2, reg3
        0x04: 'AND',      # AND reg1, reg2
        0x05: 'OR',       # OR reg1, reg2
        0x06: 'XOR',      # XOR reg1, reg2
        0x07: 'NOT',      # NOT reg
        0x08: 'JUMP',     # JUMP address
        0x09: 'INIT',     # INIT address, value
        0x0A: 'OUT',      # OUT register/value/address
        0x0B: 'CLEAR',    # CLEAR register/value/address
        0xFE: 'VER',      # VER 1/0
        0xFF: 'HALT',     # HALT
    }
    return instruction_set.get(hex_code, 'UNKNOWN')

def decode_binary_data(binary_data):
    """Decodes binary data into a structured program."""
    decoded_program = []
    i = 0
    while i < len(binary_data):
        byte = binary_data[i]
        instruction = hex_to_instruction(byte)

        # Initialize the instruction structure
        instruction_data = {
            'hex': format(byte, '02x').upper(),
            'instruction': instruction,
            'operands': []
        }

        # Handle operands based on instruction type
        if instruction == 'INIT':
            if i + 2 < len(binary_data):
                address = binary_data[i + 1]
                value = binary_data[i + 2]
                instruction_data['operands'] = [format(address, '02x').upper(), f"{format(value, '02x').upper()}=({int(value)})"]
                i += 2  # Move to the next instruction
        elif instruction == 'LOAD':
            if i + 2 < len(binary_data):
                reg = binary_data[i + 1]
                address = binary_data[i + 2]
                instruction_data['operands'] = [f'R{reg}', format(address, '02x').upper()]
                i += 2  # Move to the next instruction
        elif instruction == 'ADD':
            if i + 3 < len(binary_data):
                reg1 = binary_data[i + 1]
                reg2 = binary_data[i + 2]
                reg3 = binary_data[i + 3]
                instruction_data['operands'] = [f'R{reg1}', f'R{reg2}', f'R{reg3}']
                i += 3  # Move to the next instruction
        elif instruction == 'OUT':
            if i + 1 < len(binary_data):
                operand = binary_data[i + 1]
                instruction_data['operands'] = [f'R{operand}', format(operand, '02x').upper()]
                i += 1  # Move to the next instruction
        elif instruction == 'CLEAR':
            if i + 1 < len(binary_data):
                operand = binary_data[i + 1]
                instruction_data['operands'] = [f'R{operand}', format(operand, '02x').upper()]
                i += 1  # Move to the next instruction
        elif instruction == 'VER':
            if i + 1 < len(binary_data):
                ver = binary_data[i + 1]
                instruction_data['operands'] = [format(ver, '02x').upper()]
                i += 1  # Move to the next instruction
        elif instruction == 'STORE':
            if i + 2 < len(binary_data):
                reg = binary_data[i + 1]
                address = binary_data[i + 2]
                instruction_data['operands'] = [f'R{reg}', format(address, '02x').upper()]
                i += 2  # Move to the next instruction
        elif instruction == 'JUMP':
            if i + 1 < len(binary_data):
                address = binary_data[i + 1]
                instruction_data['operands'] = [format(address, '02x').upper()]
                i += 1  # Move to the next instruction

        # Add instruction data to the program
        decoded_program.append(instruction_data)
        i += 1  # Move to the next instruction

    return decoded_program

def restore_program(decoded_program):
    """Restores the program into a string representation."""
    program_representation = []
    for instr in decoded_program:
        operands = ' '.join(instr['operands'])
        program_line = f"{instr['hex']}: {instr['instruction']} {operands}".strip()
        program_representation.append(program_line)
    
    return "\n".join(program_representation)

def main():
    file_path = 'program.bin'
    binary_data = read_binary_file(file_path)
    decoded_program = decode_binary_data(binary_data)

    # Restore and print the program
    program_output = restore_program(decoded_program)
    print("Restored Program:")
    print(program_output)

if __name__ == '__main__':
    main()
