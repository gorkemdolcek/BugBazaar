import json
import re
import webbrowser
from PyQt5 import QtCore, QtGui, QtWidgets
import requests


class Ui_MainWindow(object):
    



    

####################################################################################################
    def gd_githubfunc(self):                                                                       #
        webbrowser.open('https://github.com/gorkemdolcek/')                                        #
                                                                                                   #
    def gd_linkedinfunc(self):                                                                     #
        webbrowser.open('https://www.linkedin.com/in/gorkemdolcek/')                               #
                                                                                                   #
    def gd_twitterfunc(self):                                                                      #
        webbrowser.open('https://twitter.com/mrdolcek')                                            #
####################################################################################################        

    def home_githubfunc(self):
        webbrowser.open('https://github.com/gorkemdolcek/BugBazaar/')



    def cvesearch_funcbutton(self): 
        cvesearch= self.search_text.toPlainText()
        print("Establishing a Connection, Please Wait...")
        url=str(f"https://cveawg.mitre.org/api/cve/{cvesearch}")
        try:
                response = requests.get(url)
        except:
                print("Cant get data. Check your connection.")
        json_data = json.loads(response.text)
        self.cveID_response.clear()
        self.cveID_response.insertPlainText(cvesearch)
        try:
                vulnerabilitytypes = json_data["containers"]["cna"]["problemTypes"][0]["descriptions"][0]["description"]
                self.vultype_response.clear()
                self.vultype_response.insertPlainText(vulnerabilitytypes)
        except:
                self.vultype_response.clear()
                self.vultype_response.insertPlainText("Vulnerability Type Data not found.")
        try:
                aciklama = json_data["containers"]["cna"]["descriptions"][0]["value"]
                self.cvedesc_response.clear()
                self.cvedesc_response.insertPlainText(aciklama)
        except:
                self.cvedesc_response.clear()
                self.cvedesc_response.insertPlainText("Description Data Not Found")
        try:
                etkilenencihazlar = json_data["containers"]["cna"]["affected"][0]["product"]
                self.affthings_response.clear()
                self.affthings_response.insertPlainText(etkilenencihazlar)
        except:
                self.affthings_response.clear()
                self.affthings_response.insertPlainText("Affected Devices Data Not Found")
        try:
                yayinlanmatarihi = json_data["containers"]["cna"]["datePublic"]
                self.date_response.clear()
                self.date_response.insertPlainText(yayinlanmatarihi)
        except:
                self.date_response.clear()
                self.date_response.insertPlainText("Data Not Found")

    def mostknowncves(self):
            url = 'https://plasticuproject.pythonanywhere.com/nvd-api/v1/recent'
            r = requests.get(url)
            text_satir = r.text.split(' ')  
            eslesme = []
            for match in text_satir:
                    if "CVE-" in match:
                            eslesme.append(match)  
            
            for dongu1, filter1 in enumerate(eslesme):
                    eslesme[dongu1] = filter1.replace('"', "")
            for dongu2, filter2 in enumerate(eslesme):
                    eslesme[dongu2] = filter2.replace("'", "")
            for dongu3, filter3 in enumerate(eslesme):
                    eslesme[dongu3] = filter3.replace(":", "")
            for dongu4, filter4 in enumerate(eslesme):
                    eslesme[dongu4] = filter4.replace(".", "")
            for dongu5, filter5 in enumerate(eslesme):
                    eslesme[dongu5] = filter5.replace("}", "")
            for dongu6, filter6 in enumerate(eslesme):
                    eslesme[dongu6] = filter6.replace("]", "")
            for dongu7, filter7 in enumerate(eslesme):
                    eslesme[dongu7] = filter7.replace(" ", "")
            for dongu8, filter8 in enumerate(eslesme):
                    eslesme[dongu8] = filter8.replace("[", "")
            for dongu9, filter9 in enumerate(eslesme):
                    eslesme[dongu9] = filter9.replace(",", "")
            global cvecodes
            cvecodes = []
            
            for i in eslesme:
                    result = re.sub(r'http\S+', '', i)
                    if len(result) != 0:
                            cvecodes.append(result)
            self.cveList_queryList.clear()
            

            for i in cvecodes:
                    self.cveList_queryList.addItem(i)
            self.cveList_queryList.clicked.connect(self.clicked)

    def clicked(self, qmodelindex): 
            global item
            item = self.cveList_queryList.currentItem()

    def clicked2(self): 
            url = str(f"https://cveawg.mitre.org/api/cve/{item.text()}")
            try:
                    response = requests.get(url)
            except:
                    print("Cant get data. Check your connection.")
            json_data = json.loads(response.text)
            self.cveList_cveID_response.clear()
            self.cveList_cveID_response.insertPlainText(item.text())
            try:
                    vulnerabilitytypes = json_data["containers"]["cna"]["problemTypes"][0]["descriptions"][0]["description"]
                    self.cveList_vultype_response.clear()
                    self.cveList_vultype_response.insertPlainText(vulnerabilitytypes)
            except:
                    self.cveList_vultype_response.clear()
                    self.cveList_vultype_response.insertPlainText("Vulnerability Type Data not found.")
            try:
                    aciklama = json_data["containers"]["cna"]["descriptions"][0]["value"]
                    self.cveList_cvedesc_response.clear()
                    self.cveList_cvedesc_response.insertPlainText(aciklama)
            except:
                    self.cveList_cvedesc_response.clear()
                    self.cveList_cvedesc_response.insertPlainText("Description Data Not Found")
            try:
                    etkilenencihazlar = json_data["containers"]["cna"]["affected"][0]["product"]
                    self.cveList_affdevices_response.clear()
                    self.cveList_affdevices_response.insertPlainText(etkilenencihazlar)
            except:
                    self.cveList_affdevices_response.clear()
                    self.cveList_affdevices_response.insertPlainText("Affected Devices Data Not Found")


    def cvespreading(self):  
        cvesearch = self.spreading_search_input.toPlainText()
        #bro who did that *-*
        print("Establishing a Connection, Please Wait...")
        url = str(f"https://cveawg.mitre.org/api/cve/{cvesearch}")
        font2 = QtGui.QFont()
        font2.setFamily("Lucida Console")
        font2.setPointSize(25)
        try:
                response = requests.get(url)
        except:
                print("Cant get data. Check your connection.")
        json_data = json.loads(response.text)
        try:
                etkilenencihazlar = json_data["containers"]["cna"]["affected"][0]["product"]
                self.CVESpread_ShodanIOPicture.clear()
                self.spreading_affdevices_response.clear()
                self.spreading_affdevices_response.insertPlainText(etkilenencihazlar)
                URL = str(f"https://www.shodan.io/search/facet.png?query={etkilenencihazlar}&facet=country")
                response = requests.get(URL)
                open("cihazlar.png", "wb").write(response.content)
                self.CVESpread_ShodanIOPicture.insertHtml('<img src="cihazlar.png" width="790" height="410">')
        except:
                self.spreading_affdevices_response.clear()
                self.spreading_affdevices_response.insertPlainText("Data Not Found")
        
            
    


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1450, 795)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")


        # Sol Sadece Logo Menüsü Başlangıç 
        self.icon_only_widget = QtWidgets.QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName("icon_only_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.icon_only_logo = QtWidgets.QHBoxLayout()
        self.icon_only_logo.setObjectName("icon_only_logo")
        self.logo = QtWidgets.QLabel(self.icon_only_widget)
        self.logo.setMinimumSize(QtCore.QSize(50, 50))
        self.logo.setMaximumSize(QtCore.QSize(50, 50))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/icon/icons/ladybug.ico"))
        self.logo.setScaledContents(True)
        self.logo.setWordWrap(False)
        self.logo.setObjectName("logo")
        self.icon_only_logo.addWidget(self.logo)
        self.verticalLayout_3.addLayout(self.icon_only_logo)
        self.icon_menu = QtWidgets.QVBoxLayout()
        self.icon_menu.setSpacing(0)
        self.icon_menu.setObjectName("icon_menu")
        self.home_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.home_btn_1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icons/home32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/icon/icons/home48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.home_btn_1.setIcon(icon)
        self.home_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.home_btn_1.setCheckable(True)
        self.home_btn_1.setAutoExclusive(True)
        self.home_btn_1.setObjectName("home_btn_1")
        self.icon_menu.addWidget(self.home_btn_1)
        self.cveSearch_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.cveSearch_btn_1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icons/search32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/icon/icons/search48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.cveSearch_btn_1.setIcon(icon1)
        self.cveSearch_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.cveSearch_btn_1.setCheckable(True)
        self.cveSearch_btn_1.setAutoExclusive(True)
        self.cveSearch_btn_1.setObjectName("cveSearch_btn_1")
        self.icon_menu.addWidget(self.cveSearch_btn_1)
        self.cveList_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.cveList_btn_1.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icons/list32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(":/icon/icons/list48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.cveList_btn_1.setIcon(icon2)
        self.cveList_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.cveList_btn_1.setCheckable(True)
        self.cveList_btn_1.setAutoExclusive(True)
        self.cveList_btn_1.setObjectName("cveList_btn_1")
        self.icon_menu.addWidget(self.cveList_btn_1)
        self.possibleSpreading_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.possibleSpreading_btn_1.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/icons/ssd32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap(":/icon/icons/ssd-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.possibleSpreading_btn_1.setIcon(icon3)
        self.possibleSpreading_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.possibleSpreading_btn_1.setCheckable(True)
        self.possibleSpreading_btn_1.setAutoExclusive(True)
        self.possibleSpreading_btn_1.setObjectName("possibleSpreading_btn_1")
        self.icon_menu.addWidget(self.possibleSpreading_btn_1)
        self.authors_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.authors_btn_1.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/icons/authors32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap(":/icon/icons/authors48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.authors_btn_1.setIcon(icon4)
        self.authors_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.authors_btn_1.setCheckable(True)
        self.authors_btn_1.setAutoExclusive(True)
        self.authors_btn_1.setObjectName("authors_btn_1")
        self.icon_menu.addWidget(self.authors_btn_1)
        self.verticalLayout_3.addLayout(self.icon_menu)
        spacerItem = QtWidgets.QSpacerItem(20, 375, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.exit_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.exit_btn_1.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/icons/close32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon5.addPixmap(QtGui.QPixmap(":/icon/icons/close48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.exit_btn_1.setIcon(icon5)
        self.exit_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.exit_btn_1.setObjectName("exit_btn_1")
        self.verticalLayout_3.addWidget(self.exit_btn_1)
        self.horizontalLayout.addWidget(self.icon_only_widget)
        self.full_menu_widget = QtWidgets.QWidget(self.centralwidget)

        #Sol Full Menü Ayarları Başlangıç
        self.full_menu_widget.setObjectName("full_menu_widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.full_menu_widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.full_menu_logo_isim = QtWidgets.QHBoxLayout()
        self.full_menu_logo_isim.setSpacing(0)
        self.full_menu_logo_isim.setObjectName("full_menu_logo_isim")
        self.full_menu_logo = QtWidgets.QLabel(self.full_menu_widget)
        self.full_menu_logo.setMinimumSize(QtCore.QSize(40, 40))
        self.full_menu_logo.setMaximumSize(QtCore.QSize(40, 40))
        self.full_menu_logo.setText("")
        self.full_menu_logo.setPixmap(QtGui.QPixmap(":/icon/icons/ladybug.ico"))
        self.full_menu_logo.setScaledContents(True)
        self.full_menu_logo.setObjectName("full_menu_logo")
        self.full_menu_logo_isim.addWidget(self.full_menu_logo)
        self.full_menu_isim = QtWidgets.QLabel(self.full_menu_widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.full_menu_isim.setFont(font)
        self.full_menu_isim.setObjectName("full_menu_isim")
        self.full_menu_logo_isim.addWidget(self.full_menu_isim)
        self.verticalLayout_4.addLayout(self.full_menu_logo_isim)
        self.full_menu = QtWidgets.QVBoxLayout()
        self.full_menu.setSpacing(0)
        self.full_menu.setObjectName("full_menu")
        self.home_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        self.home_btn_2.setIcon(icon)
        self.home_btn_2.setIconSize(QtCore.QSize(20, 20))
        self.home_btn_2.setCheckable(True)
        self.home_btn_2.setAutoExclusive(True)
        self.home_btn_2.setObjectName("home_btn_2")
        self.full_menu.addWidget(self.home_btn_2)
        self.cveSearch_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        self.cveSearch_btn_2.setIcon(icon1)
        self.cveSearch_btn_2.setIconSize(QtCore.QSize(20, 20))
        self.cveSearch_btn_2.setCheckable(True)
        self.cveSearch_btn_2.setAutoExclusive(True)
        self.cveSearch_btn_2.setObjectName("cveSearch_btn_2")
        self.full_menu.addWidget(self.cveSearch_btn_2)
        self.cveList_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        self.cveList_btn_2.setIcon(icon2)
        self.cveList_btn_2.setIconSize(QtCore.QSize(20, 20))
        self.cveList_btn_2.setCheckable(True)
        self.cveList_btn_2.setAutoExclusive(True)
        self.cveList_btn_2.setObjectName("cveList_btn_2")
        self.full_menu.addWidget(self.cveList_btn_2)
        self.possibleSpreading_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        self.possibleSpreading_btn_2.setIcon(icon3)
        self.possibleSpreading_btn_2.setIconSize(QtCore.QSize(20, 20))
        self.possibleSpreading_btn_2.setCheckable(True)
        self.possibleSpreading_btn_2.setAutoExclusive(True)
        self.possibleSpreading_btn_2.setObjectName("possibleSpreading_btn_2")
        self.full_menu.addWidget(self.possibleSpreading_btn_2)
        self.authors_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        self.authors_btn_2.setIcon(icon4)
        self.authors_btn_2.setIconSize(QtCore.QSize(20, 20))
        self.authors_btn_2.setCheckable(True)
        self.authors_btn_2.setAutoExclusive(True)
        self.authors_btn_2.setObjectName("authors_btn_2")
        self.full_menu.addWidget(self.authors_btn_2)
        self.verticalLayout_4.addLayout(self.full_menu)
        spacerItem1 = QtWidgets.QSpacerItem(20, 373, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.exit_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        self.exit_btn_2.setIcon(icon5)
        self.exit_btn_2.setIconSize(QtCore.QSize(20, 20))
        self.exit_btn_2.setObjectName("exit_btn_2")
        self.verticalLayout_4.addWidget(self.exit_btn_2)
        self.horizontalLayout.addWidget(self.full_menu_widget)


        #Sağ Menü Ayarları Başlangıç
        self.right_widget = QtWidgets.QWidget(self.centralwidget)
        self.right_widget.setObjectName("right_widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.right_widget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.menu_search_user_widget = QtWidgets.QWidget(self.right_widget)
        self.menu_search_user_widget.setMinimumSize(QtCore.QSize(0, 10))
        self.menu_search_user_widget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.menu_search_user_widget.setObjectName("menu_search_user_widget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.menu_search_user_widget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem2, 0, 1, 1, 1)
        self.menu_btn = QtWidgets.QPushButton(self.menu_search_user_widget) 
        self.menu_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.menu_btn.setMaximumSize(QtCore.QSize(30, 30))
        self.menu_btn.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icon/icons/menu32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon6.addPixmap(QtGui.QPixmap(":/icon/icons/menu48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.menu_btn.setIcon(icon6)
        self.menu_btn.setIconSize(QtCore.QSize(14, 14))
        self.menu_btn.setCheckable(True)
        self.menu_btn.setObjectName("menu_btn")
        self.gridLayout_6.addWidget(self.menu_btn, 0, 0, 1, 1)
        self.splitter = QtWidgets.QSplitter(self.menu_search_user_widget)
        self.splitter.setMouseTracking(False)
        self.splitter.setAcceptDrops(False)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setOpaqueResize(False)
        self.splitter.setHandleWidth(0)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.search_text = QtWidgets.QTextEdit(self.splitter)
        self.search_text.setMinimumSize(QtCore.QSize(0, 25))
        self.search_text.setMaximumSize(QtCore.QSize(16777215, 30))
        self.search_text.setSizeIncrement(QtCore.QSize(-24288, 0))
        self.search_text.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.search_text.setFont(font)
        self.search_text.setObjectName("search_text")
        self.search_btn = QtWidgets.QPushButton(self.splitter)
        self.search_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.search_btn.setMaximumSize(QtCore.QSize(60, 60))
        self.search_btn.setText("")
        self.search_btn.clicked.connect(self.cvesearch_funcbutton) # Arama butonuna tıkladığında cvesearch_funcbutton fonksiyonunu çalıştırır.
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icon/icons/search32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon7.addPixmap(QtGui.QPixmap(":/icon/icons/search48blue.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.search_btn.setIcon(icon7)
        self.search_btn.setObjectName("search_btn")
        self.gridLayout_6.addWidget(self.splitter, 0, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem3, 0, 3, 1, 1)
        self.verticalLayout_5.addWidget(self.menu_search_user_widget)

        # Sayfa Ayarları Başlangıç
        self.stackedWidget = QtWidgets.QStackedWidget(self.right_widget)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")

        #1.Sayfa Ayarları.
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 2, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem5, 4, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem6, 0, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem7, 2, 2, 1, 1)
        self.home_frame = QtWidgets.QFrame(self.page1)
        self.home_frame.setMinimumSize(QtCore.QSize(600, 100))
        self.home_frame.setMaximumSize(QtCore.QSize(10000, 10000))
        self.home_frame.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(49, 58, 70);\n"
"border-radius: 15px;")
        self.home_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.home_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.home_frame.setObjectName("home_frame")
        self.about_text = QtWidgets.QTextEdit(self.home_frame)
        self.about_text.setGeometry(QtCore.QRect(100, 140, 901, 111))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.about_text.setFont(font)
        self.about_text.setReadOnly(True)
        self.about_text.setObjectName("about_text")
        self.about = QtWidgets.QTextEdit(self.home_frame)
        self.about.setGeometry(QtCore.QRect(60, 60, 111, 71))
        self.about.setReadOnly(True)
        self.about.setObjectName("about")
        self.home_github_btn = QtWidgets.QPushButton(self.home_frame)
        self.home_github_btn.setGeometry(QtCore.QRect(200, 300, 91, 91))
        self.home_github_btn.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icon/icons/github32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon8.addPixmap(QtGui.QPixmap(":/icon/icons/github48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.home_github_btn.setIcon(icon8)
        self.home_github_btn.setIconSize(QtCore.QSize(32, 32))
        self.home_github_btn.setObjectName("home_github_btn")
        self.home_github_btn.clicked.connect(self.home_githubfunc)
        self.github_text = QtWidgets.QTextEdit(self.home_frame)
        self.github_text.setGeometry(QtCore.QRect(80, 320, 151, 91))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.github_text.setFont(font)
        self.github_text.setObjectName("github_text")
        self.about_text.raise_()
        self.about.raise_()
        self.github_text.raise_()
        self.home_github_btn.raise_()
        self.gridLayout_2.addWidget(self.home_frame, 2, 1, 1, 1)
        self.stackedWidget.addWidget(self.page1)

        #2.Sayfa Ayarları.
        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName("page2")
        self.gridLayout = QtWidgets.QGridLayout(self.page2)
        self.gridLayout.setObjectName("gridLayout")
        self.affthings_response_frame = QtWidgets.QFrame(self.page2)
        self.affthings_response_frame.setMinimumSize(QtCore.QSize(600, 100))
        self.affthings_response_frame.setMaximumSize(QtCore.QSize(600, 100))
        self.affthings_response_frame.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(49, 58, 70);\n"
"border-radius: 15px;")
        self.affthings_response_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.affthings_response_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.affthings_response_frame.setObjectName("affthings_response_frame")
        self.affthings_response = QtWidgets.QTextBrowser(self.affthings_response_frame)
        self.affthings_response.setGeometry(QtCore.QRect(10, 10, 581, 81))
        self.affthings_response.setObjectName("affthings_response")
        self.gridLayout.addWidget(self.affthings_response_frame, 4, 1, 1, 1)
        self.cveID_frame = QtWidgets.QFrame(self.page2)
        self.cveID_frame.setMaximumSize(QtCore.QSize(250, 100))
        self.cveID_frame.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(49, 58, 70);\n"
"border-radius: 15px;")
        self.cveID_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cveID_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cveID_frame.setObjectName("cveID_frame")
        self.cveID_text = QtWidgets.QTextBrowser(self.cveID_frame)
        self.cveID_text.setGeometry(QtCore.QRect(30, 30, 191, 41))
        self.cveID_text.setObjectName("cveID_text")
        self.gridLayout.addWidget(self.cveID_frame, 1, 0, 1, 1)
        self.cvedesc_frame = QtWidgets.QFrame(self.page2)
        self.cvedesc_frame.setMinimumSize(QtCore.QSize(250, 200))
        self.cvedesc_frame.setMaximumSize(QtCore.QSize(250, 200))
        self.cvedesc_frame.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(49, 58, 70);\n"
"border-radius: 15px;")
        self.cvedesc_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cvedesc_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cvedesc_frame.setObjectName("cvedesc_frame")
        self.cvedesc_text = QtWidgets.QTextBrowser(self.cvedesc_frame)
        self.cvedesc_text.setGeometry(QtCore.QRect(0, 50, 251, 81))
        self.cvedesc_text.setObjectName("cvedesc_text")
        self.gridLayout.addWidget(self.cvedesc_frame, 3, 0, 1, 1)
        self.vultype_frame = QtWidgets.QFrame(self.page2)
        self.vultype_frame.setMaximumSize(QtCore.QSize(250, 100))
        self.vultype_frame.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(49, 58, 70);\n"
"border-radius: 15px;")
        self.vultype_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.vultype_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.vultype_frame.setObjectName("vultype_frame")
        self.vultype_text = QtWidgets.QTextBrowser(self.vultype_frame)
        self.vultype_text.setGeometry(QtCore.QRect(10, 30, 231, 51))
        self.vultype_text.setObjectName("vultype_text")
        self.gridLayout.addWidget(self.vultype_frame, 2, 0, 1, 1)
        self.vultype_response_frame = QtWidgets.QFrame(self.page2)
        self.vultype_response_frame.setMinimumSize(QtCore.QSize(600, 100))
        self.vultype_response_frame.setMaximumSize(QtCore.QSize(600, 100))
        self.vultype_response_frame.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(49, 58, 70);\n"
"border-radius: 15px;")
        self.vultype_response_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.vultype_response_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.vultype_response_frame.setObjectName("vultype_response_frame")
        self.vultype_response = QtWidgets.QTextBrowser(self.vultype_response_frame)
        self.vultype_response.setGeometry(QtCore.QRect(10, 10, 581, 81))
        self.vultype_response.setStyleSheet("")
        self.vultype_response.setObjectName("vultype_response")
        self.gridLayout.addWidget(self.vultype_response_frame, 2, 1, 1, 1)
        self.affthings_frame = QtWidgets.QFrame(self.page2)
        self.affthings_frame.setMaximumSize(QtCore.QSize(250, 100))
        self.affthings_frame.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(49, 58, 70);\n"
"border-radius: 15px;")
        self.affthings_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.affthings_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.affthings_frame.setObjectName("affthings_frame")
        self.affthings_text = QtWidgets.QTextBrowser(self.affthings_frame)
        self.affthings_text.setGeometry(QtCore.QRect(0, 20, 241, 51))
        self.affthings_text.setObjectName("affthings_text")
        self.gridLayout.addWidget(self.affthings_frame, 4, 0, 1, 1)
        self.cvedesc_response_frame = QtWidgets.QFrame(self.page2)
        self.cvedesc_response_frame.setMaximumSize(QtCore.QSize(600, 200))
        self.cvedesc_response_frame.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(49, 58, 70);\n"
"border-radius: 15px;")
        self.cvedesc_response_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cvedesc_response_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cvedesc_response_frame.setObjectName("cvedesc_response_frame")
        self.cvedesc_response = QtWidgets.QTextBrowser(self.cvedesc_response_frame)
        self.cvedesc_response.setGeometry(QtCore.QRect(10, 10, 600, 181))
        self.cvedesc_response.setObjectName("cvedesc_response")
        self.gridLayout.addWidget(self.cvedesc_response_frame, 3, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem8, 0, 0, 1, 1)
        self.cveID_response_frame = QtWidgets.QFrame(self.page2)
        self.cveID_response_frame.setMinimumSize(QtCore.QSize(600, 100))
        self.cveID_response_frame.setMaximumSize(QtCore.QSize(600, 100))
        self.cveID_response_frame.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(49, 58, 70);\n"
"border-radius: 15px;")
        self.cveID_response_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cveID_response_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cveID_response_frame.setObjectName("cveID_response_frame")
        self.cveID_response = QtWidgets.QTextBrowser(self.cveID_response_frame)
        self.cveID_response.setGeometry(QtCore.QRect(10, 10, 581, 81))
        self.cveID_response.setObjectName("cveID_response")
        self.gridLayout.addWidget(self.cveID_response_frame, 1, 1, 1, 1)
        self.date_response_frame = QtWidgets.QFrame(self.page2)
        self.date_response_frame.setMaximumSize(QtCore.QSize(300, 50))
        self.date_response_frame.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(49, 58, 70);\n"
"border-radius: 15px;")
        self.date_response_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.date_response_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.date_response_frame.setObjectName("date_response_frame")
        self.date_response = QtWidgets.QTextBrowser(self.date_response_frame)
        self.date_response.setGeometry(QtCore.QRect(0, 0, 291, 51))
        self.date_response.setStyleSheet("")
        self.date_response.setObjectName("date_response")
        self.gridLayout.addWidget(self.date_response_frame, 5, 1, 1, 1)
        self.stackedWidget.addWidget(self.page2)

        self.page3 = QtWidgets.QWidget()
        self.page3.setObjectName("page3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.cveList_vultype_response_frame = QtWidgets.QFrame(self.page3)
        self.cveList_vultype_response_frame.setMinimumSize(QtCore.QSize(250, 100))
        self.cveList_vultype_response_frame.setMaximumSize(QtCore.QSize(600, 100))
        self.cveList_vultype_response_frame.setStyleSheet("\n"
"background-color: rgb(49, 58, 70);\n"
"border-radius: 15px;")
        self.cveList_vultype_response_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cveList_vultype_response_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cveList_vultype_response_frame.setObjectName("cveList_vultype_response_frame")
        self.cveList_vultype_response = QtWidgets.QTextBrowser(self.cveList_vultype_response_frame)
        self.cveList_vultype_response.setGeometry(QtCore.QRect(10, 10, 511, 81))
        self.cveList_vultype_response.setStyleSheet("color: rgb(255, 255, 255);")
        self.cveList_vultype_response.setObjectName("cveList_vultype_response")
        self.gridLayout_3.addWidget(self.cveList_vultype_response_frame, 3, 1, 1, 1)
        self.cveList_affdevices_response_frame = QtWidgets.QFrame(self.page3)
        self.cveList_affdevices_response_frame.setMinimumSize(QtCore.QSize(530, 100))
        self.cveList_affdevices_response_frame.setMaximumSize(QtCore.QSize(530, 100))
        self.cveList_affdevices_response_frame.setStyleSheet("\n"
"background-color: rgb(49, 58, 70);\n"
"border-radius: 15px;")
        self.cveList_affdevices_response_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cveList_affdevices_response_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cveList_affdevices_response_frame.setObjectName("cveList_affdevices_response_frame")
        self.cveList_affdevices_response = QtWidgets.QTextBrowser(self.cveList_affdevices_response_frame)
        self.cveList_affdevices_response.setGeometry(QtCore.QRect(10, 10, 511, 81))
        self.cveList_affdevices_response.setStyleSheet("color: rgb(255, 255, 255);")
        self.cveList_affdevices_response.setObjectName("cveList_affdevices_response")
        self.gridLayout_3.addWidget(self.cveList_affdevices_response_frame, 5, 1, 1, 1)
        self.cveList_cveID_response_frame = QtWidgets.QFrame(self.page3)
        self.cveList_cveID_response_frame.setMinimumSize(QtCore.QSize(250, 100))
        self.cveList_cveID_response_frame.setMaximumSize(QtCore.QSize(600, 100))
        self.cveList_cveID_response_frame.setStyleSheet("\n"
"background-color: rgb(49, 58, 70);\n"
"border-radius: 15px;")
        self.cveList_cveID_response_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cveList_cveID_response_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cveList_cveID_response_frame.setObjectName("cveList_cveID_response_frame")
        self.cveList_cveID_response = QtWidgets.QTextBrowser(self.cveList_cveID_response_frame)
        self.cveList_cveID_response.setGeometry(QtCore.QRect(10, 10, 511, 81))
        self.cveList_cveID_response.setStyleSheet("color: rgb(255, 255, 255)")
        self.cveList_cveID_response.setObjectName("cveList_cveID_response")
        self.gridLayout_3.addWidget(self.cveList_cveID_response_frame, 2, 1, 1, 1)
        self.cveList_affdevices_frame = QtWidgets.QFrame(self.page3)
        self.cveList_affdevices_frame.setMinimumSize(QtCore.QSize(250, 100))
        self.cveList_affdevices_frame.setMaximumSize(QtCore.QSize(250, 100))
        self.cveList_affdevices_frame.setStyleSheet("\n"
"background-color: rgb(49, 58, 70);\n"
"border-radius: 15px;")
        self.cveList_affdevices_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cveList_affdevices_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cveList_affdevices_frame.setObjectName("cveList_affdevices_frame")
        self.cveList_affdevices_text = QtWidgets.QTextBrowser(self.cveList_affdevices_frame)
        self.cveList_affdevices_text.setGeometry(QtCore.QRect(0, 30, 251, 41))
        self.cveList_affdevices_text.setStyleSheet("color: rgb(255, 255, 255);")
        self.cveList_affdevices_text.setObjectName("cveList_affdevices_text")
        self.gridLayout_3.addWidget(self.cveList_affdevices_frame, 5, 0, 1, 1)
        self.cveList_cvedesc_response_frame = QtWidgets.QFrame(self.page3)
        self.cveList_cvedesc_response_frame.setMinimumSize(QtCore.QSize(530, 150))
        self.cveList_cvedesc_response_frame.setMaximumSize(QtCore.QSize(550, 150))
        self.cveList_cvedesc_response_frame.setStyleSheet("\n"
"background-color: rgb(49, 58, 70);\n"
"border-radius: 15px;")
        self.cveList_cvedesc_response_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cveList_cvedesc_response_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cveList_cvedesc_response_frame.setObjectName("cveList_cvedesc_response_frame")
        self.cveList_cvedesc_response = QtWidgets.QTextBrowser(self.cveList_cvedesc_response_frame)
        self.cveList_cvedesc_response.setGeometry(QtCore.QRect(10, 10, 511, 131))
        self.cveList_cvedesc_response.setStyleSheet("color: rgb(255, 255, 255);")
        self.cveList_cvedesc_response.setObjectName("cveList_cvedesc_response")
        self.gridLayout_3.addWidget(self.cveList_cvedesc_response_frame, 4, 1, 1, 1)
        self.cveList_cveID_frame = QtWidgets.QFrame(self.page3)
        self.cveList_cveID_frame.setMinimumSize(QtCore.QSize(250, 100))
        self.cveList_cveID_frame.setMaximumSize(QtCore.QSize(250, 100))
        self.cveList_cveID_frame.setStyleSheet("\n"
"background-color: rgb(49, 58, 70);\n"
"border-radius: 15px;")
        self.cveList_cveID_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cveList_cveID_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cveList_cveID_frame.setObjectName("cveList_cveID_frame")
        self.cveList_cveID_2 = QtWidgets.QTextBrowser(self.cveList_cveID_frame)
        self.cveList_cveID_2.setGeometry(QtCore.QRect(0, 30, 251, 41))
        self.cveList_cveID_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.cveList_cveID_2.setObjectName("cveList_cveID_2")
        self.gridLayout_3.addWidget(self.cveList_cveID_frame, 2, 0, 1, 1)
        self.cveList_query_frame = QtWidgets.QFrame(self.page3)
        self.cveList_query_frame.setMinimumSize(QtCore.QSize(360, 670))
        self.cveList_query_frame.setMaximumSize(QtCore.QSize(360, 670))
        self.cveList_query_frame.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"\n"
"border-radius: 30px;")
        self.cveList_query_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cveList_query_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cveList_query_frame.setObjectName("cveList_query_frame")
        self.splitter_2 = QtWidgets.QSplitter(self.cveList_query_frame)
        self.splitter_2.setGeometry(QtCore.QRect(30, 40, 301, 596))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.cvelist_query = QtWidgets.QPushButton(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(170)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cvelist_query.sizePolicy().hasHeightForWidth())
        self.cvelist_query.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cvelist_query.setFont(font)
        self.cvelist_query.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(49, 58, 70);\n"
"border-radius: 15px;")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icon/icons/check48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon9.addPixmap(QtGui.QPixmap(":/icon/icons/check48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.cvelist_query.setIcon(icon9)
        self.cvelist_query.setIconSize(QtCore.QSize(32, 32))
        self.cvelist_query.setCheckable(True)
        self.cvelist_query.setAutoExclusive(True)
        self.cvelist_query.setObjectName("cvelist_query")
        self.cvelist_query.clicked.connect(self.clicked2) #Tıklandıgında clicked2 fonksiyonunu cagirioyr dikkat burda
        self.cveList_queryList = QtWidgets.QListWidget(self.splitter_2)
        self.cveList_queryList.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(49, 58, 70);\n"
"border-radius: 15px;")
        self.cveList_queryList.setObjectName("cveList_queryList")
        self.gridLayout_3.addWidget(self.cveList_query_frame, 1, 2, 5, 1)
        self.cveList_cvedesc_frame = QtWidgets.QFrame(self.page3)
        self.cveList_cvedesc_frame.setMinimumSize(QtCore.QSize(250, 150))
        self.cveList_cvedesc_frame.setMaximumSize(QtCore.QSize(250, 150))
        self.cveList_cvedesc_frame.setStyleSheet("\n"
"background-color: rgb(49, 58, 70);\n"
"border-radius: 15px;")
        self.cveList_cvedesc_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cveList_cvedesc_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cveList_cvedesc_frame.setObjectName("cveList_cvedesc_frame")
        self.cveList_cvedesc_text = QtWidgets.QTextBrowser(self.cveList_cvedesc_frame)
        self.cveList_cvedesc_text.setGeometry(QtCore.QRect(0, 60, 251, 61))
        self.cveList_cvedesc_text.setStyleSheet("color: rgb(255, 255, 255);")
        self.cveList_cvedesc_text.setObjectName("cveList_cvedesc_text")
        self.gridLayout_3.addWidget(self.cveList_cvedesc_frame, 4, 0, 1, 1)
        self.cveList_vultype_frame = QtWidgets.QFrame(self.page3)
        self.cveList_vultype_frame.setMinimumSize(QtCore.QSize(250, 100))
        self.cveList_vultype_frame.setMaximumSize(QtCore.QSize(250, 100))
        self.cveList_vultype_frame.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border-radius: 15px;")
        self.cveList_vultype_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cveList_vultype_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cveList_vultype_frame.setObjectName("cveList_vultype_frame")
        self.cveList_vultype_text = QtWidgets.QFrame(self.cveList_vultype_frame)
        self.cveList_vultype_text.setGeometry(QtCore.QRect(0, 0, 250, 100))
        self.cveList_vultype_text.setMinimumSize(QtCore.QSize(250, 100))
        self.cveList_vultype_text.setMaximumSize(QtCore.QSize(250, 100))
        self.cveList_vultype_text.setStyleSheet("\n"
"background-color: rgb(49, 58, 70);\n"
"border-radius: 15px;")
        self.cveList_vultype_text.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cveList_vultype_text.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cveList_vultype_text.setObjectName("cveList_vultype_text")
        self.cveID_text_3 = QtWidgets.QTextBrowser(self.cveList_vultype_text)
        self.cveID_text_3.setGeometry(QtCore.QRect(0, 30, 251, 61))
        self.cveID_text_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.cveID_text_3.setObjectName("cveID_text_3")
        self.gridLayout_3.addWidget(self.cveList_vultype_frame, 3, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem9, 0, 3, 1, 1)
        self.cveList_checkcves = QtWidgets.QPushButton(self.page3)
        self.cveList_checkcves.setMinimumSize(QtCore.QSize(250, 50))
        self.cveList_checkcves.setMaximumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.cveList_checkcves.setFont(font)
        self.cveList_checkcves.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(49, 58, 70);\n"
"border-radius: 15px;")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icon/icons/check32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon10.addPixmap(QtGui.QPixmap(":/icon/icons/check48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.cveList_checkcves.setIcon(icon10)
        self.cveList_checkcves.setIconSize(QtCore.QSize(32, 32))
        self.cveList_checkcves.setCheckable(True)
        self.cveList_checkcves.setChecked(True)
        self.cveList_checkcves.setAutoExclusive(True)
        self.cveList_checkcves.setObjectName("cveList_checkcves")
        self.cveList_checkcves.clicked.connect(self.mostknowncves) #Fonksiyon cagiriyor butona tikladiginda
        self.cveList_checkcves.clicked.connect(self.mostknowncves) #Fonksiyon cagiriyor butona tikladiginda
        self.gridLayout_3.addWidget(self.cveList_checkcves, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.page3)


        self.page4 = QtWidgets.QWidget()
        self.page4.setObjectName("page4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem10, 2, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem11, 2, 3, 1, 1)
        self.spreading_search_frame = QtWidgets.QFrame(self.page4)
        self.spreading_search_frame.setMinimumSize(QtCore.QSize(950, 60))
        self.spreading_search_frame.setMaximumSize(QtCore.QSize(950, 60))
        self.spreading_search_frame.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"border-radius: 15px;")
        self.spreading_search_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.spreading_search_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.spreading_search_frame.setObjectName("spreading_search_frame")
        self.splitter_3 = QtWidgets.QSplitter(self.spreading_search_frame)
        self.splitter_3.setGeometry(QtCore.QRect(30, 10, 901, 35))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.spreading_search_input = QtWidgets.QTextEdit(self.splitter_3)
        self.spreading_search_input.setMinimumSize(QtCore.QSize(700, 35))
        self.spreading_search_input.setMaximumSize(QtCore.QSize(700, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.spreading_search_input.setFont(font)
        self.spreading_search_input.setObjectName("spreading_search_input")
        self.spreading_search_btn = QtWidgets.QPushButton(self.splitter_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.spreading_search_btn.setFont(font)
        self.spreading_search_btn.setStyleSheet("\n"
"background-color: rgb(49, 58, 70);\n"
"border-radius: 15px;\n"
"color: rgb(255, 255, 255);")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icon/icons/search48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon11.addPixmap(QtGui.QPixmap(":/icon/icons/search32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.spreading_search_btn.setIcon(icon11)
        self.spreading_search_btn.setObjectName("spreading_search_btn")
        self.spreading_search_btn.clicked.connect(self.cvespreading)

        
        self.gridLayout_4.addWidget(self.spreading_search_frame, 0, 1, 1, 2)
        self.spreading_affdevices_frame = QtWidgets.QFrame(self.page4)
        self.spreading_affdevices_frame.setMinimumSize(QtCore.QSize(250, 60))
        self.spreading_affdevices_frame.setMaximumSize(QtCore.QSize(250, 60))
        self.spreading_affdevices_frame.setStyleSheet("\n"
"background-color: rgb(49, 58, 70);\n"
"border-radius: 15px;")
        self.spreading_affdevices_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.spreading_affdevices_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.spreading_affdevices_frame.setObjectName("spreading_affdevices_frame")

        self.spreading_affdevices_text = QtWidgets.QTextBrowser(self.spreading_affdevices_frame)
        self.spreading_affdevices_text.setGeometry(QtCore.QRect(0, 10, 251, 41))
        self.spreading_affdevices_text.setStyleSheet("color: rgb(255, 255, 255);")
        self.spreading_affdevices_text.setObjectName("spreading_affdevices_text")
        self.gridLayout_4.addWidget(self.spreading_affdevices_frame, 2, 1, 1, 1)
        self.spreading_affdevices_response_frame = QtWidgets.QFrame(self.page4)
        self.spreading_affdevices_response_frame.setMinimumSize(QtCore.QSize(690, 60))
        self.spreading_affdevices_response_frame.setMaximumSize(QtCore.QSize(690, 60))
        self.spreading_affdevices_response_frame.setStyleSheet("\n"
"background-color: rgb(49, 58, 70);\n"
"border-radius: 15px;")
        self.spreading_affdevices_response_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.spreading_affdevices_response_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.spreading_affdevices_response_frame.setObjectName("spreading_affdevices_response_frame")
        self.spreading_affdevices_response = QtWidgets.QTextBrowser(self.spreading_affdevices_response_frame)
        self.spreading_affdevices_response.setGeometry(QtCore.QRect(10, 10, 591, 41))
        self.spreading_affdevices_response.setObjectName("spreading_affdevices_response")
        self.gridLayout_4.addWidget(self.spreading_affdevices_response_frame, 2, 2, 1, 1)

        self.spreading_cveImage_frame = QtWidgets.QFrame(self.page4)
        self.spreading_cveImage_frame.setMinimumSize(QtCore.QSize(950, 370))
        self.spreading_cveImage_frame.setMaximumSize(QtCore.QSize(950, 370))
        self.spreading_cveImage_frame.setStyleSheet("background-color: rgb(49, 58, 70);\n"
"border-radius: 15px;")
        self.spreading_cveImage_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.spreading_cveImage_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.spreading_cveImage_frame.setObjectName("spreading_cveImage_frame")



        self.CVESpread_ShodanIOPicture = QtWidgets.QTextBrowser(self.spreading_cveImage_frame)
        self.CVESpread_ShodanIOPicture.setMinimumSize(QtCore.QSize(950, 370))
        self.CVESpread_ShodanIOPicture.setMaximumSize(QtCore.QSize(950, 370))
        self.CVESpread_ShodanIOPicture.setStyleSheet("background-color: rgb(49, 58, 70);\n"
"border-radius: 15px;")

        self.gridLayout_4.addWidget(self.spreading_cveImage_frame, 1, 1, 1, 2)
        self.stackedWidget.addWidget(self.page4)

        self.spreading_cveImage_frame.raise_()
        self.spreading_search_frame.raise_()
        self.spreading_affdevices_frame.raise_()
        self.spreading_affdevices_response_frame.raise_()
        self.CVESpread_ShodanIOPicture.raise_()


        self.page5 = QtWidgets.QWidget()
        self.page5.setObjectName("page5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.mehmetdemir_frame = QtWidgets.QFrame(self.page5)
        self.mehmetdemir_frame.setMinimumSize(QtCore.QSize(600, 60))
        self.mehmetdemir_frame.setMaximumSize(QtCore.QSize(600, 60))
        self.mehmetdemir_frame.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(49, 58, 70);\n"
"border-radius: 15px;")
        self.mehmetdemir_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mehmetdemir_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mehmetdemir_frame.setObjectName("mehmetdemir_frame")
        self.mehmetdemir_text = QtWidgets.QTextBrowser(self.mehmetdemir_frame)
        self.mehmetdemir_text.setGeometry(QtCore.QRect(0, 10, 601, 41))
        self.mehmetdemir_text.setObjectName("mehmetdemir_text")
        self.gridLayout_5.addWidget(self.mehmetdemir_frame, 2, 1, 1, 1)
        self.authors_frame = QtWidgets.QFrame(self.page5)
        self.authors_frame.setMinimumSize(QtCore.QSize(270, 60))
        self.authors_frame.setMaximumSize(QtCore.QSize(270, 60))
        self.authors_frame.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(49, 58, 70);\n"
"border-radius: 15px;")
        self.authors_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.authors_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.authors_frame.setObjectName("authors_frame")
        self.authors_text = QtWidgets.QTextBrowser(self.authors_frame)
        self.authors_text.setGeometry(QtCore.QRect(0, 10, 271, 41))
        self.authors_text.setObjectName("authors_text")
        self.gridLayout_5.addWidget(self.authors_frame, 0, 1, 1, 1)
        self.dilarasenturk_frame = QtWidgets.QFrame(self.page5)
        self.dilarasenturk_frame.setMinimumSize(QtCore.QSize(600, 60))
        self.dilarasenturk_frame.setMaximumSize(QtCore.QSize(600, 60))
        self.dilarasenturk_frame.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(49, 58, 70);\n"
"border-radius: 15px;")
        self.dilarasenturk_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dilarasenturk_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dilarasenturk_frame.setObjectName("dilarasenturk_frame")
        self.dilarasenturk_text = QtWidgets.QTextBrowser(self.dilarasenturk_frame)
        self.dilarasenturk_text.setGeometry(QtCore.QRect(0, 10, 601, 41))
        self.dilarasenturk_text.setObjectName("dilarasenturk_text")
        self.gridLayout_5.addWidget(self.dilarasenturk_frame, 3, 1, 1, 1)
        self.azatdolunay_frame = QtWidgets.QFrame(self.page5)
        self.azatdolunay_frame.setMinimumSize(QtCore.QSize(600, 60))
        self.azatdolunay_frame.setMaximumSize(QtCore.QSize(600, 60))
        self.azatdolunay_frame.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(49, 58, 70);\n"
"border-radius: 15px;")
        self.azatdolunay_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.azatdolunay_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.azatdolunay_frame.setObjectName("azatdolunay_frame")
        self.azatdolunay_frame_2 = QtWidgets.QTextBrowser(self.azatdolunay_frame)
        self.azatdolunay_frame_2.setGeometry(QtCore.QRect(0, 10, 601, 41))
        self.azatdolunay_frame_2.setObjectName("azatdolunay_frame_2")
        self.gridLayout_5.addWidget(self.azatdolunay_frame, 5, 1, 1, 1)
        self.talhacayli_frame = QtWidgets.QFrame(self.page5)
        self.talhacayli_frame.setMinimumSize(QtCore.QSize(600, 60))
        self.talhacayli_frame.setMaximumSize(QtCore.QSize(600, 60))
        self.talhacayli_frame.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(49, 58, 70);\n"
"border-radius: 15px;")
        self.talhacayli_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.talhacayli_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.talhacayli_frame.setObjectName("talhacayli_frame")
        self.talhacayli_text = QtWidgets.QTextBrowser(self.talhacayli_frame)
        self.talhacayli_text.setGeometry(QtCore.QRect(0, 10, 601, 41))
        self.talhacayli_text.setObjectName("talhacayli_text")
        self.gridLayout_5.addWidget(self.talhacayli_frame, 4, 1, 1, 1)
        self.gorkemdolcek_frame = QtWidgets.QFrame(self.page5)
        self.gorkemdolcek_frame.setMinimumSize(QtCore.QSize(600, 60))
        self.gorkemdolcek_frame.setMaximumSize(QtCore.QSize(600, 60))
        self.gorkemdolcek_frame.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(49, 58, 70);\n"
"border-radius: 15px;")
        self.gorkemdolcek_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gorkemdolcek_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gorkemdolcek_frame.setObjectName("gorkemdolcek_frame")
        self.gorkemdolcek_text = QtWidgets.QTextBrowser(self.gorkemdolcek_frame)
        self.gorkemdolcek_text.setGeometry(QtCore.QRect(0, 10, 581, 41))
        self.gorkemdolcek_text.setObjectName("gorkemdolcek_text")
        self.gridLayout_5.addWidget(self.gorkemdolcek_frame, 1, 1, 1, 1)
        self.ds_twitter_btn = QtWidgets.QPushButton(self.page5)
        self.ds_twitter_btn.setMinimumSize(QtCore.QSize(60, 60))
        self.ds_twitter_btn.setMaximumSize(QtCore.QSize(60, 60))
        self.ds_twitter_btn.setStyleSheet("background-color: rgb(49, 58, 70);\n"
"border-radius: 15px;")
        self.ds_twitter_btn.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icon/icons/twitter32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon12.addPixmap(QtGui.QPixmap(":/icon/icons/twitter48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.ds_twitter_btn.setIcon(icon12)
        self.ds_twitter_btn.setIconSize(QtCore.QSize(32, 32))
        self.ds_twitter_btn.setObjectName("ds_twitter_btn")
        self.gridLayout_5.addWidget(self.ds_twitter_btn, 3, 4, 1, 1)
        self.gd_twitter_btn = QtWidgets.QPushButton(self.page5)
        self.gd_twitter_btn.setMinimumSize(QtCore.QSize(60, 60))
        self.gd_twitter_btn.setMaximumSize(QtCore.QSize(60, 60))
        self.gd_twitter_btn.setStyleSheet("background-color: rgb(49, 58, 70);\n"
"border-radius: 15px;")
        self.gd_twitter_btn.setCheckable(True)
        self.gd_twitter_btn.setText("")
        self.gd_twitter_btn.setIcon(icon12)
        self.gd_twitter_btn.setIconSize(QtCore.QSize(32, 32))
        self.gd_twitter_btn.setObjectName("gd_twitter_btn")
        self.gd_twitter_btn.clicked.connect(self.gd_twitterfunc) #Görkem Dolcek Github logosuna tıklandığında githubfunc fonksiyonunu çalıştırır.
        self.gridLayout_5.addWidget(self.gd_twitter_btn, 1, 4, 1, 1)
        self.tc_github_btn = QtWidgets.QPushButton(self.page5)
        self.tc_github_btn.setMinimumSize(QtCore.QSize(60, 60))
        self.tc_github_btn.setMaximumSize(QtCore.QSize(60, 60))
        self.tc_github_btn.setStyleSheet("background-color: rgb(49, 58, 70);\n"
"border-radius: 15px;")
        self.tc_github_btn.setText("")
        self.tc_github_btn.setIcon(icon8)
        self.tc_github_btn.setIconSize(QtCore.QSize(32, 32))
        self.tc_github_btn.setCheckable(True)
        self.tc_github_btn.setAutoExclusive(True)
        self.tc_github_btn.setObjectName("tc_github_btn")
        self.gridLayout_5.addWidget(self.tc_github_btn, 4, 2, 1, 1)
        self.md_linkedin_btn = QtWidgets.QPushButton(self.page5)
        self.md_linkedin_btn.setMinimumSize(QtCore.QSize(60, 60))
        self.md_linkedin_btn.setMaximumSize(QtCore.QSize(60, 60))
        self.md_linkedin_btn.setStyleSheet("background-color: rgb(49, 58, 70);\n"
"border-radius: 15px;")
        self.md_linkedin_btn.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icon/icons/linkedin32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon13.addPixmap(QtGui.QPixmap(":/icon/icons/linkedin48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.md_linkedin_btn.setIcon(icon13)
        self.md_linkedin_btn.setIconSize(QtCore.QSize(32, 32))
        self.md_linkedin_btn.setObjectName("md_linkedin_btn")
        self.gridLayout_5.addWidget(self.md_linkedin_btn, 2, 3, 1, 1)
        self.ds_linkedin_btn = QtWidgets.QPushButton(self.page5)
        self.ds_linkedin_btn.setMinimumSize(QtCore.QSize(60, 60))
        self.ds_linkedin_btn.setMaximumSize(QtCore.QSize(60, 60))
        self.ds_linkedin_btn.setStyleSheet("background-color: rgb(49, 58, 70);\n"
"border-radius: 15px;")
        self.ds_linkedin_btn.setText("")
        self.ds_linkedin_btn.setIcon(icon13)
        self.ds_linkedin_btn.setIconSize(QtCore.QSize(32, 32))
        self.ds_linkedin_btn.setObjectName("ds_linkedin_btn")
        self.gridLayout_5.addWidget(self.ds_linkedin_btn, 3, 3, 1, 1)
        self.md_twitter_btn = QtWidgets.QPushButton(self.page5)
        self.md_twitter_btn.setMinimumSize(QtCore.QSize(60, 60))
        self.md_twitter_btn.setMaximumSize(QtCore.QSize(60, 60))
        self.md_twitter_btn.setStyleSheet("background-color: rgb(49, 58, 70);\n"
"border-radius: 15px;")
        self.md_twitter_btn.setText("")
        self.md_twitter_btn.setIcon(icon12)
        self.md_twitter_btn.setIconSize(QtCore.QSize(32, 32))
        self.md_twitter_btn.setObjectName("md_twitter_btn")
        self.gridLayout_5.addWidget(self.md_twitter_btn, 2, 4, 1, 1)
        self.md_github_btn = QtWidgets.QPushButton(self.page5)
        self.md_github_btn.setMinimumSize(QtCore.QSize(60, 60))
        self.md_github_btn.setMaximumSize(QtCore.QSize(60, 60))
        self.md_github_btn.setStyleSheet("background-color: rgb(49, 58, 70);\n"
"border-radius: 15px;")
        self.md_github_btn.setText("")
        self.md_github_btn.setIcon(icon8)
        self.md_github_btn.setIconSize(QtCore.QSize(32, 32))
        self.md_github_btn.setCheckable(True)
        self.md_github_btn.setAutoExclusive(True)
        self.md_github_btn.setObjectName("md_github_btn")
        self.gridLayout_5.addWidget(self.md_github_btn, 2, 2, 1, 1)
        self.tc_twitter_btn = QtWidgets.QPushButton(self.page5)
        self.tc_twitter_btn.setMinimumSize(QtCore.QSize(60, 60))
        self.tc_twitter_btn.setMaximumSize(QtCore.QSize(60, 60))
        self.tc_twitter_btn.setStyleSheet("background-color: rgb(49, 58, 70);\n"
"border-radius: 15px;")
        self.tc_twitter_btn.setText("")
        self.tc_twitter_btn.setIcon(icon12)
        self.tc_twitter_btn.setIconSize(QtCore.QSize(32, 32))
        self.tc_twitter_btn.setObjectName("tc_twitter_btn")
        self.gridLayout_5.addWidget(self.tc_twitter_btn, 4, 4, 1, 1)
        self.ds_github_btn = QtWidgets.QPushButton(self.page5)
        self.ds_github_btn.setMinimumSize(QtCore.QSize(60, 60))
        self.ds_github_btn.setMaximumSize(QtCore.QSize(60, 60))
        self.ds_github_btn.setStyleSheet("background-color: rgb(49, 58, 70);\n"
"border-radius: 15px;")
        self.ds_github_btn.setText("")
        self.ds_github_btn.setIcon(icon8)
        self.ds_github_btn.setIconSize(QtCore.QSize(32, 32))
        self.ds_github_btn.setCheckable(True)
        self.ds_github_btn.setAutoExclusive(True)
        self.ds_github_btn.setObjectName("ds_github_btn")
        self.gridLayout_5.addWidget(self.ds_github_btn, 3, 2, 1, 1)
        self.tc_linkedin_btn = QtWidgets.QPushButton(self.page5)
        self.tc_linkedin_btn.setMinimumSize(QtCore.QSize(60, 60))
        self.tc_linkedin_btn.setMaximumSize(QtCore.QSize(60, 60))
        self.tc_linkedin_btn.setStyleSheet("background-color: rgb(49, 58, 70);\n"
"border-radius: 15px;")
        self.tc_linkedin_btn.setText("")
        self.tc_linkedin_btn.setIcon(icon13)
        self.tc_linkedin_btn.setIconSize(QtCore.QSize(32, 32))
        self.tc_linkedin_btn.setObjectName("tc_linkedin_btn")
        self.gridLayout_5.addWidget(self.tc_linkedin_btn, 4, 3, 1, 1)
        self.ad_twitter_btn = QtWidgets.QPushButton(self.page5)
        self.ad_twitter_btn.setMinimumSize(QtCore.QSize(60, 60))
        self.ad_twitter_btn.setMaximumSize(QtCore.QSize(60, 60))
        self.ad_twitter_btn.setStyleSheet("background-color: rgb(49, 58, 70);\n"
"border-radius: 15px;")
        self.ad_twitter_btn.setText("")
        self.ad_twitter_btn.setIcon(icon12)
        self.ad_twitter_btn.setIconSize(QtCore.QSize(32, 32))
        self.ad_twitter_btn.setObjectName("ad_twitter_btn")
        self.gridLayout_5.addWidget(self.ad_twitter_btn, 5, 4, 1, 1)
        self.ad_github_btn = QtWidgets.QPushButton(self.page5)
        self.ad_github_btn.setMinimumSize(QtCore.QSize(60, 60))
        self.ad_github_btn.setMaximumSize(QtCore.QSize(60, 60))
        self.ad_github_btn.setStyleSheet("background-color: rgb(49, 58, 70);\n"
"border-radius: 15px;")
        self.ad_github_btn.setText("")
        self.ad_github_btn.setIcon(icon8)
        self.ad_github_btn.setIconSize(QtCore.QSize(32, 32))
        self.ad_github_btn.setCheckable(True)
        self.ad_github_btn.setAutoExclusive(True)
        self.ad_github_btn.setObjectName("ad_github_btn")
        self.gridLayout_5.addWidget(self.ad_github_btn, 5, 2, 1, 1)
        self.ad_linkedin_btn = QtWidgets.QPushButton(self.page5)
        self.ad_linkedin_btn.setMinimumSize(QtCore.QSize(60, 60))
        self.ad_linkedin_btn.setMaximumSize(QtCore.QSize(60, 60))
        self.ad_linkedin_btn.setStyleSheet("background-color: rgb(49, 58, 70);\n"
"border-radius: 15px;")
        self.ad_linkedin_btn.setText("")
        self.ad_linkedin_btn.setIcon(icon13)
        self.ad_linkedin_btn.setIconSize(QtCore.QSize(32, 32))
        self.ad_linkedin_btn.setObjectName("ad_linkedin_btn")
        self.gridLayout_5.addWidget(self.ad_linkedin_btn, 5, 3, 1, 1)
        self.gd_linkedin_btn = QtWidgets.QPushButton(self.page5)
        self.gd_linkedin_btn.setMinimumSize(QtCore.QSize(60, 60))
        self.gd_linkedin_btn.setMaximumSize(QtCore.QSize(60, 60))
        self.gd_linkedin_btn.setStyleSheet("background-color: rgb(49, 58, 70);\n"
"border-radius: 15px;")
        self.gd_linkedin_btn.setCheckable(True)
        self.gd_linkedin_btn.setText("")
        self.gd_linkedin_btn.setIcon(icon13)
        self.gd_linkedin_btn.setIconSize(QtCore.QSize(32, 32))
        self.gd_linkedin_btn.setObjectName("gd_linkedin_btn")
        self.gd_linkedin_btn.clicked.connect(self.gd_linkedinfunc) #Görkem Dolcek Github logosuna tıklandığında githubfunc fonksiyonunu çalıştırır.

        self.gridLayout_5.addWidget(self.gd_linkedin_btn, 1, 3, 1, 1)

        self.gd_github_btn = QtWidgets.QPushButton(self.page5)
        self.gd_github_btn.setMinimumSize(QtCore.QSize(60, 60))
        self.gd_github_btn.setMaximumSize(QtCore.QSize(60, 60))
        self.gd_github_btn.setStyleSheet("background-color: rgb(49, 58, 70);\n"
"border-radius: 15px;")
        self.gd_github_btn.setText("")
        self.gd_github_btn.setIcon(icon8)
        self.gd_github_btn.setIconSize(QtCore.QSize(32, 32))
        self.gd_github_btn.setCheckable(True)
        self.gd_github_btn.setObjectName("gd_github_btn")
        self.gd_github_btn.clicked.connect(self.gd_githubfunc) #Görkem Dolcek Github logosuna tıklandığında githubfunc fonksiyonunu çalıştırır.

        self.gridLayout_5.addWidget(self.gd_github_btn, 1, 2, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem12, 2, 5, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem13, 2, 0, 1, 1)
        self.stackedWidget.addWidget(self.page5)
        self.page6 = QtWidgets.QWidget()
        self.page6.setObjectName("page6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.page6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.search_label = QtWidgets.QLabel(self.page6)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.search_label.setFont(font)
        self.search_label.setScaledContents(True)
        self.search_label.setAlignment(QtCore.Qt.AlignCenter)
        self.search_label.setObjectName("search_label")
        self.gridLayout_7.addWidget(self.search_label, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page6)
        self.page7 = QtWidgets.QWidget()
        self.page7.setObjectName("page7")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.page7)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.stackedWidget.addWidget(self.page7)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.horizontalLayout.addWidget(self.right_widget)
        MainWindow.setCentralWidget(self.centralwidget)



        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(3)
        self.exit_btn_1.clicked.connect(MainWindow.close) # type: ignore
        self.menu_btn.toggled['bool'].connect(self.icon_only_widget.setVisible) # type: ignore
        self.cveSearch_btn_2.toggled['bool'].connect(self.cveSearch_btn_1.setChecked) # type: ignore
        self.home_btn_1.toggled['bool'].connect(self.home_btn_2.setChecked) # type: ignore
        self.exit_btn_2.clicked.connect(MainWindow.close) # type: ignore
        self.possibleSpreading_btn_2.toggled['bool'].connect(self.possibleSpreading_btn_1.setChecked) # type: ignore
        self.authors_btn_2.toggled['bool'].connect(self.authors_btn_1.setChecked) # type: ignore
        self.cveList_btn_2.toggled['bool'].connect(self.cveList_btn_1.setChecked) # type: ignore
        self.possibleSpreading_btn_1.toggled['bool'].connect(self.possibleSpreading_btn_2.setChecked) # type: ignore
        self.home_btn_2.toggled['bool'].connect(self.home_btn_1.setChecked) # type: ignore
        self.cveList_btn_1.toggled['bool'].connect(self.cveList_btn_2.setChecked) # type: ignore
        self.cveSearch_btn_1.toggled['bool'].connect(self.cveSearch_btn_2.setChecked) # type: ignore
        self.authors_btn_1.toggled['bool'].connect(self.authors_btn_2.setChecked) # type: ignore
        self.menu_btn.toggled['bool'].connect(self.full_menu_widget.setHidden) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.full_menu_isim.setText(_translate("MainWindow", "BugBazaar"))
        self.home_btn_2.setText(_translate("MainWindow", "Home"))
        self.cveSearch_btn_2.setText(_translate("MainWindow", "CVE Search"))
        self.cveList_btn_2.setText(_translate("MainWindow", "CVE List"))
        self.possibleSpreading_btn_2.setText(_translate("MainWindow", "Possible Spreading"))
        self.authors_btn_2.setText(_translate("MainWindow", "Authors"))
        self.exit_btn_2.setText(_translate("MainWindow", "Exit"))
        self.about_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#ffffff;\">An application that finds current security vulnerabilities and list them with a graphical interface. It also shows which countries a vulnerability cloud most affect.</span></p></body></html>"))
        self.about.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">About:</span></p></body></html>"))
        self.github_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; font-weight:600; color:#ffffff;\">Github:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:22pt; font-weight:600; color:#ffffff;\"><br /></p></body></html>"))
        self.affthings_response.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.cveID_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">CVE ID:</span></p></body></html>"))
        self.cvedesc_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">CVE Description:</span></p></body></html>"))
        self.vultype_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">Vulnerability Type:</span></p></body></html>"))
        self.vultype_response.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.affthings_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; font-style:italic;\">Affected Things:</span></p></body></html>"))
        self.cvedesc_response.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.cveID_response.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.date_response.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.cveList_vultype_response.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.cveList_affdevices_response.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.cveList_cveID_response.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.cveList_affdevices_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; font-style:italic; color:#ffffff;\">Affected Devices:</span></p></body></html>"))
        self.cveList_cvedesc_response.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.cveList_cveID_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">CVE ID:</span></p></body></html>"))
        self.cvelist_query.setText(_translate("MainWindow", "Query"))
        self.cveList_cvedesc_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">CVE Description:</span></p></body></html>"))
        self.cveID_text_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">Vulnerability Type:</span></p></body></html>"))
        self.cveList_checkcves.setText(_translate("MainWindow", "Check Up-to-date CVE\'s"))
        self.spreading_search_btn.setText(_translate("MainWindow", "Search"))
        self.spreading_affdevices_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; font-style:italic;\">Affected Devices:</span></p></body></html>"))
        self.spreading_affdevices_response.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.mehmetdemir_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; font-style:italic;\">2. Mehmet Demir</span></p></body></html>"))
        self.authors_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">Authors:</span></p></body></html>"))
        self.dilarasenturk_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; font-style:italic;\">3. Dilara Şentürk</span></p></body></html>"))
        self.azatdolunay_frame_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; font-style:italic;\">5. Azat Dolunay</span></p></body></html>"))
        self.talhacayli_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; font-style:italic;\">4. Talha Çaylı</span></p></body></html>"))
        self.gorkemdolcek_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; font-style:italic;\">1. Görkem Dolcek</span></p></body></html>"))
        self.search_label.setText(_translate("MainWindow", "Serach Page"))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
