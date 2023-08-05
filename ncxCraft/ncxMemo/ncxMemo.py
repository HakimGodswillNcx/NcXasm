#:::::::::::::::.
#future features::
#::::::::::::::::'
#pin proc list loop to detect new created procs (and closed ones too?)
#_____________________________________________________________________
#install pyQt5 using pip3 !
#install psutil using pip3 !

import sys
import re
import subprocess
import time

import psutil

from PyQt5 import Qt
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets

#GLOBAL variables:
#::::::::::::::::::
chosenPID=0
attached=False

#=======================================================================
def convertBTN_clicked(self):
    print("convertBTN clicked")
    procName=procNameToConvert.text()
    print(procName)
    for proc in psutil.process_iter(['pid', 'name']):
        if procName.lower() in proc.info['name'].lower():
            pid=proc.info['pid']
            procIDtoConvert.setText(f"{pid}")
            return pid
    procIDtoConvert.setText("invalid_PID")

def listBTN_clicked(self):
    print("listBTN clicked")
    process_names = set()
    for proc in psutil.process_iter(['name']):
        process_names.add(proc.info['name'])
    all_process_names = process_names
    sorted_process_names = sorted(all_process_names)
    procBrowser.setText("") #cleaning buffer from welcome msg
    procNamesList=""
    for name in sorted_process_names:
        procNamesList+=name+'\n'
    procBrowser.setText(procNamesList)

def attachBTN_clicked(self):
    global chosenPID, attached
    print("attachBTN_clicked")
    if attached==False:
        for proc in psutil.process_iter(['pid', 'name']):
            if chosenProcTxT.text() in str(proc.info['pid']):
                chosenPID=proc.info['pid']
                chosenProcTxT.setText(f"Attaching... to {chosenPID}.")
                attachBTN.setText("Dis-Attach")
                attachBTN.setStyleSheet("background-color:red;color:black;")
                attached=True
                return chosenPID
            else:
                chosenPID=0
        if chosenPID == 0:
            chosenProcTxT.setText("invalid_PID")
            return chosenPID
    else:
        #detaching process
        attachBTN.setText("Attach proc")
        attachBTN.setStyleSheet("background-color:purple;color:black;")
        chosenProcTxT.setText("proc_ID-to-Attach")
        viewCpuBTN.setText("view regs")
        viewCpuBTN.setStyleSheet("background-color:yellow;color:black;")
        attached=False
        chosenPID=0
        print("i did set pid to zero")
        return chosenPID

