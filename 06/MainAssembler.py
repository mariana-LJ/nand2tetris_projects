#!/usr/bin/env python
"""
Main module to translate Hack assembly programs into Hack machine language instructions
Author: Mariana Lopez Jaimez
Date: April 15, 2016
Project 6 From Nand to Tetris Build a Computer from Scratch (Coursera)
"""

from sys import argv
import Parser


def main():
    """
    Invokes the module Parser to make the translation from assembler to machine language
    :return: filename.hack containing binary instructions
    """

    script, filename = argv
    print "Opening Hack assembly file"
    asm_file = open(filename, 'r')
    output_file = Parser.parse_asm_file(asm_file)

    asm_file.close()
    output_file.close()


main()