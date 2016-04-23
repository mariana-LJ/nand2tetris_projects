// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, the
// program clears the screen, i.e. writes "white" in every pixel.

// Put your code here.
(BLACK)      // Blacken the entire screen
    @i
    D=M
    @end
    D=D-M
    @LOOP    
    D;JGT   // if i>end goto LOOP
    
    @addr
    A=M
    M=-1    // RAM[addr] = 1111111111111111
    
    @i
    M=M+1   // i = i + 1
    @1
    D=A
    @addr
    M=D+M   // addr = addr + 1
    @BLACK
    0;JMP

(WHITE)      // 'Clear' the entire screen
    @i
    D=M
    @end
    D=D-M
    @LOOP    
    D;JGT   // if i>end goto LOOP
    
    @addr
    A=M
    M=0    // RAM[addr] = 0000000000000000
    
    @i
    M=M+1   // i = i + 1
    @1
    D=A
    @addr
    M=D+M   // addr = addr + 1
    @WHITE
    0;JMP

(LOOP)
    @SCREEN
    D=A
    @addr       //Copy starting address for the screen
    M=D
    @8191       // Final count for the address of the screen memory block
    D=A
    @end
    M=D
    @i
    M=0

    @KBD        // If key is pressed goto BLACK
    D=M
    @BLACK
    D;JNE

    @WHITE      // If key is not pressed goto WHITE
    D;JEQ
    
    @LOOP
    0;JMP
