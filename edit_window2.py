# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_window_2.ui'
#
# Created: Thu Apr 17 18:49:27 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(839, 745)
        #self.scrollArea = QtGui.QScrollArea()
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #self.centralwidget.inFullScreenResize = False
        #self.scrollArea.setWidget(self.centralwidget)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(270, 10, 551, 241))
        self.groupBox.setObjectName("groupBox")
        self.name_surname = QtGui.QLineEdit(self.groupBox)
        self.name_surname.setGeometry(QtCore.QRect(20, 30, 291, 21))
        self.name_surname.setObjectName("name_surname")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(350, 30, 151, 21))
        self.label.setObjectName("label")
        self.phone = QtGui.QLineEdit(self.groupBox)
        self.phone.setGeometry(QtCore.QRect(20, 60, 291, 21))
        self.phone.setObjectName("phone")
        self.city = QtGui.QLineEdit(self.groupBox)
        self.city.setGeometry(QtCore.QRect(20, 90, 291, 21))
        self.city.setObjectName("city")
        self.main_t = QtGui.QLineEdit(self.groupBox)
        self.main_t.setGeometry(QtCore.QRect(20, 120, 291, 21))
        self.main_t.setObjectName("main_t")
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(350, 120, 151, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(350, 60, 151, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(350, 90, 151, 21))
        self.label_5.setObjectName("label_5")
        self.minor_t = QtGui.QLineEdit(self.groupBox)
        self.minor_t.setGeometry(QtCore.QRect(20, 150, 291, 21))
        self.minor_t.setObjectName("minor_t")
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(350, 150, 151, 21))
        self.label_6.setObjectName("label_6")
        self.level = QtGui.QComboBox(self.groupBox)
        self.level.addItems(['','Weak junior', 'Junior', 'Srong junior', 
        						'Weak middle', 'Middle', 'Strong middle',
        						'Weak senior', 'Senior', 'Strong senior', 
        						'Architect'])
        self.level.setGeometry(QtCore.QRect(20, 180, 161, 26))
        self.level.setObjectName("level")
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(200, 180, 151, 31))
        self.label_7.setObjectName("label_7")
        self.photo_path = QtGui.QPushButton(self.groupBox)
        self.photo_path.setGeometry(QtCore.QRect(20, 210, 61, 23))
        self.photo_path.setObjectName("photo_path")
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(200, 210, 151, 21))
        self.label_8.setObjectName("label_8")
        self.profile_photo = QtGui.QGraphicsView(self.centralwidget)
        self.profile_photo.setGeometry(QtCore.QRect(20, 30, 211, 221))
        self.profile_photo.setObjectName("profile_photo")
        self.CV = QtGui.QPlainTextEdit(self.centralwidget)
        self.CV.setGeometry(QtCore.QRect(20, 290, 391, 411))
        self.CV.setObjectName("CV")
        self.comments = QtGui.QPlainTextEdit(self.centralwidget)
        self.comments.setGeometry(QtCore.QRect(440, 290, 361, 261))
        self.comments.setObjectName("comments")
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(439, 549, 381, 151))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 260, 151, 21))
        self.label_2.setObjectName("label_2")
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(440, 260, 151, 21))
        self.label_9.setObjectName("label_9")
        self.b_save = QtGui.QPushButton(self.centralwidget)
        self.b_save.setGeometry(QtCore.QRect(690, 660, 114, 32))
        self.b_save.setObjectName("b_save")
        self.b_upload = QtGui.QPushButton(self.centralwidget)
        self.b_upload.setGeometry(QtCore.QRect(690, 630, 114, 32))
        self.b_upload.setObjectName("b_upload")
        self.cv_path = QtGui.QPushButton(self.centralwidget)
        self.cv_path.setGeometry(QtCore.QRect(750, 600, 51, 23))
        self.cv_path.setObjectName("cv_path")
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(670, 570, 91, 21))
        self.label_10.setObjectName("label_10")
        self.indicator_cv = QtGui.QRadioButton(self.centralwidget)
        self.indicator_cv.setGeometry(QtCore.QRect(670, 600, 71, 20))
        self.indicator_cv.setObjectName("indicator_cv")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 839, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Main information", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Name, Surname", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Main tech.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Phone number", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "City", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Minor tech.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Candidate\'s level", None, QtGui.QApplication.UnicodeUTF8))
        self.photo_path.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Upload photo", None, QtGui.QApplication.UnicodeUTF8))
        self.CV.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>copy CV content here</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.comments.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>write your comments here</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "CV", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Comments", None, QtGui.QApplication.UnicodeUTF8))
        self.b_save.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>save chnges (locally)</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.b_save.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.b_upload.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>upload changes to server</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.b_upload.setText(QtGui.QApplication.translate("MainWindow", "Upload", None, QtGui.QApplication.UnicodeUTF8))
        self.cv_path.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>upload CV file</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.cv_path.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "Upload CV fie", None, QtGui.QApplication.UnicodeUTF8))
        self.indicator_cv.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>CV indicator</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.indicator_cv.setText(QtGui.QApplication.translate("MainWindow", "CV file", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Actions", None, QtGui.QApplication.UnicodeUTF8))

