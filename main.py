#! /usr/bin/python

import sys
import platform

from edit_window2 import Ui_MainWindow
from PySide.QtGui import (QApplication, QMainWindow, QTextEdit,
                         QPushButton,  QMessageBox, QFileDialog,QComboBox)



class MainWindow(Ui_MainWindow, QMainWindow):
	def __init__(self, parent=None):
		super(MainWindow,self).__init__(parent)
		self.setupUi(self)

		self.connect_vidgets()


	def connect_vidgets(self):
		self.name_surname.editingFinished.connect(self.get_name)
		self.phone.editingFinished.connect(self.get_phone)
		self.city.editingFinished.connect(self.get_city)
		self.main_t.editingFinished.connect(self.get_main_tech)
		self.minor_t.editingFinished.connect(self.get_minor_t)
		self.level.activated.connect(self.get_level) 

		self.comments.textChanged.connect(self.get_comments)
		self.CV.textChanged.connect(self.get_cv)

		self.photo_path.clicked.connect(self.get_photo)
		self.cv_path.clicked.connect(self.get_cv_file)
		self.b_save.clicked.connect(self.save_triggered)
		self.b_upload.clicked.connect(self.upload_triggered)


	def get_name(self):
		self.Name_surname = self.name_surname.text()
		print self.Name_surname

	def get_phone(self):
		self.Phone = self.phone.text()
		print self.Phone

	def get_city(self):
		self.City = self.city.text()
		print self.City

	def get_main_tech(self):
		self.Main_tech = self.main_t.text()
		print self.Main_tech

	def get_minor_t(self):
		self.Minor_tech = self.minor_t.text()
		print self.Minor_tech

	def get_comments(self):
		self.Comments = self.comments.toPlainText()  # toPlainText 
		print self.Comments

	def get_cv(self):
		self.cv = self.CV.toPlainText()  # toPlainText 
		print self.cv

	def get_photo(self):
		self.Photo_path = QFileDialog.getOpenFileName(self,("Open Image"),
			                                       ("Image Files (*.png *.jpg *.bmp *.JPG)"))
		print self.Photo_path

	def get_cv_file(self):
		self.CV_file = QFileDialog.getOpenFileName(self,("Open CV file"))


	def save_triggered(self):
		print 'going to save your changes'

	def upload_triggered(self):
		print 'Upload ypur changes'

	def get_level(self):
		print self.level.currentText()




if __name__ == "__main__":
	app = QApplication(sys.argv)
	frame=MainWindow()
	frame.show()
	app.exec_()