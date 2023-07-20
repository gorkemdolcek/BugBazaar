try:
    import sys
    import urllib
    import json
    import re
    import webbrowser
    try:
        import requests
        from PyQt5.QtCore import pyqtSlot, QFile, QTextStream
        from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
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

from bugbazaar import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self): # Ana pencereyi oluşturur
        super(MainWindow, self).__init__() #

        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self) 

        self.ui.icon_only_widget.hide() # Butonların sadece ikonlarını gösterir
        self.ui.stackedWidget.setCurrentIndex(0) # StackedWidget'ın hangi sayfada başlayacağını belirler
        self.ui.home_btn_2.setChecked(True) # Ana sayfanın seçili olmasını sağlar

    def on_stackedWidget_currentChanged(self, index): # StackedWidget'ın hangi sayfada olduğunu belirler
        btn_list = self.ui.icon_only_widget.findChildren(QPushButton) # Butonların listesini alır
        self.ui.full_menu_widget.findChildren(QPushButton) 
        
        for btn in btn_list: 
            if index in [5, 6]:
                btn.setAutoExclusive(False) # Butonların birbirini kapatmasını engeller
                btn.setChecked(False) # Butonların seçili olmasını engeller
            else:
                btn.setAutoExclusive(True) # Butonların birbirini kapatmasını engeller

      
    ## Menü dağılımı
    def on_home_btn_1_toggled(self): # Butonlar seçildiğinde stackedWidget'ın hangi sayfaya geçeceğini belirler
        self.ui.stackedWidget.setCurrentIndex(0) # 0. sayfa ana sayfa
    
    def on_home_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_cveSearch_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_cveSearch_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_cveList_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_cveList_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_possibleSpreading_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_possibleSpreading_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_authors_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def on_authors_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def on_search_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_user_btn_clicked(self): 
        self.ui.stackedWidget.setCurrentIndex(6)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    style_file = QFile("style.qss")
    style_file.open(QFile.ReadOnly | QFile.Text)
    style_stream = QTextStream(style_file)
    app.setStyleSheet(style_stream.readAll())


    window = MainWindow()
    window.show()

    sys.exit(app.exec())



