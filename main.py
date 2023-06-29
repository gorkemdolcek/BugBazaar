#from PyQt5 import QtCore, QtGui, QtWidgets
#import requests
#import webbrowser
try:
    import urllib
    import json
    import re
    import webbrowser
    try:
        import requests
        #import webbrowser
        from PyQt5 import QtCore, QtGui, QtWidgets
    except ImportError:
        import os
        print('Requirements isn\'t installed, installing now.')
        ret_code = os.system('pip3 install -r requirements.txt')
        if(ret_code != 0):
            print('Requests installation failed.')
            quit()
        print('Requests has been installed, restart me:3')
        quit()
except ImportError:
    print('BugBazaar isn\'t compatible with python2. Use python > 3.4 to run BugBazaar.')
    quit()


class Ui_Dialog(object):

    def githubfunc(self): #logoya basınca github reposuna yonlendir
        webbrowser.open('https://github.com/jackalkarlos/BugBazaar')

    def cvesearch_funcbutton(self):
        cvesearch= self.CVESearch_SearchBar.toPlainText()
        print("Establishing a Connection, Please Wait...")
        url=str(f"https://cveawg.mitre.org/api/cve/{cvesearch}")
        try:
                response = requests.get(url)
        except:
                print("Cant get data. Check your connection.")
        #alınan ham http datasını kolay kullanım için jsona dönüştürülmesi
        json_data = json.loads(response.text)
        #olan verinin bulunmaması halinde kodun çökmemesi için try except döngüleri.
        self.Search_CVE_ID.clear()
        self.Search_CVE_ID.insertPlainText(cvesearch)
        try:
                vulnerabilitytypes = json_data["containers"]["cna"]["problemTypes"][0]["descriptions"][0]["description"]
                self.Search_Vulnerability_Type.clear()
                self.Search_Vulnerability_Type.insertPlainText(vulnerabilitytypes)
        except:
                self.Search_Vulnerability_Type.clear()
                self.Search_Vulnerability_Type.insertPlainText("Vulnerability Type Data not found.")
        try:
                aciklama = json_data["containers"]["cna"]["descriptions"][0]["value"]
                self.Search_CVE_Description.clear()
                self.Search_CVE_Description.insertPlainText(aciklama)
        except:
                self.Search_CVE_Description.clear()
                self.Search_CVE_Description.insertPlainText("Description Data Not Found")
        try:
                etkilenencihazlar = json_data["containers"]["cna"]["affected"][0]["product"]
                self.Search_CVEAffectedThings.clear()
                self.Search_CVEAffectedThings.insertPlainText(etkilenencihazlar)
        except:
                self.Search_CVEAffectedThings.clear()
                self.Search_CVEAffectedThings.insertPlainText("Affected Devices Data Not Found")
        try:
                yayinlanmatarihi = json_data["containers"]["cna"]["datePublic"]
                self.Search_PublishTime.clear()
                self.Search_PublishTime.insertPlainText(yayinlanmatarihi)
        except:
                self.Search_PublishTime.clear()
                self.Search_PublishTime.insertPlainText("Data Not Found")

    def mostknowncves(self):
            #print("this function working, so dont worry bro.") lutfen bu satiri silelim arkdslr...
            url = 'https://plasticuproject.pythonanywhere.com/nvd-api/v1/recent'
            r = requests.get(url)
            text_satir = r.text.split(' ')  # Çıktıyı satırlara böler
            eslesme = []
            for match in text_satir:
                    if "CVE-" in match:
                            eslesme.append(match)  # İçinde CVE olan elemanları "eslesme" listesine ekle
            # "eslesme" içerisindeki gereksiz harflerin filtrelenmesini sağlar.
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
            # http ve https linklerini sil, ayrıca boş çıktıları da sil ve outputa ekle
            for i in eslesme:
                    result = re.sub(r'http\S+', '', i)
                    if len(result) != 0:
                            cvecodes.append(result)
            self.UpToDate_List.clear()
            #self.UpToDate_List.addItem(cvecodes)

            for i in cvecodes:
                    self.UpToDate_List.addItem(i)
            #for linenumber, cvelist in zip(range(50), cvecodes): bro who did that:D
            #        self.UpToDate_list.insertItem(linenumber + ", " + str(cvelist))
            self.UpToDate_List.clicked.connect(self.clicked)
    def clicked(self, qmodelindex):
            global item
            item = self.UpToDate_List.currentItem()

    def clicked2(self):
            url = str(f"https://cveawg.mitre.org/api/cve/{item.text()}")
            try:
                    response = requests.get(url)
            except:
                    print("Cant get data. Check your connection.")
            json_data = json.loads(response.text)
            #print(json_data)
            self.UpToDate_CVEID.clear()
            self.UpToDate_CVEID.insertPlainText(item.text())
            try:
                    vulnerabilitytypes = json_data["containers"]["cna"]["problemTypes"][0]["descriptions"][0]["description"]
                    self.UpToDate_CVEType.clear()
                    self.UpToDate_CVEType.insertPlainText(vulnerabilitytypes)
            except:
                    self.UpToDate_CVEType.clear()
                    self.UpToDate_CVEType.insertPlainText("Vulnerability Type Data not found.")
            try:
                    aciklama = json_data["containers"]["cna"]["descriptions"][0]["value"]
                    self.UpToDate_CVEDescription.clear()
                    self.UpToDate_CVEDescription.insertPlainText(aciklama)
            except:
                    self.UpToDate_CVEDescription.clear()
                    self.UpToDate_CVEDescription.insertPlainText("Description Data Not Found")
            try:
                    etkilenencihazlar = json_data["containers"]["cna"]["affected"][0]["product"]
                    self.UpToDate_AffectedThings.clear()
                    self.UpToDate_AffectedThings.insertPlainText(etkilenencihazlar)
            except:
                    self.UpToDate_AffectedThings.clear()
                    self.UpToDate_AffectedThings.insertPlainText("Affected Devices Data Not Found")
            try:
                    yayinlanmatarihi = json_data["containers"]["cna"]["datePublic"]
                    self.SHARETIME_2.clear()
                    self.SHARETIME_2.insertPlainText(yayinlanmatarihi)
            except:
                    self.SHARETIME_2.clear()
                    self.SHARETIME_2.insertPlainText("Data Not Found")

    def cvespreading(self):
        cvesearch = self.CVESpread_SearchBar.toPlainText()
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
                self.CVESpread_AffectedThings.clear()
                self.CVESpread_AffectedThings.insertPlainText(etkilenencihazlar)
                URL = str(f"https://www.shodan.io/search/facet.png?query={etkilenencihazlar}&facet=country")
                response = requests.get(URL)
                open("cihazlar.png", "wb").write(response.content)
                self.CVESpread_ShodanIOPicture.insertHtml('<img src="cihazlar.png" width="790" height="410">')
        except:
                self.CVESpread_AffectedThings.clear()
                self.CVESpread_AffectedThings.insertPlainText("Data Not Found")
