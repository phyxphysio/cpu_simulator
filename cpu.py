"""
CPU Implementation 
================================
This program is an implementaion of CPU with a counter to determine execution flow, registers to hold data, and instruction processing functions.  

Classes:
- CPU - Represents the CPU 

Usage:
1. Create an instance of the CPU class: `cpu = CPU()`
2. Adjust the counter: using set_cpu_counter and increment cpu_counter 
 

Example:
    # Create a memory bus with a size of 128
    memory_bus = MemoryBus(128)

    # Write data to memory address 00000001
    memory_bus.write_memory(00000001, 42)

    # Read data from memory address 00000001
    data = memory_bus.read_memory(00000001)
    print(data)  # Output: 42

"""



from cache import Cache
from memory import MemoryBus

# Cpmstamts 
CPU_COUNTER_INIT_VALUE = 0
NUMBER_OF_REGISTERS = 9

# Instruction Operators 
ADD_INSTRUCTION_OPERATOR = "ADD"
ADD_I_INSTRUCTION_OPERATOR = "ADDI"
JUMP_INSTRUCTION_OPERATOR = "J"
CACHE_INSTRUCTION_OPERATOR = "CACHE"

# Cache instruction values
CACHE_OFF_VALUE = 0
CACHE_ON_VALUE = 1

# Change rsiter string to index integer 

def convert_register_to_index(value):
    return int(value[1:])

# Define CPU Simulator class

class CPU:
    def __init__(self):
        self.cpu_counter = CPU_COUNTER_INIT_VALUE
        self.registers = [0] * NUMBER_OF_REGISTERS
        self.cache_flag = False
        self.cache = Cache()
        self.memory_bus = MemoryBus(128)

    # CPU countermethods

    def increment_cpu_counter(self):
        self.cpu_counter += 1

    def reset_cpu_counter(self):
        self.cpu_counter = CPU_COUNTER_INIT_VALUE

    def set_cpu_counter(self, value):
        self.cpu_counter = value

    def get_cpu_counter(self):
        return self.cpu_counter
    
    # Reset CPU Register

    def reset_registers(self):
        self.registers = [0] * NUMBER_OF_REGISTERS

    # Cache methods

    def set_cache_flag(self, value):
        self.cache_flag = bool(value)

    def search_cache(self, address):
        return self.cache.search_cache(address)

    def write_cache(self, address, value):
        self.cache.write_cache(address, value)

    # Memory methds
    def search_memory_bus(self, address):
        return self.memory_bus.search_memory_bus(address)

    def write_memory_bus(self, address, value):
        self.memory_bus.write_memory(address, value) 

    # Instruction implementations

    #Jump to a different instruction in the register

    def jump_instruction(self, target):
        self.set_cpu_counter(int(target))
    
    # Add value from source register to value from target register and store in destination register

    def add_instruction(self, destination, source, target):
        dest_index = convert_register_to_index(destination)
        src_index = convert_register_to_index(source)
        target_index = convert_register_to_index(target)
        self.registers[dest_index] = self.registers[src_index] + self.registers[target_index]

    # Add input value to one stored in source register and store result in destination register
    def add_i_instruction(self, destination, source, immediate):
        dest_index = convert_register_to_index(destination)
        src_index = convert_register_to_index(source)
        self.registers[dest_index] = self.registers[src_index] + int(immediate)

    # Turn the cache on or off to determine whether the CPU communcates directly with memory

    def cache_instruction(self, value):
        if value == CACHE_OFF_VALUE:
            self.set_cache_flag(False)
        elif value == CACHE_ON_VALUE:
            self.set_cache_flag(True)

    # Extract instructions from input file

    def parse_instruction(self, instruction):
        instruction_parts = instruction.split(",")
        operator = instruction_parts[0]
        args = instruction_parts[1:]
        print("Reading instruction:", instruction)
        self.increment_cpu_counter()

        if operator == ADD_INSTRUCTION_OPERATOR:
            self.add_instruction(*args)
        elif operator == ADD_I_INSTRUCTION_OPERATOR:
            self.add_i_instruction(*args)
        elif operator == JUMP_INSTRUCTION_OPERATOR:
            self.jump_instruction(*args)
        elif operator == CACHE_INSTRUCTION_OPERATOR:
            self.cache_instruction(*args)


    

