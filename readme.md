# Simple Python HEX Decoder  
Python Script goes through a bin file and checks if some of the values corresponding to the data set (can be made by determined which ASM was used), in my case - it was custom thing written in rust, here's binary file:  
https://github.com/denver-code/pc_simulation_rs/blob/assembler/b.bin

## Example IN
![HEX View](https://github.com/denver-code/pc_simulation_rs/blob/assembler/%7B18A42B14-6133-4310-BCF3-05A8BBB26D8D%7D.png?raw=true)  
## Example OUT  
```
Restored Program:
FE: VER 00
09: INIT 08 05=(5)
09: INIT 10 0A=(10)
09: INIT 1F 0A=(10)
01: LOAD R1 08
01: LOAD R2 10
03: ADD R1 R2 R3
02: STORE R3 20
0A: OUT R3 03
0B: CLEAR R32 20
0B: CLEAR R8 08
0B: CLEAR R16 10
0B: CLEAR R31 1F
FE: VER 00
FF: HALT
```