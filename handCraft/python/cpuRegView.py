import psutil
import pydbg

def find_proc_by_name(proc_name):
    for proc in psutil.process_iter(['pid', 'name']):
        if proc_name.lower() in proc.info['name'].lower():
            return proc.info['pid']
    return None

def print_registers(dbg):
    context = dbg.context
    print("EAX: 0x{:08x}".format(context.Eax))
    print("EBX: 0x{:08x}".format(context.Ebx))
    print("ECX: 0x{:08x}".format(context.Ecx))
    print("EDX: 0x{:08x}".format(context.Edx))
    print("ESP: 0x{:08x}".format(context.Esp))
    print("EBP: 0x{:08x}".format(context.Ebp))
    print("ESI: 0x{:08x}".format(context.Esi))
    print("EDI: 0x{:08x}".format(context.Edi))
    print("EIP: 0x{:08x}".format(context.Eip))
    # Additional registers can be accessed based on the target architecture.

def main():
    proc_name = input("Enter the process name to search for: ")
    pid = find_proc_by_name(proc_name)

    if pid is not None:
        print(f"Process '{proc_name}' found with PID: {pid}")
        dbg = pydbg.pydbg()
        try:
            dbg.attach(pid)
            print("Attached to process with PID: {}".format(pid))
            print_registers(dbg)
        except Exception as e:
            print("Error attaching to process:", e)
        finally:
            dbg.detach()
    else:
        print(f"No process with the name '{proc_name}' found.")

if __name__ == "__main__":
    main()
