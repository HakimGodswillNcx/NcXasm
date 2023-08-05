#future features::
#::::::::::::::::::
#protect variable by:
#copy var to new compare to +=1
#also check if +1 is int, not a char or symbole
#to avoid crash and cheat memory (forced)
#========================================
import sys

import setproctitle
from PyQt5.Qt import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

setproctitle.setproctitle("ncxShootGui") #change own proc name
#Global vars:
#::::::::::::
totalSoundCount=0
score=0
startUpLevel=0
currentLevelCount=0
originalGunRoom=0
shotSoundCount=0
shotSoundMax=3
bulletsLeftCount=9
bulletsBaret=9
maxBulletsAllowed=9
minBulettsAllowed=0
#CLASS customWindow(QMainWindow)
#===============================
class CustomWindow(QMainWindow):
    def paintEvent(self, event=None):
        painter = QPainter(self)
        painter.setOpacity(1.0)
        painter.setBrush(Qt.black)
        painter.setPen(QPen(Qt.black))   
        painter.drawRect(self.rect())
    def shootBTN_clicked(self):
        global shotSoundCount, bulletsLeftCount, originalGunRoom, minBulettsAllowed
        global shotSoundMax, currentLevelCount, score, totalSoundCount
        shotSoundCount = originalGunRoom + shotSoundCount + 1
        bulletsLeftCount = bulletsLeftCount -1 -originalGunRoom
        bulletsLeftLabel.setText("bullets left in gun: "+str(bulletsLeftCount)+" bulets")
        if (shotSoundCount!=0) and (bulletsLeftCount>=minBulettsAllowed):
            totalSoundCount+=1
        score=totalSoundCount
        scoreLabel.setText("score: "+str(score)+" points")
        if bulletsLeftCount<minBulettsAllowed:
            bulletsLeftCount=minBulettsAllowed
            shotSoundCount-=1
            bulletsLeftLabel.setText("bullets left in gun: "+str(bulletsLeftCount)+" bulets")
        shotSoundString = str(shotSoundCount)
        soundLabel.setText("bang!bang: "+shotSoundString+" /3 exp for next level!")
        if shotSoundCount==shotSoundMax:
            soundLabel.setText("level complete!: "+shotSoundString+" /3 shotsounds")
        if shotSoundCount>shotSoundMax:
            currentLevelCount= startUpLevel+currentLevelCount+1
            currentLeveLabel.setText("level: "+str(currentLevelCount)+" hitman")
            shotSoundCount=0
            currentSoundString=str(totalSoundCount)
            soundLabel.setText("cheatResult: "+currentSoundString+" bang!bang: "+shotSoundString+" shotsound NEXTlevel!")
    def reloadBTN_clicked(self):
        global bulletsLeftCount, maxBulletsAllowed
        bulletsLeftCount+=maxBulletsAllowed
        if bulletsLeftCount>maxBulletsAllowed:
            bulletsLeftCount=maxBulletsAllowed
        bulletsLeftString = str(bulletsLeftCount)
        bulletsLeftLabel.setText("bullets left in gun: "+bulletsLeftString+" bullets")
#============================================================ END of CLASS.

#settings variables init
#:::::::::::::::::::::::
hintFrameless = Qt.FramelessWindowHint #fullscreen
hintAlwaysOnTop = Qt.WindowStaysOnTopHint #windowed always on top
customWindowFlag=hintAlwaysOnTop #framed/framless = windowed/fullscreen

solidBackground=Qt.WA_NoSystemBackground
opacityBackground=Qt.WA_TranslucentBackground

#==============
#PROGRAM STARTS
#::::::::::::::
app = QApplication(sys.argv)
# Create the main window
window = CustomWindow()
#framed/framless = windowed/fullscreen
window.setWindowFlags(customWindowFlag)

#SOLID (switch)
window.setAttribute(solidBackground, True)
#opacity (switch)
window.setAttribute(opacityBackground, True)

# Create the Widget (MAIN opacity WINDOW/WIDGET)
mainWidget=QWidget(window)
mainWidget.setGeometry(QRect(0, 0, 999, 999))

# Create the Label (main)
soundLabel = QLabel(mainWidget)
soundLabel.setGeometry(QRect(0, 0, 555, 555))
soundLabel.setAlignment(Qt.AlignTop | Qt.AlignLeft)
soundLabel.setStyleSheet("color:"+"red"+";")
soundLabel.setText("bang!bang: "+"0"+" shotsound!")
soundLabel.setFont(QFont('Comic Sans MS', 22))
soundLabel.move(0, 0)

currentLeveLabel = QLabel(mainWidget)
currentLeveLabel.setGeometry(QRect(0, 0, 555, 555))
currentLeveLabel.setAlignment(Qt.AlignTop | Qt.AlignLeft)
currentLeveLabel.setStyleSheet("color:"+"pink"+";")
currentLeveLabel.setText("level: "+str(currentLevelCount)+" hitman")
currentLeveLabel.setFont(QFont('Comic Sans MS', 22))
currentLeveLabel.move(100, 55)

