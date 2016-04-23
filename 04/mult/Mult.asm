// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

// Read R1 and copy to n
    @R1
    D=M
    @n
    M=D

// Initialize R2 to 0
    @R2
    M=0
    
(LOOP)
    @n      // if n=0 goto END
    D=M
    @END
    D;JEQ
    
    @R0     // if R0 = 1 goto FIRSTONE
    D=M-1
    @FIRSTONE
    D;JEQ
    
    @R1     // If R1 = 1, goto SECONDONE
    D=M-1
    @SECONDONE
    D;JEQ
    
    @R0     // If R0 = 0, goto ZERO
    D=M
    @ZERO
    D;JEQ
    
    
    @R1     // If R1 = 0, goto ZERO
    D=M
    @ZERO
    D;JEQ
    
    @R0
    D=M
    @R2     // R2 += R0
    M=D+M
    @n      // n--
    M=M-1
    @LOOP   // goto LOOP
    0;JMP

(FIRSTONE)  // Return R1 if R0 = 1
    @R1
    D=M
    @R2
    M=D
    @END
    0;JMP

(SECONDONE) // Return R0 if R1 = 1
    @R0
    D=M
    @R2
    M=D
    @END
    0;JMP

(ZERO)      // Return 0 if R0 = 0 or R1 = 0
    @R2
    M=0
    @END
    0;JMP
    
(END)   // infinite loop to end the program
    @END
    0;JMP
