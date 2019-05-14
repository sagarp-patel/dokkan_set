import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from DokkanSelector import *
from functools import partial

class Window(QMainWindow):
    def __init__ (self):
        super().__init__()
        self.homePage = QtWidgets.QWidget()
        self.insertDataPage = QtWidgets.QWidget()
        self.singleSummonPage = QtWidgets.QWidget()
        self.multiSummonPage = QtWidgets.QWidget()
        self.dSummons = DokkanSummons() # This class contains all the logic of the Project
        self.stackedLayout = QtWidgets.QStackedLayout()
        #Inserting Main Pages Shown at the HomeScreen here
        #Will add one for Generate Plot here soon
        self.stackedLayout.addWidget(self.homePage)
        self.stackedLayout.addWidget(self.insertDataPage)
        #Central Widget of the UI
        self.centralWidget = QWidget()
        self.centralWidget.setLayout(self.stackedLayout)
        self.setCentralWidget(self.centralWidget)
        #Window Settings such as Title, Size etc
        self.setWindowTitle("Dokkan Summon Predictor")
        self.setGeometry(300, 50, 300,250)
        self.init_ui()
        self.show()
        #      self.stackedLayout.addWidget


    def init_ui(self):
        #creates the homepage layout, adds all the buttons etc
        self.homePageLayout = QVBoxLayout()
        self.genPlotButton = QtWidgets.QPushButton("Generate Plot")
        self.predictButton = QtWidgets.QPushButton("Predict Summons")
        self.insertButton = QtWidgets.QPushButton("Insert Data")
        self.homePageLayout.addWidget(self.genPlotButton)
        self.homePageLayout.addWidget(self.insertButton)
        self.homePageLayout.addWidget(self.predictButton)
        self.homePage.setLayout(self.homePageLayout)
        #Connect All the Buttons to their respective fucntions
        self.insertButton.clicked.connect(self.insertData)
        self.predictButton.clicked.connect(self.predictSummons)
        self.genPlotButton.clicked.connect(self.generatePlot)



    def generatePlot(self):
        #self.dSummons.minPulled() # Was just a test
        self.dSummons.createPlot()

    def insertData(self):
        self.hrLineEdit = QtWidgets.QLineEdit()
        self.minLineEdit = QtWidgets.QLineEdit()
        self.secLineEdit = QtWidgets.QLineEdit()
        self.create_insertData_Page()
        #self.stackedLayout.addWidget(self.insertDataPage)
        #self.stackedLayout.setCurrentIndex(1)

    def create_insertData_Page(self):
        #This function will create a simple List that will be used to navigate through
        #different insert pages depending upon the summon type
        self.summonTypeList = QListWidget()
        self.multiSummonItem = QListWidgetItem("Multi Summon")
        self.singleSummonItem = QListWidgetItem("Single Summon")
        self.doubleRateSummonItem = QListWidgetItem("Double Rate Summon")
        self.gssrSummonItem = QListWidgetItem("GSSR Summon")
        self.ticketSummonItem = QListWidgetItem("Ticket Summon")
        self.summonTypeList.insertItem(0,self.singleSummonItem)
        self.summonTypeList.insertItem(1,self.multiSummonItem)
        self.summonTypeList.insertItem(2,self.doubleRateSummonItem)
        self.summonTypeList.insertItem(3,self.gssrSummonItem)
        self.summonTypeList.insertItem(4,self.ticketSummonItem)
        self.summonTypeList.setCurrentItem(self.singleSummonItem) # Set the default to Single Summon For the List
        self.insertDataLayout = QVBoxLayout()
        self.insertDataLayout.addWidget(self.summonTypeList)
        self.insertDataPage.setLayout(self.insertDataLayout)
        #Moves over to default page which is the Single Summon Layout
        if self.summonTypeList.currentRow() == 0:
            self.singleSummonLayout()
        elif self.summonTypeList.currentRow() == 1:
            self.multiSummonLayout()
        elif self.summonTypeList.currentRow() == 2:
            self.gssrSummonLayout()
        elif self.summonTypeList.currentRow() == 3:
            self.doubleRateSummonLayout()
        elif self.summonTypeList.currentRow() == 4:
            self.customSummonLayout()


    def predictSummons(self):
        self.dSummons.prediction()

    def multiSummonLayout(self):
        #Creates all the UI items and adds them to the multisummon Page
        print("Multi Summon Layout Started")
        #Create items for layout
        self.msSummonTypeList = QListWidget()
        self.msMultiSummonItem = QListWidgetItem("Multi Summon")
        self.msSingleSummonItem = QListWidgetItem("Single Summon")
        self.msDoubleRateSummonItem = QListWidgetItem("Double Rate Summon")
        self.msGssrSummonItem = QListWidgetItem("GSSR Summon")
        self.msTicketSummonItem = QListWidgetItem("Ticket Summon")
        self.msSummonTypeList.insertItem(0,self.msSingleSummonItem)
        self.msSummonTypeList.insertItem(1,self.msMultiSummonItem)
        self.msSummonTypeList.insertItem(2,self.msDoubleRateSummonItem)
        self.msSummonTypeList.insertItem(3,self.msGssrSummonItem)
        self.msSummonTypeList.insertItem(4,self.msTicketSummonItem)
        rareLvlLabel = QtWidgets.QLabel("Rare")
        srLvlLabel = QtWidgets.QLabel("SR")
        ssrLvlLabel = QtWidgets.QLabel("SSR")
        timeLabel = QtWidgets.QLabel("Time: ")
        hrLabel = QtWidgets.QLabel("hr")
        minLabel = QtWidgets.QLabel("min")
        secLabel = QtWidgets.QLabel("s")
        self.msHrLineEdit = QtWidgets.QLineEdit()
        self.msMinLineEdit = QtWidgets.QLineEdit()
        self.msSecLineEdit = QtWidgets.QLineEdit()
        introAnimeLabel = QtWidgets.QLabel("Intro Animation")
        addDataButton = QtWidgets.QPushButton("Add")
        dayLabel = QtWidgets.QLabel("Day: ")
        self.msDayComboBox = QComboBox()
        self.msDayComboBox.addItem("Sunday")
        self.msDayComboBox.addItem("Monday")
        self.msDayComboBox.addItem("Tuesday")
        self.msDayComboBox.addItem("Wednesday")
        self.msDayComboBox.addItem("Thursday")
        self.msDayComboBox.addItem("Friday")
        self.msDayComboBox.addItem("Saturday")
        self.msRarelvlComboBox = QComboBox()
        self.msRarelvlComboBox.addItem("0")
        self.msRarelvlComboBox.addItem("1")
        self.msRarelvlComboBox.addItem("2")
        self.msRarelvlComboBox.addItem("3")
        self.msRarelvlComboBox.addItem("4")
        self.msRarelvlComboBox.addItem("5")
        self.msRarelvlComboBox.addItem("6")
        self.msRarelvlComboBox.addItem("7")
        self.msRarelvlComboBox.addItem("8")
        self.msRarelvlComboBox.addItem("9")
        self.msRarelvlComboBox.addItem("10")
        self.msSrlvlComboBox = QComboBox()
        self.msSrlvlComboBox.addItem("0")
        self.msSrlvlComboBox.addItem("1")
        self.msSrlvlComboBox.addItem("2")
        self.msSrlvlComboBox.addItem("3")
        self.msSrlvlComboBox.addItem("4")
        self.msSrlvlComboBox.addItem("5")
        self.msSrlvlComboBox.addItem("6")
        self.msSrlvlComboBox.addItem("7")
        self.msSrlvlComboBox.addItem("8")
        self.msSrlvlComboBox.addItem("9")
        self.msSrlvlComboBox.addItem("10")
        self.msSsrlvlComboBox = QComboBox()
        self.msSsrlvlComboBox.addItem("0")
        self.msSsrlvlComboBox.addItem("1")
        self.msSsrlvlComboBox.addItem("2")
        self.msSsrlvlComboBox.addItem("3")
        self.msSsrlvlComboBox.addItem("4")
        self.msSsrlvlComboBox.addItem("5")
        self.msSsrlvlComboBox.addItem("6")
        self.msSsrlvlComboBox.addItem("7")
        self.msSsrlvlComboBox.addItem("8")
        self.msSsrlvlComboBox.addItem("9")
        self.msSsrlvlComboBox.addItem("10")
        singleSummonPageLayout = QVBoxLayout()
        isFeaturedLabel = QtWidgets.QLabel("Featured")
        self.msIsFeaturedComboBox = QComboBox()
        self.msIsFeaturedComboBox.addItem("0")
        self.msIsFeaturedComboBox.addItem("1")
        self.msIsFeaturedComboBox.addItem("2")
        self.msIsFeaturedComboBox.addItem("3")
        self.msIsFeaturedComboBox.addItem("4")
        self.msIsFeaturedComboBox.addItem("5")
        self.msIsFeaturedComboBox.addItem("6")
        self.msIsFeaturedComboBox.addItem("7")
        self.msIsFeaturedComboBox.addItem("8")
        self.msIsFeaturedComboBox.addItem("9")
        self.msIsFeaturedComboBox.addItem("10")
        cancelButton = QtWidgets.QPushButton("Cancel")
        #Create Layouts
        hBoxLayout = QHBoxLayout()
        cardLvlLayout = QHBoxLayout()
        featuredLayout = QHBoxLayout()
        dayLayout = QHBoxLayout()
        self.multiSummonPageLayout = QVBoxLayout()
        #insert items into the layouts
        hBoxLayout.addWidget(timeLabel)
        hBoxLayout.addWidget(hrLabel)
        hBoxLayout.addWidget(self.msHrLineEdit)
        hBoxLayout.addWidget(minLabel)
        hBoxLayout.addWidget(self.msMinLineEdit)
        hBoxLayout.addWidget(secLabel)
        hBoxLayout.addWidget(self.msSecLineEdit)
        hBoxLayout.addStretch()
        featuredLayout.addWidget(isFeaturedLabel)
        featuredLayout.addWidget(self.msIsFeaturedComboBox)
        cardLvlLayout.addWidget(rareLvlLabel)
        cardLvlLayout.addWidget(self.msRarelvlComboBox)
        cardLvlLayout.addWidget(srLvlLabel)
        cardLvlLayout.addWidget(self.msSrlvlComboBox)
        cardLvlLayout.addWidget(ssrLvlLabel)
        cardLvlLayout.addWidget(self.msSsrlvlComboBox)
        cardLvlLayout.addStretch()
        dayLayout.addWidget(dayLabel)
        dayLayout.addWidget(self.msDayComboBox)
        dayLayout.addStretch()
        self.multiSummonPageLayout.addWidget(self.msSummonTypeList)
        self.msSummonTypeList.setCurrentItem(self.msMultiSummonItem)
        self.multiSummonPageLayout.addLayout(cardLvlLayout)
        self.multiSummonPageLayout.addLayout(featuredLayout)
        self.multiSummonPageLayout.addLayout(hBoxLayout)
        self.multiSummonPageLayout.addLayout(dayLayout)
        self.multiSummonPageLayout.addWidget(addDataButton)
        self.multiSummonPageLayout.addWidget(cancelButton)
        self.multiSummonPage.setLayout(self.multiSummonPageLayout)
        #Need to Remove this part of the code from here and move it to display
        #So we don't keep on creating things again and again
        self.stackedLayout.addWidget(self.multiSummonPage)
        self.stackedLayout.setCurrentIndex(2)
        self.msSummonTypeList.currentRowChanged.connect(self.displayLayout)
        addDataButton.clicked.connect(self.addMultiSummon)
        #addDataButton.connect(addDataButton,QtCore.SIGNAL('clicked()'),self.addMultiSummon(hrLineEdit.text()))
        cancelButton.clicked.connect(self.viewHome)

    def singleSummonLayout(self):
        print("Check Point Here")
        self.ssSummonTypeList = QListWidget()
        self.ssMultiSummonItem = QListWidgetItem("Multi Summon")
        self.ssSingleSummonItem = QListWidgetItem("Single Summon")
        self.ssDoubleRateSummonItem = QListWidgetItem("Double Rate Summon")
        self.ssGssrSummonItem = QListWidgetItem("GSSR Summon")
        self.ssTicketSummonItem = QListWidgetItem("Ticket Summon")
        self.ssSummonTypeList.insertItem(0,self.ssSingleSummonItem)
        self.ssSummonTypeList.insertItem(1,self.ssMultiSummonItem)
        self.ssSummonTypeList.insertItem(2,self.ssDoubleRateSummonItem)
        self.ssSummonTypeList.insertItem(3,self.ssGssrSummonItem)
        self.ssSummonTypeList.insertItem(4,self.ssTicketSummonItem)
        cardLvlLabel = QtWidgets.QLabel("Rarity")
        timeLabel = QtWidgets.QLabel("Time: ")
        hrLabel = QtWidgets.QLabel("hr")
        minLabel = QtWidgets.QLabel("min")
        secLabel = QtWidgets.QLabel("s")
        self.ssHrLineEdit = QtWidgets.QLineEdit()
        self.ssMinLineEdit = QtWidgets.QLineEdit()
        self.ssSecLineEdit = QtWidgets.QLineEdit()
        introAnimeLabel = QtWidgets.QLabel("Intro Animation")
        addDataButton = QtWidgets.QPushButton("Add")
        self.ssCardlvlComboBox = QComboBox()
        self.ssCardlvlComboBox.addItem("Rare")
        self.ssCardlvlComboBox.addItem("Sr")
        self.ssCardlvlComboBox.addItem("SSR")
        self.singleSummonPageLayout = QVBoxLayout()
        isFeaturedLabel = QtWidgets.QLabel("Featured")
        cancelButton = QtWidgets.QPushButton("Cancel")
        self.ssIsFeaturedComboBox = QComboBox()
        self.ssIsFeaturedComboBox.addItem("Yes")
        self.ssIsFeaturedComboBox.addItem("No")
        dayLabel = QtWidgets.QLabel("Day: ")
        self.ssDayComboBox = QComboBox()
        self.ssDayComboBox.addItem("Sunday")
        self.ssDayComboBox.addItem("Monday")
        self.ssDayComboBox.addItem("Tuesday")
        self.ssDayComboBox.addItem("Wednesday")
        self.ssDayComboBox.addItem("Thursday")
        self.ssDayComboBox.addItem("Friday")
        self.ssDayComboBox.addItem("Saturday")

        hBoxLayout = QHBoxLayout()
        cardLvlLayout = QHBoxLayout()
        featuredLayout = QHBoxLayout()
        dayLayout = QHBoxLayout()
        #inserting the items into layout
        hBoxLayout.addWidget(timeLabel)
        hBoxLayout.addWidget(hrLabel)
        hBoxLayout.addWidget(self.ssHrLineEdit)
        hBoxLayout.addWidget(minLabel)
        hBoxLayout.addWidget(self.ssMinLineEdit)
        hBoxLayout.addWidget(secLabel)
        hBoxLayout.addWidget(self.ssSecLineEdit)
        hBoxLayout.addStretch()
        featuredLayout.addWidget(isFeaturedLabel)
        featuredLayout.addWidget(self.ssIsFeaturedComboBox)
        cardLvlLayout.addWidget(cardLvlLabel)
        cardLvlLayout.addWidget(self.ssCardlvlComboBox)
        cardLvlLayout.addStretch()
        dayLayout.addWidget(dayLabel)
        dayLayout.addWidget(self.ssDayComboBox)
        dayLayout.addStretch()
        self.singleSummonPageLayout.addWidget(self.ssSummonTypeList)
        self.ssSummonTypeList.setCurrentItem(self.ssSingleSummonItem)
        self.singleSummonPageLayout.addLayout(cardLvlLayout)
        self.singleSummonPageLayout.addLayout(featuredLayout)
        self.singleSummonPageLayout.addLayout(hBoxLayout)
        self.singleSummonPageLayout.addLayout(dayLayout)
        self.singleSummonPageLayout.addWidget(addDataButton)
        self.singleSummonPageLayout.addWidget(cancelButton)
        self.singleSummonPage.setLayout(self.singleSummonPageLayout)
        self.stackedLayout.addWidget(self.singleSummonPage)
        self.stackedLayout.setCurrentIndex(2)
        self.ssSummonTypeList.currentRowChanged.connect(self.displayLayout)
        #Adding Functions for Buttons
        addDataButton.clicked.connect(self.addSingleSummon)
        cancelButton.clicked.connect(self.viewHome)
        print("Layout still in Development")

    def printHello(self):
        print("Hello")

    def addSingleSummon(self):
        print("Adding Data . . .")
        dataString = "SS "
        if str(self.ssIsFeaturedComboBox.currentText()) == "Yes":
            dataString+= "Featured "
        else:
            dataString+="NotFeatured "
        dataString+= str(self.ssCardlvlComboBox.currentText())+" "
        dataString+=str(self.ssDayComboBox.currentText())+" "
        dataString = dataString + "Hr:" + self.ssHrLineEdit.text() + " Min:" + self.ssMinLineEdit.text() + " Sec:" + self.ssSecLineEdit.text()
        self.dSummons.insertSummonData(dataString+"\n")
        self.ssHrLineEdit.clear()
        self.ssMinLineEdit.clear()
        self.ssSecLineEdit.clear()
        self.ssCardlvlComboBox.setCurrentIndex(0)
        self.ssIsFeaturedComboBox.setCurrentIndex(0)
        self.ssDayComboBox.setCurrentIndex(0)
        print("Time: " + dataString)


    def addMultiSummon(self):
        print("Adding Data ...")
        print("Time: hr: " + self.msHrLineEdit.text())
        numFeatured = int(self.msIsFeaturedComboBox.currentText())
        numRare = int(self.msRarelvlComboBox.currentText())
        numSR = int(self.msSrlvlComboBox.currentText())
        numSSR = int(self.msSsrlvlComboBox.currentText())
        numSSR = numSSR - numFeatured
        for i in range(0,numFeatured):
            dataString = "MS "
            dataString+="Featured SSR "
            dataString+= str(self.msDayComboBox.currentText()) + " "
            dataString+= str("Hr:"+self.msHrLineEdit.text())+" "
            dataString+= str("Min:"+self.msMinLineEdit.text())+" "
            dataString+= str("Sec:"+self.msSecLineEdit.text())
            self.dSummons.insertSummonData(dataString+"\n")
        for i in range(0,numSSR):
            dataString = "MS "
            dataString+="NotFeatured SSR "
            dataString+= str(self.msDayComboBox.currentText()) + " "
            dataString+= str("Hr:"+self.msHrLineEdit.text())+" "
            dataString+= str("Min:"+self.msMinLineEdit.text())+" "
            dataString+= str("Sec:"+self.msSecLineEdit.text())
            self.dSummons.insertSummonData(dataString+"\n")
        for i in range(0,numFeatured):
            dataString = "MS "
            dataString+="NotFeatured Rare "
            dataString+= str(self.msDayComboBox.currentText()) + " "
            dataString+= str("Hr:"+self.msHrLineEdit.text())+" "
            dataString+= str("Min:"+self.msMinLineEdit.text())+" "
            dataString+= str("Sec:"+self.msSecLineEdit.text())
            print(dataString)
            self.dSummons.insertSummonData(dataString+"\n")
        for i in range(0,numFeatured):
            dataString = "MS "
            dataString+="NotFeatured Sr "
            dataString+= str(self.msDayComboBox.currentText()) + " "
            dataString+= str("Hr:"+self.msHrLineEdit.text())+" "
            dataString+= str("Min:"+self.msMinLineEdit.text())+" "
            dataString+= str("Sec:"+self.msSecLineEdit.text())
            self.dSummons.insertSummonData(dataString+"\n")
        self.msHrLineEdit.clear()
        self.msMinLineEdit.clear()
        self.msSecLineEdit.clear()
        self.msIsFeaturedComboBox.setCurrentIndex(0)
        self.msRarelvlComboBox.setCurrentIndex(0)
        self.msSrlvlComboBox.setCurrentIndex(0)
        self.msSsrlvlComboBox.setCurrentIndex(0)
        '''
        String Layout Featured Rarity Day Hr min sec
        '''

    def gssrSummonLayout(self):
        print("Layout still in Development")

    def displayLayout(self,index):
        print(index)
        if index == 1:
            self.multiSummonLayout()
            self.stackedLayout.setCurrentIndex(index+2)
        elif index == 0:
            #self.singleSummonLayout()
            self.stackedLayout.setCurrentIndex(index+2)
    def viewHome(self):
        self.stackedLayout.setCurrentIndex(0)

    def doubleRateSummonLayout(self):
        print("Layout still in Development")

    def customSummonLayout(self):
        print("Layout still in Development")

    def ticketSummonLayout(self):
        print("Layout still in Development")

app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())
