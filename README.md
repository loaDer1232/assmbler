# assmbler
a pain
# basic over view of plan               
the idea is that you put your assmbley code into in.txt and the program will produce a binary in rom.bin                
## example                  
take the following assmbley program for "hello, world"
```
global _start

section .text

_start:
  mov rax, 1        ; write(
  mov rdi, 1        ;   STDOUT_FILENO,
  mov rsi, msg      ;   "Hello, world!\n",
  mov rdx, msglen   ;   sizeof("Hello, world!\n")
  syscall           ; );

  mov rax, 60       ; exit(
  mov rdi, 0        ;   EXIT_SUCCESS
  syscall           ; );

section .rodata
  msg: db "Hello, world!", 10
  msglen: equ $ - msg
```
the out put would be 
```