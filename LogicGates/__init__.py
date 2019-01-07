from __future__ import absolute_import
name = "LogicGates"

# --- Implementing logic gates with only NAND gate ---
from .GatesWithNAND import NAND, AND, AND3
from .GatesWithNAND import NOT, OR, MultiOR, NOR, XOR, XNOR
from .GatesWithNAND import HalfAdder, Adder, HalfSubtractor, Subtractor
from .GatesWithNAND import RCA_4Bit
# --- WIP ---
#TODO:Need to see if this is needed or can be deleted
from .LogicGate import LogicGate, UnaryGate, BinaryGate
from .LogicGate import AndGate, OrGate, XorGate, Connectors
# --- THIS PROGRAM IS DESIGNED FOR INPUTS OF 0 AND 1, AND NO OTHER INPUTS ---
