<pre style="white-space: pre-wrap;"> #python interpreter
(gdb) python
> code here (in multi lines)
>end
:: notice end to execute the script
</pre>
<pre style="white-space: pre-wrap;"> #python interpreter 2
(gdb) python print(gdb.breakpoints())
:: it is inline python (single line mode)
</pre>
<pre style="white-space: pre-wrap;"> #commands
gdb -q ./helloworld -tui
(gdb) set disassembly-flavor intel
(gdb) break _start
(gdb) run
(gdb) layout asm
(gdb) layout regs

step back before breakpoint (gdb) reverse-stepi
step by step after breakpoint (gdb) stepi
step into asm instruction (gdb) nexti
</pre>
<pre style="white-space: pre-wrap;">
#variables:
target record-full (this should be done before going backwards) after breakpoint
rn or reverse-next
rs or reverst-step

p or print (look SCENARIO) stack_pointer as variable (gdb) print $sp
info locals (show local variables inside function)
info args   (show arguments variables func(args))
w or watch (look scenario) (gdb) watch (long**) x7ffff548
display (var) same as watch? (youcan push next and see where var changed)
undisplay (var by id number line) stop display (destroy)
bt or backtrace (show all relative functions before that did affect current)
finish (finish function call and stop to see steps until end of function)
what or whatis (varname) show the type of variable (int, char, ect)
</pre>
<pre style="white-space: pre-wrap;">
b or break (used on main/start) break main
d or delete (used after breakpoints) destroy breakpoints and deletes them by id number

up -> to go to the function called the current
r or run are samething (start/restart)
continue backwards (gdb) reverse-continue
c or continue (run until next breakpoint)
down-> to go to next function called by current

i b or info breakpoints (show all breakpoints adres)
info registers (info have lotof suboptions) here we show registers
set var x=15 (set have lot of subprocess too) here we make var equal 15 (edit var)

n or next (next line) without steping into functions
s or step (almost same as n/next) but steps inside functions
</pre>
<pre style="white-space: pre-wrap;"> #SCENARIO:
with the -g compiled software we can break at source code lines by number (gdb) break 9
	must set the breakpoint for gdb: (at line 9): example
		run binary as a proc (gdb) run
	         in the current line:
		        (gdb) print varName
varname is name of the memory adress and print will print current value of the variable
</pre>
<pre style="white-space: pre-wrap;"> #SCENARIO:
with the -g compiled software we can break at source code lines by number (gdb) break 9
	must set the breakpoint for gdb: (at line 9): example
		will auto_break after variable value changes (gdb) continue
	         in the current line: (gdb printing variable value changes)
		        (gdb) continue
</pre>
<pre style="white-space: pre-wrap;"> #BONUS
g++ -g hello.cpp -o hello
gdb -tui ./hello
(gdb) layout next
refresh (gdb) ref
show sourceCode (gdb) list
examine inline asm (gdb) x/i $pc
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