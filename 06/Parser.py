#!/usr/bin/env python
"""
The Parser encapsulates access to the input code. It reads an assembly language command, parses it, and provides
access to the command's fields and symbols.
Author: Mariana Lopez Jaimez
Date: April 15, 2016
Project 6 From Nand to Tetris Build a Computer from Scratch (Coursera)
"""
import Code
import SymbolTable

# Command types for the Hack assembly language
A_COMMAND = 1
C_COMMAND = 2
L_COMMAND = 3


def parse_asm_file(asm_file):
    """
    Opens the input file and gets ready to parse it
    :param filename: Hack assembly file name
    :return: Hack file with the translated instructions in binary
    """
    print "Creating output file: filename.hack"
    # Get the name for the output file from the .asm file
    out_filename = asm_file.name.split('.')[0]
    # Concatenate correct file extension (.hack)
    out_filename += ".hack"
    # Create the file if it doesn't exist. It doesn't truncate the file if it exists
    hack_file = open(out_filename, 'a')

    # First pass: Building the symbol table
    rom_address = 0
    for line in asm_file:
        # Remove trailing or leading white spaces of the line
        line = line.strip()
        # Ignore empty lines or comments
        if not (line.startswith("//") or not line):
            command = get_command_type(line)
            if command == A_COMMAND or command == C_COMMAND:
                rom_address += 1
            if command == L_COMMAND:
                new_symbol = line[1:-1]  # Strip off parentheses
                SymbolTable.add_entry(new_symbol, rom_address)
    print "First pass ended"

    # Second pass: take into account variables and add them to the symbol table if needed
    ram_address = 16    # This is the starting point for ram addresses (see SymbolTable.py)
    asm_file.seek(0, 0)     # Return to the first line
    for line in asm_file:
        instruction = ""  # Clean instruction
        # Remove trailing or leading white spaces of the line
        line = line.strip()
        # Ignore empty lines or comments
        if not (line.startswith("//") or not line):
            command_type = get_command_type(line)
            command = line
            command = clean_command(command)
            if command_type == A_COMMAND:
                if command_type == A_COMMAND:
                    command = line[1:]      # Strip off '@'
                if command.isdigit():
                    instruction += get_symbol(int(command))
                # If @symbol, look up on the symbol table and replace with the numeric value
                # or add new symbol if not found
                else:
                    if SymbolTable.contains(command):
                        value = SymbolTable.get_address(command)
                        instruction = get_symbol(value)
                    else:
                        SymbolTable.add_entry(command, ram_address)
                        instruction = get_symbol(ram_address)
                        ram_address += 1
            elif command_type == C_COMMAND:
                instruction += '111'
                instruction += get_comp(command)
                instruction += get_dest(command)
                instruction += get_jump(command)
            # Write instruction if it is not empty
            if instruction != "":
                hack_file.write(instruction+'\n')
    print "Translation to binary code ended"
    return hack_file


def get_command_type(line):
    """
    Returns the type of the current command
    :param line: Current command
    :return: A_COMMAND, C_COMMAND, L_COMMAND
    """
    if line.startswith('@'):
        return A_COMMAND
    elif line.startswith('('):
        return L_COMMAND
    else:
        return C_COMMAND


def get_symbol(value):
    """
    Returns the symbol or decimal Xxx of the current command @Xxx or (Xxx). Should be called only when command_type()
    is A_COMMAND or L_COMMAND
    :param line: Current command (A-command or L-command)
    :return: String
    """
    # Generate binary value
    instruction = "{0:b}".format(value)
    # Prepend zeros until 15 characters are reached
    zeros = '0' * (15 - len(instruction))
    instruction = zeros + instruction
    # Prepend 0 opcode (Most significant bit of instruction)
    instruction = '0' + instruction

    return instruction


def get_dest(c_command):
    """
    Returns the 'dest' mnemonic in the current C-command (8 possibilities). Should be called only when command_type()
    is C_COMMAND
    :param c_command: String
    :return: String
    """
    # Get the mnemonic for the destination part of the C-command
    if '=' in c_command:
        dest_str = c_command.split('=')[0]
    else:
        dest_str = ""
    dest = Code.get_dest_bin(dest_str)
    return dest


def get_comp(c_command):
    """
    Returns the 'comp' mnemonic in the current C-command (28 possibilities). Should be called only when
    command_type() is C_COMMAND
    :param c_command: String
    :return: String
    """
    if '=' in c_command:
        c_command = c_command.split('=')[1]
    if ';' in c_command:
        c_command = c_command.split(';')[0]
    comp = Code.get_comp_bin(c_command)
    return comp


def get_jump(c_command):
    """
    Returns the 'jump' mnemonic in the current C-command (8 possibilities). Should be called only when command_type()
    is C_COMMAND
    :param c_command: String
    :return: String
    """
    # Get the mnemonic for the jump part of the C-command
    if ';' in c_command:
        jump_str = c_command.split(';')[-1]
    else:
        jump_str = ""
    jump = Code.get_jump_bin(jump_str)
    return jump


def clean_command(command):
    """
    Strips off white spaces and comments from a line of code that corresponds to a command
    :param command: String containing a command
    :return command: String containing the command without spaces or comments
    """
    command = command.replace(" ", "")  # Remove white spaces
    # Remove comments
    if '//' in command:
        command = command.split('//')[0]
    return command


def check_syntax(command):
    is_command_valid = True
    valid_symbol_chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                          'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    command_type = get_command_type(command)
    if command_type == A_COMMAND:
        value = command[1:]
        if value.isdigit() and int(value) < 0:
            is_command_valid = False
            print "For A-instructions, the value in @value must be positive"
        else:
            if value[0].isdigit():
                is_command_valid = False
                print "For A-instructions, the value in @value must not start with a digit."

    elif command_type == L_COMMAND:
        pass
    else:
        pass

    return is_command_valid