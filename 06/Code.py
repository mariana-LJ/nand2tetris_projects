#!/usr/bin/env python
"""
Translates Hck assembly language mnemonics into binary codes.
Author: Mariana Lopez Jaimez
Date: April 15, 2016
Project 6 From Nand to Tetris Build a Computer from Scratch (Coursera)
"""


def get_dest_bin(mnemonic):
    """
    Returns the binary code of the 'dest' mnemonic
    :param mnemonic: String
    :return: String (3 bit representation)
    """
    dest_dict = {
        '': '000',
        'M': '001',
        'D': '010',
        'MD': '011',
        'A': '100',
        'AM': '101',
        'AD': '110',
        'AMD': '111'
    }

    if mnemonic in dest_dict:
        return dest_dict[mnemonic]
    else:
        print "Incorrect destination"
        return ""


def get_comp_bin(mnemonic):
    """
    Returns the binary code of the 'comp' mnemonic
    :param mnemonic: String
    :return: String (7 bit representation)
    """
    a = '0'
    instr_found = False
    comp_dict = {
        ('0', ''): '101010',
        ('1', ''): '111111',
        ('-1', ''): '111010',
        ('D', ''): '001100',
        ('A', 'M'): '110000',
        ('!D', ''): '001101',
        ('!A', '!M'): '110001',
        ('-D', ''): '001111',
        ('-A', '-M'): '110011',
        ('D+1', ''): '011111',
        ('A+1', 'M+1'): '110111',
        ('D-1', ''): '001110',
        ('A-1', 'M-1'): '110010',
        ('D+A', 'D+M'): '000010',
        ('D-A', 'D-M'): '010011',
        ('A-D', 'M-D'): '000111',
        ('D&A', 'D&M'): '000000',
        ('D|A', 'D|M'): '010101'
    }

    key_pairs = comp_dict.keys()
    for item in key_pairs:
        if mnemonic == item[0]:
            instr_found = True
            break
        elif mnemonic == item[1]:
            instr_found = True
            a = '1'
            break
    if instr_found:
        return a + comp_dict[item]
    else:
        print "Incorrect comp instruction"
        return ""


def get_jump_bin(mnemonic):
    """
    Returns the binary code of the 'jump' mnemonic
    :param mnemonic: String
    :return: String (3 bit representation)
    """
    jump_dict = {
        '': '000',
        'JGT': '001',
        'JEQ': '010',
        'JGE': '011',
        'JLT': '100',
        'JNE': '101',
        'JLE': '110',
        'JMP': '111'
    }

    if mnemonic in jump_dict:
        return jump_dict[mnemonic]
    else:
        print "Incorrect jump instruction"
        return ""