def viewCpuBTN_clicked(self):
    global chosenPID, attached
    print("viewRegs_clicked")
    if viewCpuBTN.text()=="view regs":
        viewCpuBTN.setText("Stop RegsView")
    else:
        viewCpuBTN.setText("view regs")
    viewCpuBTN.setStyleSheet("background-color:red;color:black;")
    if chosenPID!=0 and viewCpuBTN.text()!="view regs" and attached==True:
        gdb_command = ['sudo', 'gdb', '-p', str(chosenPID), '-ex', 'set pagination off', '-ex', 'info registers', '-ex', 'detach', '-ex', 'quit']
        try:
            gdb_process = subprocess.Popen(gdb_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            #Optionally, you can add more GDB commands here
            #gdb_process.wait()
            return_code = gdb_process.wait()
            if return_code == 0:
                gdb_output, _ = gdb_process.communicate()
                gdb_output=gdb_output.decode('utf-8')
                regexPattern = r"(?s).*rax(.*?)$" #deletes everything before 'rax' including rax.
                regexed_parts = re.split(regexPattern, gdb_output, maxsplit=1)
                regexed_gdb = ''.join(regexed_parts[:-1])
                regTxT.setText(f"rax {regexed_gdb}")  # This will print GDB's output
                #regTxT.setText("gdb is on")
            else:
                error_message = f"Error executing the command. GDB returned a non-zero exit code: {return_code}"
                regTxT.setText(error_message)
            #time.sleep(1)  # Adjust the delay as needed
        except subprocess.CalledProcessError as e:
            regTxT.setText(f"Failed Popen !GDB: {e}")
            viewCpuBTN.setStyleSheet("background-color:yellow;color:black;")
            viewCpuBTN.setText("view regs")
            return chosenPID
    elif chosenPID==0:
        regTxT.setText("you forgot to attach process PID ?!")
        viewCpuBTN.setStyleSheet("background-color:yellow;color:black;")
        viewCpuBTN.setText("view regs")
        return chosenPID
    else:
        #breakLoop if you put while above (here)
        viewCpuBTN.setText("view regs")
        print("nothing to be done ELSE final")
        viewCpuBTN.setStyleSheet("background-color:yellow;color:black;")
        return chosenPID
#start program==========================================================
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    custoMainWindow = QtWidgets.QMainWindow()
    custoMainWindow.setGeometry(0, 0, 555, 555)
    custoMainWindow.setStyleSheet("color:white;background-color:black;")
    centralwidget = QtWidgets.QWidget(custoMainWindow)
    centralwidget.setObjectName("centralwidget")
    gridLayout = QtWidgets.QGridLayout(centralwidget)
    gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
    gridLayout.setObjectName("gridLayout")
    font = QtGui.QFont()
    font.setPointSize(15)
#
    listBTN =QtWidgets.QPushButton(centralwidget)
    listBTN.setObjectName("listBTN")
    gridLayout.addWidget(listBTN, 1, 0, 1, 1)
    listBTN.setStyleSheet("color:black;background-color:green;")
    listBTN.setFont(font)
    #
    viewCpuBTN =QtWidgets.QPushButton(centralwidget)
    viewCpuBTN.setObjectName("viewCpuBTN")
    viewCpuBTN.setStyleSheet("color:black;background-color:yellow;")
    gridLayout.addWidget(viewCpuBTN, 0, 6, 1, 1)
    #
    logoLabel =QtWidgets.QLabel(centralwidget)
    logoLabel.setObjectName("logoLabel")
    gridLayout.addWidget(logoLabel, 9, 6, 1, 1)
    #
    regTxT =QtWidgets.QTextBrowser(centralwidget)
    regTxT.setFont(font)
    regTxT.setStyleSheet("color:red;background-color:black;")
    regTxT.setObjectName("regTxT")
    gridLayout.addWidget(regTxT, 0, 5, 10, 1)
    #
    attachBTN =QtWidgets.QPushButton(centralwidget)
    attachBTN.setObjectName("attachBTN")
    attachBTN.setFont(font)
    gridLayout.addWidget(attachBTN, 0, 0, 1, 1)
    attachBTN.setStyleSheet("background-color:purple;color:black;")
    #
    procNameToConvert =QtWidgets.QLineEdit(centralwidget)
    procNameToConvert.setFont(font)
    procNameToConvert.setStyleSheet("background-color:white;color:black;")
    procNameToConvert.setObjectName("procNameToConvert")
    gridLayout.addWidget(procNameToConvert, 9, 0, 1, 4)
    #
    convertBTN =QtWidgets.QPushButton(centralwidget)
    convertBTN.setObjectName("convertBTN")

    gridLayout.addWidget(convertBTN, 8, 2, 1, 1)
    #
    chosenProcTxT =QtWidgets.QLineEdit(centralwidget)
    chosenProcTxT.setFont(font)
    chosenProcTxT.setStyleSheet("color:black;background-color:white;")
    chosenProcTxT.setObjectName("chosenProcTxT")
    gridLayout.addWidget(chosenProcTxT, 0, 1, 1, 4)
    #
    gitBTN =QtWidgets.QPushButton(centralwidget)
    gitBTN.setObjectName("gitBTN")
    gridLayout.addWidget(gitBTN, 8, 6, 1, 1)
    #
    hintzBTN =QtWidgets.QPushButton(centralwidget)
    hintzBTN.setObjectName("hintzBTN")
    gridLayout.addWidget(hintzBTN, 9, 4, 1, 1)
    #
    procIDtoConvert =QtWidgets.QLineEdit(centralwidget)
    procIDtoConvert.setFont(font)
    procIDtoConvert.setObjectName("procIDtoConvert")
    gridLayout.addWidget(procIDtoConvert, 8, 0, 1, 2)
    #
    procBrowser =QtWidgets.QTextBrowser(centralwidget)
    procBrowser.setFont(font)
    procBrowser.setStyleSheet("color:green;background-color:black;")
    procBrowser.setObjectName("procBrowser")
    gridLayout.addWidget(procBrowser, 1, 1, 7, 4)
    #
    custoMainWindow.setCentralWidget(centralwidget)
    custoMainWindow.setWindowTitle("ncxRegView")
    listBTN.setText("show Proc\n"
" list")
    viewCpuBTN.setText("view regs")
    viewCpuBTN.setFont(font)
    logoLabel.setText("NcX RegViewier #")
    regTxT.setHtml("""
</head>
<body style=' font-family:\'Ubuntu\'; font-size:15pt; font-weight:400; font-style:normal;\'>\n
<pre style='white-space: pre-wrap;'>
rax        0xfffffffffffffe00  -512
rbx        0x555555b5ba50      93824998554192
rcx        0x7ffff7cea45a      140737350902874
rdx        0x0         0
rsi        0x7fffffffcd8c      140737488342412
rdi        0x311b          12571
rbp        0x555555b5ba50      0x555555b5ba50
rsp        0x7fffffffcd78      0x7fffffffcd78
r8         0x0         0
r9         0x0         0
r10        0x0         0
r11        0x246           582
r12        0x7fffffffcd8c      140737488342412
r13        0x311b          12571
r14        0x0         0
r15        0x555555ab32e0      93824997864160
rip        0x7ffff7cea45a      0x7ffff7cea45a <__GI___wait4+26>
eflags     0x246           [ PF ZF IF ]
cs         0x33        51
ss         0x2b        43
ds         0x0         0
es         0x0         0
fs         0x0         0
gs         0x0         0
Detaching from program: /usr/bin/python3.10, process 12570
[Inferior 1 (process 12570) detached] (THIS IS AN EXAMPLE PREVIEW)
</pre>
</body>
</html>""")
    attachBTN.setText("Attach proc")
    procNameToConvert.setText("proc_NAME")
    convertBTN.setText("convert")
    convertBTN.setFont(font)
    convertBTN.setStyleSheet("background-color:purple;color:black;")
    chosenProcTxT.setText("proc_ID-to-Attach")
    gitBTN.setText("Git Bugs Repo")
    gitBTN.setStyleSheet("background-color:blue;color:black;")
    gitBTN.setFont(font)
    hintzBTN.setText("HINTz/help")
    hintzBTN.setStyleSheet("background-color:grey;color:black;")
    hintzBTN.setFont(font)
    procIDtoConvert.setText("invalid_PID")
    procIDtoConvert.setStyleSheet("background-color:white;color:black;")
    procBrowser.setHtml("""
</head><body style=' font-family:\'Ubuntu\'; font-size:15pt; font-weight:400; font-style:normal;\'>\n
<p style='white-space: pre-wrap;'>
here we are showing values from:
 -psutil (proc list)
 -Gnu (gdb)
 -python3 (latest)
 -qtpy5 (pip3 install)
 -cpp.UI (from QtDesign)

(tested on linux ubuntu)

lisence and more info on:
 -HiNTz/help
BUGS -> issues -> github.com
 #[NcXasm]

(OPEN SOURCE code 
 Education Purpose) &


SPECIAL THANKS QtCreator! 
        2024-2025
[GUi]                   
@NcX.
</p>
</body>
</html>""")
    
    
    convertBTN.clicked.connect(convertBTN_clicked)
    attachBTN.clicked.connect(attachBTN_clicked)
    listBTN.clicked.connect(listBTN_clicked)
    viewCpuBTN.clicked.connect(viewCpuBTN_clicked)
    custoMainWindow.show()
#============================================END.
    sys.exit(app.exec_())
#============================================END.

