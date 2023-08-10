<pre style="white-space: pre-wrap;">
(gdb) set disassembly-flavor intel

sudo cat /proc/1700388/maps
______
sudo gdb -p 1702907 -ex 'set pagination off' -ex 'info registers'
________
gcc -o ncxC  ncxTreadNoinput.c -g 
__________
(gdb) show architecture

#gdb shell ls (runs shell cmd from gdb)
</pre>
<br>

<pre style="white-space: pre-wrap;"> #python interpreter

(gdb) python
> code here (in multi lines)
>end
:: notice end to execute the script

<br>

(gdb) python gdb.execute('next')
(gdb) python bp = gdb.Breakpoint('hello.c:9')
(gdb) python bp.enabled = False
(gdb) python print(gdb.breakpoints())
</pre>

<pre style="white-space: pre-wrap;"> #commands
r (gdb) run

b(gdb) break (by adress)
i b or info breakpoints (show all breakpoints adres)
d(gdb) delete (by id) destroy all breakpoints!

(gdb) list
(gdb) layout asm
(gdb) layout regs

(gdb) reverse-stepi
(gdb) reverse-nexti
si(gdb) stepi (step in asm instruction)
ni(gdb) nexti (next asm without steping)
n(gdb) next (next line) without steping into functions
s(gdb) step (steps inside functions)
rn(gdb)reverse-next
rs(gdb)reverst-step

up -> to go to the function called the current
c (gdb)continue (run until next breakpoint)
down-> to go to next function called by current

rc(gdb) reverse-continue
bt(gdb) backtrace
finish (finish function call and stop to see steps until end of function)

w(gdb) watch (long**) 0x7ffff548
display (var) same as watch? (youcan push next and see where var changed)
undisplay (var by id number line) stop display (destroy)

(gdb) print $rip
(gdb) print *0x000deadbeef
set var x=15 (set have lot of subprocess too)
disas main
x/i $pc
x/20i *0x000deadbeef
x/x *$rip
x/10x $rbp+0x1

info locals (show local variables inside function)
info args   (show arguments variables func(args))
info variables
info registers (info have lotof suboptions) here we show registers
info func

what or whatis (varname) show the type of variable (int, char, ect)
</pre>

<pre style="white-space: pre-wrap;"> #BONUS
refresh (gdb) ref
show floats general registers (gdb) tui reg floats
</pre>
<pre style="white-space: pre-wrap;">
ctrl L = clear screen/bugs
ctrl X 2 = multipple windows
CTRL p/n = navigate previous commands
</pre>
<br>
<br>
sudo apt-get install libncurses5-dev libncursesw5-dev
<br>
