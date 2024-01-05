HIT ncx FOR help!
(home folder is /home/ncx 
MESSAGE from .bashrc)

[PROGRAMS LIST]
GameConqueror: GUI memory scan
cheathappens: GUI capstone disasm
execution-trace-viewer : GUI (trace)
xPEviewer/xELFviewer : GUI PE/ELF file view
sudo cat /proc/procID/maps
nasm: assembler
git clone <link>

nano ncx (example) edit text in terminal
subl ncx (example) edit in GUI sublime text

objdump -D inline.bin > inline.dump
cat inline.dumb
cat ~/ncx (example) will echo text in terminal
find */prefs.py ((to find file in current dir of all subdirs))
sudo find / -name libthread_db.so.0
sudo visudo ((ncx ALL = NOPASSWD: /usr/bin/gdb)) at end of file

qtcreator

[commands lists]
file_manager: nautilus
disassembler: PEfile & capstone
SUDO => gdb-peda gdb-gef gdb-pwndbg
asm_budy.py: asma 'jmp esp; inc ecx; call 0x400100' (here will convert to HEX code)
SAME PACKAG: asmd 'ffe441e8f8004000' ((here will reverse to asm code)).
radare2: Unix-like reverse engineering framework and commandline tools.
cd /home/ncx/Downloads/execution-trace-viewer && python tv.py
pyuic5 -x untitled.ui -o main.py

[configuration list]
~/ == pageDown/
./script.sh
python3 script.py
for home directory type: cd ~/
gio set /home/ncx/Desktop/gameTrainer.desktop metadata::trusted true

sudo apt update
sudo apt upgrade
pip install packageName (for python2)
pip3 install packageName (for pyton3)

pip uninstall packagename
sudo apt remove qtcreator

sudo apt install strace
python3 -m pip install distorm3
[gdb] python-ptrace pip3 install python-ptrace
_
sudo gdb -p 137998 -ex 'set pagination off' -ex 'tui enable' -ex 'layout split' -ex 'info registers' -ex continue
sudo gdb -p 137998 -ex 'set pagination off' -ex 'info registers' -ex detach -ex quit
sudo gdb -p 137998 -ex 'set pagination off' -ex 'info registers' -ex c
_

[kernel]ASLR:
cat /proc/sys/kernel/randomize_va_space
to DESABLE: echo 0 | sudo tee /proc/sys/kernel/randomize_va_space
^
to ENABLE: echo 2 | sudo tee /proc/sys/kernel/randomize_va_space
This won't survive a reboot, so you'll have to configure this in sysctl. 
Add a file /etc/sysctl.d/01-disable-aslr.conf containing:
kernel.randomize_va_space = 0
for that we do thus final line # and at the end we refresh sysctl -p # :
v
sudo echo "kernel.randomize_va_space = 0" | sudo tee /etc/sysctl.d/01-disable-aslr.conf && sudo sysctl -p

