Block [0x0:0x9]
---
Predecessors: []
Successors: [0xd, 0xa]
---
0x0 PUSH1 0x60
0x2 PUSH1 0x40
0x4 MSTORE
0x5 CALLDATASIZE
0x6 ISZERO
0x7 PUSH1 0xd
0x9 JUMPI
---
0x0: V0 = 0x60
0x2: V1 = 0x40
0x4: M[0x40] = 0x60
0x5: V2 = CALLDATASIZE
0x6: V3 = ISZERO V2
0x7: V4 = 0xd
0x9: JUMPI 0xd V3
---
Stack pops: 0
Stack additions: []

-----

Block [0xa:0xc]
---
Predecessors: [0x0]
Successors: [0xd]
---
0xa PUSH1 0xd
0xc JUMP
---
0xa: V0 = 0xd
0xc: JUMP 0xd
---
Stack pops: 0
Stack additions: []

-----

Block [0xd:0xf]
---
Predecessors: [0x0, 0xa]
Successors: [0x10]
---
0xd JUMPDEST
0xe PUSH1 0x47
---
0xd: JUMPDEST 
0xe: V0 = 0x47
---
Stack pops: 0
Stack additions: [0x47]

-----

Block [0x10:0x44]
---
Predecessors: [0xd]
Successors: [0x45]
---
0x10 JUMPDEST
0x11 CALLER
0x12 PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0x27 AND
0x28 PUSH1 0x0
0x2a PUSH1 0x64
0x2c PUSH1 0x40
0x2e MLOAD
0x2f DUP1
0x30 SWAP1
0x31 POP
0x32 PUSH1 0x0
0x34 PUSH1 0x40
0x36 MLOAD
0x37 DUP1
0x38 DUP4
0x39 SUB
0x3a DUP2
0x3b DUP6
0x3c DUP9
0x3d DUP9
0x3e CALL
0x3f SWAP4
0x40 POP
0x41 POP
0x42 POP
0x43 POP
0x44 POP
---
0x10: JUMPDEST 
0x11: V0 = CALLER
0x12: V1 = 0xffffffffffffffffffffffffffffffffffffffff
0x27: V2 = AND 0xffffffffffffffffffffffffffffffffffffffff V0
0x28: V3 = 0x0
0x2a: V4 = 0x64
0x2c: V5 = 0x40
0x2e: V6 = M[0x40]
0x32: V7 = 0x0
0x34: V8 = 0x40
0x36: V9 = M[0x40]
0x39: V10 = SUB V6 V9
0x3e: V11 = CALL 0x0 V2 0x64 V9 V10 V9 0x0
---
Stack pops: 0
Stack additions: []

-----

Block [0x45:0x46]
---
Predecessors: [0x10]
Successors: []
Has unresolved jump.
---
0x45 JUMPDEST
0x46 JUMP
---
0x45: JUMPDEST 
0x46: JUMP S0
---
Stack pops: 1
Stack additions: []

-----

Block [0x47:0x48]
---
Predecessors: []
Successors: []
---
0x47 JUMPDEST
0x48 STOP
---
0x47: JUMPDEST 
0x48: STOP 
---
Stack pops: 0
Stack additions: []
