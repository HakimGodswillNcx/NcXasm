import sys
import psutil
import subprocess
import time

def print_registers(pid):
    print("here is pid attached function success")
    gdbCMD='-ex "set pagination off" -ex "info registers" -ex "detach" -ex "quit"'
    gdb_command = f"sudo gdb -p {pid}"+' '+gdbCMD

    try:
        gdb_process = subprocess.Popen(gdb_command, shell=True)
        time.sleep(1)  # Adjust the delay as needed

        # Optionally, you can add more GDB commands here

        gdb_process.wait()
        gdb_output, _ = gdb_process.communicate()
        print(gdb_output)  # This will print GDB's output

    except subprocess.CalledProcessError as e:
        print(f"Error while running GDB: {e}")
def find_proc_by_name(proc_name):
    for proc in psutil.process_iter(['pid', 'name']):
        if proc_name.lower() in proc.info['name'].lower():
            return proc.info['pid']
    return None
def get_all_process_names():
    process_names = set()
    for proc in psutil.process_iter(['name']):
        process_names.add(proc.info['name'])
    return process_names
def main():
    proc_name = input("Enter the [process_name]: ")
    pid = find_proc_by_name(proc_name)

    if pid is not None:
        print(f"Process '{proc_name}' found with PID: {pid}")
        try:
            pid = int(input("Enter the PID of the process to inspect: "))
            print("Attached to process with PID: {}".format(pid))
            print_registers(pid)
        except Exception as e:
            print("Error attaching to process:", e)
    else:
        all_process_names = get_all_process_names()
        print("List of all process names:")
        for name in all_process_names:
            print(name)
        print(f"No process with the name '{proc_name}' found.")

if __name__ == "__main__":
    main()
    print("system_exit")
