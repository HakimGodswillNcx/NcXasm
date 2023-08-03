import os
import ptrace

def write_process_memory(pid, address, data):
    process = ptrace.getProcess(pid)
    process.writeBytes(address, data)
    process.detach()

if __name__ == "__main__":
    target_pid = 1234  # Replace this with the PID of the target process
    memory_address = 0xdeadbeef  # Replace this with the target memory address
    data_to_write = b"\x90\x90\x90"  # Replace this with the data you want to write

    write_process_memory(target_pid, memory_address, data_to_write)

