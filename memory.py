"""
Memory Bus Implementation 
================================
This program is an implementaion of a memory bus, as outlined in the project promp. 
A memory bus allows the CPU to read from and write to specific memory addresses. 

Classes:
- MemoryBus - Represents the memory bus and provides methods for memory access. 

Usage:
1. Create an instance of the MemoryBus class: `memory_bus = MemoryBus(size)`, where `size` is the desired memory size.
2. Read from memory: `data = memory_bus.read_memory(address)`, where `address` is the memory address to read from.
3. Write to memory: `memory_bus.write_memory(address, value)`, where `address` is the memory address to write to and
   `value` is the data to be written.
4. Initalize memory addresses that are 8-bit binary  

Example:
    # Create a memory bus with a size of 128
    memory_bus = MemoryBus(128)

    # Write data to memory address 00000001
    memory_bus.write_memory(00000001, 42)

    # Read data from memory address 00000001
    data = memory_bus.read_memory(00000001)
    print(data)  # Output: 42

"""
class MemoryBus:
    """
    Represents memory bus. 

    Attributes:
        memory (dict): Dictionary representing the memory bus. Key: 8-bit binary string address, Value: Data value.
        size (int): Size of the memory bus.
    
    Methods:
        read_memory(address): Reads data from the specified memory address.
        write_memory(address, value): Writes data to the specified memory address.
        init_memory(value): Fills memory dictionar with addresses that are 8-bit binary strings
        _generate_addresses(): Internal method used to generate binary strings that become memory addresses 


    """


    def __init__(self, size):

        """
        Initializes the MemoryBus object.

        Parameters:
            size (int): Sets the number of addresses in the memory bus

        """
        self.memory = {}
        self.size = size

    def read_memory(self, address):

        """
        Reads data from the specified memory address.

        Parameters:
            address (str): 8-bit binary string representing the memory address to read from.

        Returns:
            str: Data read from the memory address.

        Raises:
            ValueError: If the memory address is invalid or not present in the memory bus.

        """

        if address in self.memory:
            return self.memory[address]
        else:
            raise ValueError('Invalid memory address')
    
    def write_memory(self, address, value):

        """
        Writes data to the specified memory address.

        Parameters:
            address (str): 8-bit binary string representing the memory address to write to.
            value: Data to be written.

        Raises:
            ValueError: If the memory address is invalid or the value is not of the expected type.

        """
        if len(address) == 8:
            self.memory[address] = value
        else:
            raise ValueError('Invalid memory address')
    
    def init_memory(self, value=0):

        """
        Initalizes memory addresses

        Attributes: 
            value (int): starting value of memory addresses 

        """

        self.memory = {address: value for address in self._enerate_addresses()}
    
    def _generate_addresses(self):
        """
        Generates binary strings for memory dictionary
        
        """
        for i in range(self.size):
            yield format(i, "08b")


