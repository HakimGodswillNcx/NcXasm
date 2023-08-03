#pip install ReadWriteMemory '(done)' readm.me website!
#add button attach memo to process (rawtext_reader)
#read write from file
#include QTpy import *
#-----------------------------------------
from ReadWriteMemory import ReadWriteMemory

rwm = ReadWriteMemory()
process = rwm.get_process_by_name("python3")
#PEfile.open(process)
#capstone???
process.open() #process.close() ?: see rwm lib's docs!

#get base adress (0x400000 example) + (0017F150) HIGH
#baseadress = 0x400000+0x17F150
#00139118+4b0
#you can put address directly without offsets
#change name of baseadress to customAdress :?
#healthponter=process.get_pointer(baseadress) 

#with offsets and base and esp:
#healthponter=process.get_pointer(baseadress, offsets=[0x4b0,0x108])

#while 1:
#value= process.read(healthpointer)
#print(value)
#AND/or
#process.write(healthpointer,500)

#run as sudo root (visudo) without infinit while loop

