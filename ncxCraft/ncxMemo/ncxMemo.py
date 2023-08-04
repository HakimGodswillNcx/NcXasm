import sys

from PyQt5 import Qt
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets


#=======================================================================
def convertBTN_clicked(self):
    print("convertBTN clicked")

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
    viewCpuBTN.setText("view REGS")
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
    attachBTN.setText("attach proc")
    procNameToConvert.setText("proc_NAME")
    convertBTN.setText("convert")
    convertBTN.setFont(font)
    convertBTN.setStyleSheet("background-color:purple;color:black;")
    chosenProcTxT.setText("proc_ID |oR| Proc_NAME")
    gitBTN.setText("Git Bugs Repo")
    gitBTN.setStyleSheet("background-color:blue;color:black;")
    gitBTN.setFont(font)
    hintzBTN.setText("HINTz/help")
    hintzBTN.setStyleSheet("background-color:grey;color:black;")
    hintzBTN.setFont(font)
    procIDtoConvert.setText("proc_ID")
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
    custoMainWindow.show()
    #================END.
    sys.exit(app.exec_())
