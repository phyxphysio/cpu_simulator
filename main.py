from cpu import CPU
import json

# Get instructions and input data 
def read_config_file(config_file):
    with open (config_file, 'r') as file:
        config_data = json.load(file)
    return config_data

config_data = read_config_file('CPU_sim_project/config.json')
instruction_input_file = config_data['instruction_input_file']
data_input_file = config_data['data_input_file']

# Generate instructions
def fetch_instructions():
    with open(instruction_input_file, 'r') as instruction_file:
        instructions = instruction_file.readlines()
        instructions = [s.strip() for s in instructions]
    return instructions

# Generate list of data inputs to initialize the memory bus from.
def fetch_data():
    with open(data_input_file, 'r') as data_file:
        data = data_file.readlines()
        data = [s.strip() for s in data]
    return data

# Method to write each value from data_input file to CPU's memory bus
def initialize_memory_bus(cpu):
    data_loaded = fetch_data()
    for data in data_loaded:
        data_parsed = data.split(",")
        address, value = data_parsed[0], data_parsed[1]
        cpu.write_memory_bus(address, value)

# Method to send instructions line-by-line to CPU object
def send_instructions_to_cpu(cpu):
    instructions_loaded = fetch_instructions()
    for instruction in instructions_loaded:
        cpu.parse_instruction(instruction)

# Start of Python script to run the CPU simulator
def run_cpu_simulator():
    my_cpu = CPU()
    print("---------------------------------------------------")
    print("Welcome to the Python CPU Simulator!")
    print("---------------------------------------------------")
    print("Initializing Memory Bus from data input file...")
    initialize_memory_bus(my_cpu)
    print("Memory Bus successfully initialized")
    print("---------------------------------------------------")
    print("Sending instructions to CPU...")
    send_instructions_to_cpu(my_cpu)
    print("---------------------------------------------------")
    print("Terminating CPU Processing...")

run_cpu_simulator()