#Ben kaldım kardeş, ben kaldım... -Görkem Dolcek
#Kim bu yerden bitme karı? Ne anamız kaldı, ne avradımız -Azat Dolunay
#Yaralarım var, ama düşmedim ensesinden -Mehmet Demir
#Kod espri gibidir, açıklamak zorundaysan kötüdür -Talha Çaylı


    def setupUi(self, Dialog):
        #gui ayarları burdan başlıyor..
        Dialog.setWindowTitle("BugBazaar")
        Dialog.setObjectName("Dialog")
        Dialog.resize(880, 625)
        Dialog.setStyleSheet("")
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        Dialog.setWindowIcon(QtGui.QIcon('ladybug.ico')) #cok tatli<3
        font2 = QtGui.QFont()
        font2.setFamily("Lucida Console")
        font2.setPointSize(25)
        font3 = QtGui.QFont()
        font3.setFamily("Lucida Console")
        font3.setPointSize(20)
        font7 = QtGui.QFont()
        font7.setFamily("Lucida Console")
        font7.setPointSize(14)

        #Ana ekranin calismaya basladigi alan
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(-2, -2, 890, 635))
        self.tabWidget.setMinimumSize(QtCore.QSize(50, 50))
        self.tabWidget.setBaseSize(QtCore.QSize(500, 500))
        font = QtGui.QFont()
        font.setFamily("Javanese Text")
        font.setPointSize(15)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        #tab_4 anasayfamiz burasi onun ayarlari
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        #tab4te arka plana fotograf koymak icin bir frame olusturduk onun ayarlari burda
        self.frame = QtWidgets.QFrame(self.tab_4)
        self.frame.setGeometry(QtCore.QRect(-10, -20, 900, 700))
        #stylesheet ile ekledik framein ustune, sonra framenin cikma sirasini raise ile belirliyoruz
        self.frame.setStyleSheet("background-image: url(:/karlostanselamlar/Free-HD-Solid-Color-Wallpaper-Download.png);\n"
"        background-repeat: no-repeat; \n"
"        background-position: center;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        #Githuba yonlendirmek icin frame gibi gozuken bi buton ayarlamistik flat ile sadece gorunmez yapiyoruz stylesheet ile resim olmasini sagliyoruz
        self.GitHubButton = QtWidgets.QPushButton(self.tab_4)
        self.GitHubButton.setGeometry(QtCore.QRect(270, 40, 351, 271))
        self.GitHubButton.setStyleSheet("border-image: url(:/karlostanselamlar/ladybug.png);")
        self.GitHubButton.setText("")
        self.GitHubButton.setAutoDefault(False)
        self.GitHubButton.setDefault(False)
        self.GitHubButton.setFlat(True)
        self.GitHubButton.setObjectName("GitHubButton")
        self.GitHubButton.clicked.connect(self.githubfunc)
        #Authors kısmının yazdığı text browser
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_4)
        self.textBrowser.setGeometry(QtCore.QRect(240, 330, 431, 181))
        self.textBrowser.setStyleSheet("background-color: transparent")
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setLineWidth(0)
        self.textBrowser.setObjectName("textBrowser")
        self.frame.raise_()
        self.GitHubButton.raise_()
        self.textBrowser.raise_()
        self.tabWidget.addTab(self.tab_4, "")
        #Cve Search Function kisminin sekmesi
        self.tab = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("Jokerman")
        self.tab.setFont(font)
        self.tab.setObjectName("tab")
        #Cve Aratma Kısmı Search Bar Ayar Kısmı Burası
        self.CVESearch_SearchBar = QtWidgets.QPlainTextEdit(self.tab)
        self.CVESearch_SearchBar.setGeometry(QtCore.QRect(50, 21, 790, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(31)
        self.CVESearch_SearchBar.setFont(font)
        self.CVESearch_SearchBar.setAutoFillBackground(False)
        self.CVESearch_SearchBar.setStyleSheet(" background-color: white;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:10px;\n"
"ScrollBarAlwaysOff")
        self.CVESearch_SearchBar.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.CVESearch_SearchBar.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        #Search Button ayarlari burda
        self.CVESearch_SearchButton = QtWidgets.QPushButton(self.tab)
        self.CVESearch_SearchButton.setGeometry(QtCore.QRect(710, 25, 120, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        self.CVESearch_SearchButton.setFont(font)
        self.CVESearch_SearchButton.clicked.connect(self.cvesearch_funcbutton) #Butona tiklandiginda cvesearch_funcbutton fonksiyonunu cagiriyo, kabakodda bu satirdan sonrasina
        #fonksiyon ile devam edicez bittikten sonra 285.satırdan devam tarzinda olcak
        #CVE ID arkasinda duran beyaz koseli frame
        self.frame_4 = QtWidgets.QFrame(self.tab)
        self.frame_4.setGeometry(QtCore.QRect(50, 100, 210, 40))
        self.frame_4.setStyleSheet(" background-color: white;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:10px;\n"
"ScrollBarAlwaysOff")
        #CVE_ID yazısı -htmlden nefret ediyorum-
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.frame_4)
        self.textBrowser_2.setGeometry(QtCore.QRect(30, 7, 151, 21))
        self.textBrowser_2.setStyleSheet(" border-width:0px;\n"
"")
        self.textBrowser_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        #Search CVE ID yani sonuclarda cveidin denk geldigi kismin arkasi
        self.frame_6 = QtWidgets.QFrame(self.tab)
        self.frame_6.setGeometry(QtCore.QRect(280, 100, 561, 41))
        self.frame_6.setStyleSheet(" background-color: white;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:10px;\n"
"ScrollBarAlwaysOff")
        #Sonuclardan gelen cve id'in ayarlari
        self.Search_CVE_ID = QtWidgets.QTextBrowser(self.frame_6)
        self.Search_CVE_ID.setGeometry(QtCore.QRect(0, 0, 561, 41))
        self.Search_CVE_ID.setStyleSheet("border-width:0px;")
        self.Search_CVE_ID.setReadOnly(1)
        self.Search_CVE_ID.setFont(font2)
        self.Search_CVE_ID.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Search_CVE_ID.setAlignment(QtCore.Qt.AlignCenter)
        #Vulnerability Type yazisinin arkasi
        self.frame_17 = QtWidgets.QFrame(self.tab)
        self.frame_17.setGeometry(QtCore.QRect(50, 150, 211, 41))
        self.frame_17.setStyleSheet(" background-color: white;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:10px;\n"
"ScrollBarAlwaysOff")
        #Vulnerability Type Yazısı
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.frame_17)
        self.textBrowser_5.setGeometry(QtCore.QRect(30, 7, 151, 21))
        self.textBrowser_5.setStyleSheet(" border-width:0px;\n"
"")
        self.textBrowser_5.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_5.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        #Vulnerability Type değerinin arka planı
        self.frame_18 = QtWidgets.QFrame(self.tab)
        self.frame_18.setGeometry(QtCore.QRect(280, 150, 561, 41))
        self.frame_18.setStyleSheet(" background-color: white;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:10px;\n"
"ScrollBarAlwaysOff")
        #Vulnerability Type değerinin olduğu alan
        self.Search_Vulnerability_Type = QtWidgets.QTextBrowser(self.frame_18)
        self.Search_Vulnerability_Type.setGeometry(QtCore.QRect(0, 0, 561, 41))
        self.Search_Vulnerability_Type.setStyleSheet(" border-width:0px;\n"
"")
        self.Search_Vulnerability_Type.setFont(font2)
        self.Search_Vulnerability_Type.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Search_Vulnerability_Type.setAlignment(QtCore.Qt.AlignCenter)
        #Search Cve Description değişkenin arkası
        self.frame_19 = QtWidgets.QFrame(self.tab)
        self.frame_19.setGeometry(QtCore.QRect(280, 200, 561, 181))
        self.frame_19.setStyleSheet(" background-color: white;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:10px;\n"
"ScrollBarAlwaysOff")
        #Cve Açıklaması
        self.Search_CVE_Description = QtWidgets.QTextBrowser(self.frame_19)
        self.Search_CVE_Description.setGeometry(QtCore.QRect(0, 0, 561, 181))
        self.Search_CVE_Description.setStyleSheet(" border-width:0px;\n"
"")
        self.Search_CVE_Description.setFont(font2)
        self.Search_CVE_Description.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Search_CVE_Description.setAlignment(QtCore.Qt.AlignCenter)
        #CVE Description yazısının arkası
        self.frame_20 = QtWidgets.QFrame(self.tab)
        self.frame_20.setGeometry(QtCore.QRect(50, 200, 211, 181))
        self.frame_20.setStyleSheet(" background-color: white;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:10px;\n"
"ScrollBarAlwaysOff")
        #Cve Description yazısı
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.frame_20)
        self.textBrowser_6.setGeometry(QtCore.QRect(22, 75, 171, 21))
        self.textBrowser_6.setStyleSheet(" border-width:0px;\n"
"")
        self.textBrowser_6.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_6.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        #Affected Devices Yazısının arkası
        self.frame_21 = QtWidgets.QFrame(self.tab)
        self.frame_21.setGeometry(QtCore.QRect(50, 390, 211, 101))
        self.frame_21.setStyleSheet(" background-color: white;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:10px;\n"
"ScrollBarAlwaysOff")
        #Affected Devices Yazısı
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.frame_21)
        self.textBrowser_7.setGeometry(QtCore.QRect(30, 40, 151, 21))
        self.textBrowser_7.setStyleSheet(" border-width:0px;\n"
"")
        self.textBrowser_7.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_7.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        #Etkilenen Cihazlar Verisinin arkası
        self.frame_22 = QtWidgets.QFrame(self.tab)
        self.frame_22.setGeometry(QtCore.QRect(280, 390, 561, 101))
        self.frame_22.setStyleSheet(" background-color: white;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:10px;\n"
"ScrollBarAlwaysOff")
        #Etkilenen Cihazlar Verisinin olduğu kısım
        self.Search_CVEAffectedThings = QtWidgets.QTextBrowser(self.frame_22)
        self.Search_CVEAffectedThings.setGeometry(QtCore.QRect(0, 0, 561, 101))
        self.Search_CVEAffectedThings.setStyleSheet(" border-width:0px;\n"
"")
        self.Search_CVEAffectedThings.setFont(font2)
        self.Search_CVEAffectedThings.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Search_CVEAffectedThings.setAlignment(QtCore.Qt.AlignCenter)
        #Yayınlanma Zamanı Kkısmının Ayarları
        self.Search_PublishTime = QtWidgets.QTextBrowser(self.tab)
        self.Search_PublishTime.setGeometry(QtCore.QRect(530, 510, 311, 41))
        self.Search_PublishTime.setFont(font7)
        self.Search_PublishTime.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Search_PublishTime.setAlignment(QtCore.Qt.AlignCenter)
        #Arkaplan resmi
        self.frame_3 = QtWidgets.QFrame(self.tab)
        self.frame_3.setGeometry(QtCore.QRect(-20, -10, 951, 641))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        self.frame_3.setFont(font)
        self.frame_3.setStyleSheet("background-image: url(:/karlostanselamlar/Free-HD-Solid-Color-Wallpaper-Download.png);")
        self.frame_3.raise_()
        self.CVESearch_SearchBar.raise_()
        self.CVESearch_SearchButton.raise_()
        self.frame_4.raise_()
        self.frame_6.raise_()
        self.frame_17.raise_()
        self.frame_18.raise_()
        self.frame_19.raise_()
        self.frame_20.raise_()
        self.frame_21.raise_()
        self.frame_22.raise_()
        self.Search_PublishTime.raise_()
        #List Of Up-To-Date sekmesi
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        #Cvelerin olduğu liste
        self.UpToDate_List = QtWidgets.QListWidget(self.tab_3)
        self.UpToDate_List.setGeometry(QtCore.QRect(635, 69, 230, 491))
        self.UpToDate_Query = QtWidgets.QPushButton(self.tab_3)
        self.UpToDate_Query.setGeometry(QtCore.QRect(635, 10, 230, 50))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        #Query cveyi sorgulama butonu
        self.UpToDate_Query.setFont(font)
        self.UpToDate_Query.clicked.connect(self.clicked2) #Tıklandıgında clicked2 fonksiyonunu cagirioyr dikkat burda
        self.UpToDate_DBQuery = QtWidgets.QPushButton(self.tab_3)
        self.UpToDate_DBQuery.setGeometry(QtCore.QRect(20, 10, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        self.UpToDate_DBQuery.setFont(font)
        self.UpToDate_DBQuery.clicked.connect(self.mostknowncves) #Fonksiyon cagiriyor butona tikladiginda
        #CVE_ID yazısının arka planı
        self.frame_7 = QtWidgets.QFrame(self.tab_3)
        self.frame_7.setGeometry(QtCore.QRect(20, 80, 211, 41))
        self.frame_7.setStyleSheet(" background-color: white;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:10px;\n"
"ScrollBarAlwaysOff")
        #CVE_ID yazısı
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.frame_7)
        self.textBrowser_3.setGeometry(QtCore.QRect(30, 10, 151, 21))
        self.textBrowser_3.setStyleSheet(" border-width:0px;\n"
"")
        self.textBrowser_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        #CVE ID Değerinin arka planı
        self.frame_8 = QtWidgets.QFrame(self.tab_3)
        self.frame_8.setGeometry(QtCore.QRect(250, 80, 371, 41))
        self.frame_8.setStyleSheet(" background-color: white;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:10px;\n"
"ScrollBarAlwaysOff")
        #CVE ID değeri
        self.UpToDate_CVEID = QtWidgets.QTextBrowser(self.frame_8)
        self.UpToDate_CVEID.setGeometry(QtCore.QRect(0, 0, 371, 41))
        self.UpToDate_CVEID.setStyleSheet(" border-width:0px;\n"
"")
        self.UpToDate_CVEID.setFont(font2)
        self.UpToDate_CVEID.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.UpToDate_CVEID.setAlignment(QtCore.Qt.AlignCenter)
        #Vulnerability Type yazısının arka planı
        self.frame_23 = QtWidgets.QFrame(self.tab_3)
        self.frame_23.setGeometry(QtCore.QRect(20, 140, 211, 41))
        self.frame_23.setStyleSheet(" background-color: white;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:10px;\n"
"ScrollBarAlwaysOff")
        #Vulnerability Type yazısı
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.frame_23)
        self.textBrowser_8.setGeometry(QtCore.QRect(30, 10, 151, 21))
        self.textBrowser_8.setStyleSheet(" border-width:0px;\n"
"")
        self.textBrowser_8.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_8.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        #Vulnerability Type Değerinin Arkaplanı
        self.frame_24 = QtWidgets.QFrame(self.tab_3)
        self.frame_24.setGeometry(QtCore.QRect(250, 140, 371, 41))
        self.frame_24.setStyleSheet(" background-color: white;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:10px;\n"
"ScrollBarAlwaysOff")
        #Vulnerability Type Değeri
        self.UpToDate_CVEType = QtWidgets.QTextBrowser(self.frame_24)
        self.UpToDate_CVEType.setGeometry(QtCore.QRect(0, 0, 371, 41))
        self.UpToDate_CVEType.setStyleSheet(" border-width:0px;\n"
"")
        self.UpToDate_CVEType.setFont(font7)
        self.UpToDate_CVEType.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.UpToDate_CVEType.setAlignment(QtCore.Qt.AlignCenter)
        #Cve Description yazısının arka planı
        self.frame_25 = QtWidgets.QFrame(self.tab_3)
        self.frame_25.setGeometry(QtCore.QRect(20, 200, 211, 181))
        self.frame_25.setStyleSheet(" background-color: white;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:10px;\n"
"ScrollBarAlwaysOff")
        #Cve Description yazısı
        self.textBrowser_9 = QtWidgets.QTextBrowser(self.frame_25)
        self.textBrowser_9.setGeometry(QtCore.QRect(20, 70, 171, 21))
        self.textBrowser_9.setStyleSheet(" border-width:0px;\n"
"")
        self.textBrowser_9.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_9.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        #Cve Description Değerinin arka planı
        self.frame_26 = QtWidgets.QFrame(self.tab_3)
        self.frame_26.setGeometry(QtCore.QRect(250, 200, 371, 181))
        self.frame_26.setStyleSheet(" background-color: white;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:10px;\n"
"ScrollBarAlwaysOff")
        #Cve Description Değeri
        self.UpToDate_CVEDescription = QtWidgets.QTextBrowser(self.frame_26)
        self.UpToDate_CVEDescription.setGeometry(QtCore.QRect(0, 0, 371, 181))
        self.UpToDate_CVEDescription.setStyleSheet(" border-width:0px;\n"
"")
        self.UpToDate_CVEDescription.setFont(font7)
        self.UpToDate_CVEDescription.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.UpToDate_CVEDescription.setAlignment(QtCore.Qt.AlignCenter)
        #Affected Devices yazısının arkaplanı
        self.frame_27 = QtWidgets.QFrame(self.tab_3)
        self.frame_27.setGeometry(QtCore.QRect(20, 400, 211, 101))
        self.frame_27.setStyleSheet(" background-color: white;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:10px;\n"
"ScrollBarAlwaysOff")
        #Affected Devices yazısı
        self.textBrowser_10 = QtWidgets.QTextBrowser(self.frame_27)
        self.textBrowser_10.setGeometry(QtCore.QRect(30, 40, 151, 21))
        self.textBrowser_10.setStyleSheet(" border-width:0px;\n"
"")
        self.textBrowser_10.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_10.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        #Affected Devices değerinin arkaplanı
        self.frame_28 = QtWidgets.QFrame(self.tab_3)
        self.frame_28.setGeometry(QtCore.QRect(250, 400, 371, 101))
        self.frame_28.setStyleSheet(" background-color: white;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:10px;\n"
"ScrollBarAlwaysOff")
        #Affected Devices değeri
        self.UpToDate_AffectedThings = QtWidgets.QTextBrowser(self.frame_28)
        self.UpToDate_AffectedThings.setGeometry(QtCore.QRect(0, 0, 371, 101))
        self.UpToDate_AffectedThings.setStyleSheet(" border-width:0px;\n"
"")
        self.UpToDate_AffectedThings.setFont(font2)
        self.UpToDate_AffectedThings.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.UpToDate_AffectedThings.setAlignment(QtCore.Qt.AlignCenter)
        #Yayınlanma Tarihinin ayarları
        self.SHARETIME_2 = QtWidgets.QTextBrowser(self.tab_3)
        self.SHARETIME_2.setGeometry(QtCore.QRect(310, 520, 311, 41))
        self.SHARETIME_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.SHARETIME_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.SHARETIME_2.setFont(font7)
        self.SHARETIME_2.setAlignment(QtCore.Qt.AlignCenter)
        #Arkaplan Resmi
        self.frame_9 = QtWidgets.QFrame(self.tab_3)
        self.frame_9.setGeometry(QtCore.QRect(-10, -20, 911, 611))
        self.frame_9.setStyleSheet("background-image: url(:/karlostanselamlar/Free-HD-Solid-Color-Wallpaper-Download.png);")
        self.frame_9.raise_()
        #Guncel Veri Aciklarini Cektigimiz Sekmedeki Objelerin İleri
        #Atilmasini sagliyor. Yoksa resim onlerine gecer.
        self.UpToDate_List.raise_()
        self.UpToDate_Query.raise_()
        self.UpToDate_DBQuery.raise_()
        self.frame_7.raise_()
        self.frame_8.raise_()
        self.frame_23.raise_()
        self.frame_24.raise_()
        self.frame_25.raise_()
        self.frame_26.raise_()
        self.frame_27.raise_()
        self.frame_28.raise_()
        self.SHARETIME_2.raise_()
        self.tabWidget.addTab(self.tab_3, "")
        #Possible Spreading Tab
        self.tab_2 = QtWidgets.QWidget()
        #Arama Barı Ayarları
        self.CVESpread_SearchBar = QtWidgets.QPlainTextEdit(self.tab_2)
        self.CVESpread_SearchBar.setGeometry(QtCore.QRect(50, 10, 791, 51))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(31)
        self.CVESpread_SearchBar.setFont(font)
        self.CVESpread_SearchBar.setAutoFillBackground(False)
        self.CVESpread_SearchBar.setStyleSheet(" background-color: white;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:10px;\n"
"ScrollBarAlwaysOff")
        self.CVESpread_SearchBar.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.CVESpread_SearchBar.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.CVESpread_ShodanIOPicture = QtWidgets.QTextBrowser(self.tab_2)
        self.CVESpread_ShodanIOPicture.setGeometry(QtCore.QRect(50, 140, 800, 420))
        self.CVESpread_ShodanIOPicture.setStyleSheet("background-color: white; border-style: solid; border-width:1px; border-radius:10px; ScrollBarAlwaysOff")
       #Arama butonu ayarları
        self.CVESpread_SearchButton = QtWidgets.QPushButton(self.tab_2)
        self.CVESpread_SearchButton.setGeometry(QtCore.QRect(680, 15, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        self.CVESpread_SearchButton.setFont(font)
        self.CVESpread_SearchButton.clicked.connect(self.cvespreading)
        #Resmin Olduğu Alan
    #Affected Devices yazısının arkaplanı
        self.frame_29 = QtWidgets.QFrame(self.tab_2)
        self.frame_29.setGeometry(QtCore.QRect(50, 80, 211, 41))
        self.frame_29.setStyleSheet(" background-color: white;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:10px;\n"
"ScrollBarAlwaysOff")
        #Affected Devices Yazısı
        self.textBrowser_11 = QtWidgets.QTextBrowser(self.frame_29)
        self.textBrowser_11.setGeometry(QtCore.QRect(30, 10, 151, 21))
        self.textBrowser_11.setStyleSheet(" border-width:0px;\n"
"")
        self.textBrowser_11.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_11.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        #Affected Devices Değerinin Arkaplanı
        self.frame_30 = QtWidgets.QFrame(self.tab_2)
        self.frame_30.setGeometry(QtCore.QRect(280, 80, 561, 41))
        self.frame_30.setStyleSheet(" background-color: white;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:10px;\n"
"ScrollBarAlwaysOff")
        #Affected Devices Değeri
        self.CVESpread_AffectedThings = QtWidgets.QTextBrowser(self.frame_30)
        self.CVESpread_AffectedThings.setGeometry(QtCore.QRect(0, 0, 561, 41))
        self.CVESpread_AffectedThings.setStyleSheet(" border-width:0px;\n"
"")
        self.CVESpread_AffectedThings.setFont(font2)
        self.CVESpread_AffectedThings.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.CVESpread_AffectedThings.setAlignment(QtCore.Qt.AlignCenter)
        #Arkaplanı
        self.frame_11 = QtWidgets.QFrame(self.tab_2)
        self.frame_11.setGeometry(QtCore.QRect(-50, -10, 931, 601))
        self.frame_11.setStyleSheet("background-image: url(:/karlostanselamlar/Free-HD-Solid-Color-Wallpaper-Download.png);")
        self.frame_11.raise_()
        self.CVESpread_SearchBar.raise_()
        self.CVESpread_SearchButton.raise_()
        self.CVESpread_ShodanIOPicture.raise_()
        self.frame_29.raise_()
        self.frame_30.raise_()
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Dialog) #retranslateUi fonksiyonunu Dialog ekranı için çalıştırıyor, translate html ile yaptığımız textlerin görünütlenmesini sağlıyor
        self.tabWidget.setCurrentIndex(4) #Programın ana sayfadan açılmasını sağlıyor.
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; font-style:italic; color:#ffffff;\">Authors:</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; font-style:italic; color:#ffffff;\">Gorkem Dolcek (@gorkemdolcek) </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; font-style:italic; color:#ffffff;\">Mehmet Demir (@jackalkarlos) </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; font-style:italic; color:#ffffff;\">Dilara Senturk (@dilarasenturk)</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; font-style:italic; color:#ffffff;\">Talha Cayli (@talhacyl) </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; font-style:italic; color:#ffffff;\">Azat Dolunay (@Butex-a11)</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "Home"))
        self.CVESearch_SearchButton.setText(_translate("Dialog", "Search"))
        self.textBrowser_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">CVE ID:</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600; font-style:italic;\"><br /></p></body></html>"))
        self.textBrowser_5.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Vulnerability Type:</span></p></body></html>"))
        self.textBrowser_6.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">CVE Description:</span></p></body></html>"))
        self.textBrowser_7.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">Affected Things:</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "CVE Search Function"))
        self.UpToDate_Query.setText(_translate("Dialog", "Query"))
        self.UpToDate_DBQuery.setText(_translate("Dialog", "Check Up-to-Date CVE\'s"))
        self.textBrowser_3.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">CVE ID:</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600; font-style:italic;\"><br /></p></body></html>"))
        self.UpToDate_CVEID.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_8.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Vulnerability Type:</span></p></body></html>"))
        self.UpToDate_CVEType.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_9.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">CVE Description:</span></p></body></html>"))
        self.UpToDate_CVEDescription.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; marg     in-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_10.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">Affected Devices:</span></p></body></html>"))
        self.UpToDate_AffectedThings.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "List Of Up-to-date Vulnerabilites and Descriptions"))
        self.CVESpread_SearchButton.setText(_translate("Dialog", "Search"))
        self.textBrowser_11.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">Affected Devices:</span></p></body></html>"))
        self.CVESpread_AffectedThings.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "CVE Possible Spreading"))
import karlostanselamlar_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
