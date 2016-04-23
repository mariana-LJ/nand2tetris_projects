#!/usr/bin/env python
"""
Defines the table of symbols to use in the translation from Hack assembler to Hack machine language
Author: Mariana Lopez Jaimez
Date: April 15, 2016
Project 6 From Nand to Tetris Build a Computer from Scratch (Coursera)
"""

# Predefined symbols
symbol_table = {
    ('SP', 'R0'): 0,
    ('LCL', 'R1'): 1,
    ('ARG', 'R2'): 2,
    ('THIS', 'R3'): 3,
    ('THAT', 'R4'): 4,
    ('R5', ): 5,
    ('R6', ): 6,
    ('R7', ): 7,
    ('R8', ): 8,
    ('R9', ): 9,
    ('R10', ): 10,
    ('R11', ): 11,
    ('R12', ): 12,
    ('R13', ): 13,
    ('R14', ): 14,
    ('R15', ): 15,
    ('SCREEN', ): 16384,
    ('KBD', ): 24576
}


def add_entry(symbol, address):
    symbol_table[(symbol, )] = str(address)


def contains(symbol):
    symbol_key_list = symbol_table.keys()
    for k in symbol_key_list:
        if symbol in k:
            return True

    return False


def get_address(symbol):
    symbol_key_list = symbol_table.keys()
    for k in symbol_key_list:
        if symbol in k:
            return int(symbol_table[k])

