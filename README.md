# Custom 16-Bit CPU & Python Assembler (Logisim)

This project implements a custom 16-bit CPU designed in Logisim, along with a Python-based assembler that converts assembly-style instructions into machine-encoded memory images for execution on the CPU.

The repository includes the full CPU hardware implementation, assembler tooling, and example programs and compiled memory images used for testing and verification.

Collaboration Note  
This project was collaboratively developed by myself and a partner. The repository reflects the CPU design, assembler, test programs, and execution workflow we built and validated together.

---

## Overview

The system integrates three components into a working execution pipeline:

1. An assembly input program written in a compact instruction format  
2. A Python assembler that parses and encodes instructions into machine code  
3. A Logisim CPU that fetches, decodes, and executes the program in simulation

The CPU supports arithmetic and memory-I/O behavior, register-based execution, and deterministic instruction sequencing.

The assembler automates program encoding and generates Logisim-compatible memory image files, allowing workloads to be loaded directly into simulated memory.

---

## Repository Contents

B127.circ — Main CPU implementation (Logisim)  
assembler.py — Custom Python assembler  
input.txt — Example assembly program  
image EXAMPLE — Example compiled memory image  
data image EXAMPLE — Additional sample memory image output  
B127 GUIDE.pdf — Architecture / reference document

The PDF is provided for architectural context and documentation — execution and tooling operate fully from the included CPU circuit and assembler.

---

## CPU Architecture Summary

The 16-bit CPU design includes:

- General-purpose register file  
- ALU supporting arithmetic and logical operations  
- Control-signal-driven instruction sequencing  
- Memory load / store behavior  
- Register-to-register execution model  
- Deterministic, clock-driven program execution

The instruction format consists of:

- Opcode field  
- Register operand fields  
- Immediate / constant fields (where applicable)

Execution pipeline (simulation-observable):

1. Instruction fetch  
2. Decode and operand selection  
3. ALU or memory execution  
4. Write-back or store operation

---

## Assembler Workflow

The Python assembler reads an input assembly program from input.txt, validates instruction structure, and encodes it into a machine-formatted Logisim memory image.

Example input:

LDR, X1, X3, 4  
ADD, X0, X1, X2  
MUL, X0, X1, X0  
STR, X3, X0, 0

The assembler performs:

- parsing and tokenization  
- operand validation  
- opcode and field encoding  
- machine-word output generation

Output is written using Logisim’s expected format:

v3.0 hex words addressed

This enables direct loading into the CPU memory module.

---

## Running the Pipeline

Step 1 — Edit or create an assembly program  
Modify input.txt or supply your own program.

Step 2 — Run the assembler

python3 assembler.py

This generates a compiled memory image file. Example outputs are included in the repository.

Step 3 — Load the program into the CPU in Logisim

1. Open B127.circ  
2. Open the memory module  
3. Load the generated image file  
4. Reset the CPU if needed  
5. Step or run simulation

You may observe:

- register state transitions  
- ALU output behavior  
- memory read / write operations  
- instruction sequencing and control flow

---

## Testing & Validation

The system was validated by:

- assembling sample program workloads  
- generating compiled memory image files  
- loading images into Logisim  
- stepping through execution  
- confirming expected register and memory results

Example inputs and outputs are provided to support reproducibility.

---