bulletsLeftLabel = QLabel(mainWidget)
bulletsLeftLabel.setGeometry(QRect(0, 0, 555, 555))
bulletsLeftLabel.setAlignment(Qt.AlignTop | Qt.AlignLeft)
bulletsLeftLabel.setStyleSheet("color:"+"green"+";")
bulletsLeftLabel.setText("bullets left in gun: "+str(bulletsLeftCount)+" bullets.")
bulletsLeftLabel.setFont(QFont('Comic Sans MS', 22))
bulletsLeftLabel.move(0, 155)

scoreLabel = QLabel(mainWidget)
scoreLabel.setGeometry(QRect(0, 0, 555, 555))
scoreLabel.setAlignment(Qt.AlignTop | Qt.AlignLeft)
scoreLabel.setStyleSheet("color:"+"orange"+";")
scoreLabel.setText("score: "+str(score)+" points.")
scoreLabel.setFont(QFont('Comic Sans MS', 22))
scoreLabel.move(0, 222)

bulletsBaretLabel = QLabel(mainWidget)
bulletsBaretLabel.setGeometry(QRect(0, 0, 555, 555))
bulletsBaretLabel.setAlignment(Qt.AlignTop | Qt.AlignLeft)
bulletsBaretLabel.setStyleSheet("color:"+"white"+";")
bulletsBaretLabel.setText("bullets in each barrette: "+"9"+" bullets.")
bulletsBaretLabel.setFont(QFont('Comic Sans MS', 22))
bulletsBaretLabel.move(0, 300)

maxBulletsAllowedLabel = QLabel(mainWidget)
maxBulletsAllowedLabel.setGeometry(QRect(0, 0, 555, 555))
maxBulletsAllowedLabel.setAlignment(Qt.AlignTop | Qt.AlignLeft)
maxBulletsAllowedLabel.setStyleSheet("color:"+"white"+";")
maxBulletsAllowedLabel.setText("max bullets allowed in gun: "+"9"+" bullets.")
maxBulletsAllowedLabel.setFont(QFont('Comic Sans MS', 22))
maxBulletsAllowedLabel.move(0, 350)

minBulettsAllowedLAbel = QLabel(mainWidget)
minBulettsAllowedLAbel.setGeometry(QRect(0, 0, 555, 555))
minBulettsAllowedLAbel.setAlignment(Qt.AlignTop | Qt.AlignLeft)
minBulettsAllowedLAbel.setStyleSheet("color:"+"yellow"+";")
minBulettsAllowedLAbel.setText("min bullets allowed in gun: "+"0"+" bullets.")
minBulettsAllowedLAbel.setFont(QFont('Comic Sans MS', 22))
minBulettsAllowedLAbel.move(0, 400)

originalGunRoomLabel = QLabel(mainWidget)
originalGunRoomLabel.setGeometry(QRect(0, 0, 555, 555))
originalGunRoomLabel.setAlignment(Qt.AlignTop | Qt.AlignLeft)
originalGunRoomLabel.setStyleSheet("color:"+"blue"+";")
originalGunRoomLabel.setText("original gun room(0): "+str(originalGunRoom)+" bullet")
originalGunRoomLabel.setFont(QFont('Comic Sans MS', 22))
originalGunRoomLabel.move(100, 500)

startUpLeveLabel = QLabel(mainWidget)
startUpLeveLabel.setGeometry(QRect(0, 0, 555, 555))
startUpLeveLabel.setAlignment(Qt.AlignTop | Qt.AlignLeft)
startUpLeveLabel.setStyleSheet("color:"+"blue"+";")
startUpLeveLabel.setText("original startup level(0): "+str(startUpLevel))
startUpLeveLabel.setFont(QFont('Comic Sans MS', 22))
startUpLeveLabel.move(100, 555)

shotSoundMaxLabel = QLabel(mainWidget)
shotSoundMaxLabel.setGeometry(QRect(0, 0, 555, 555))
shotSoundMaxLabel.setAlignment(Qt.AlignTop | Qt.AlignLeft)
shotSoundMaxLabel.setStyleSheet("color:"+"blue"+";")
shotSoundMaxLabel.setText("original max xp(3)/: "+str(shotSoundMax))
shotSoundMaxLabel.setFont(QFont('Comic Sans MS', 22))
shotSoundMaxLabel.move(100, 600)


#===========================================QPushButton
shootBTN = QPushButton(mainWidget)
shootBTN.setText("shootBTN")
shootBTN.move(64,32)
shootBTN.show()

reloadBTN = QPushButton(mainWidget)
reloadBTN.setText("reloadBTN")
reloadBTN.move(64,100)
reloadBTN.show()
#======================================================

# Run the application
window.setGeometry(QRect(0, 0, 555, 555))
window.show()
#window.showFullScreen()

#if conditions (signal/slot)
#:::::::::::::::::::::::::
shootBTN.clicked.connect(window.shootBTN_clicked)
reloadBTN.clicked.connect(window.reloadBTN_clicked)

#=================END OF PROGRAM.
#::::::::::::::::::::::::::::::::
#keep app opened until exit! (necessary) THE END.
sys.exit(app.exec_())



