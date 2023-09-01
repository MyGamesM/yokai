from sys import exit
from requests import get
from json import loads
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QLineEdit, QGridLayout
from PyQt6.QtGui import QImage,	QPixmap, QIcon

class App:
	def __init__(self) -> None:
		self.active: list[QWidget] = []
		self.width, self.height = 250, 122

		with open("data.json", "r", encoding="UTF-8") as f:
			self.data = loads(f.read())

		self.app = QApplication([])
		_, _, self.screen_width, self.screen_height = QApplication.primaryScreen().geometry().getRect()

		self.window = QWidget()
		self.window.setWindowTitle("Medallium")
		self.window.setStyleSheet("background-color: #333")
		self.window.setWindowIcon(QIcon("imgs/watch.png"))
		self.window.setGeometry(
			int(self.screen_width / 2 - (250 / 2)),
			int(self.screen_height / 2 - (122 / 2)),
			self.width, self.height
		)
		
		self.window.setFixedSize(250, 122)

		self.layout = QGridLayout()
		self.window.setLayout(self.layout)
		self.window.show()
		self.searchScreen()
		exit(self.app.exec())

	def clearScreen(self) -> None:
		for widget in self.active:
			widget.setParent(None)

	def searchScreen(self) -> None:
		self.clearScreen()

		label = QLabel("Insert yokai id to search")
		label.setStyleSheet("font-size: 21px; color: #ccc")
		self.layout.addWidget(label, 0, 0, 1, 2, Qt.AlignmentFlag.AlignCenter)
		self.active.append(label)

		self.entry = QLineEdit()
		self.entry.setStyleSheet("border: 1 solid #bbb; color: #ccc")
		self.layout.addWidget(self.entry, 1, 0, 1, 2)
		self.active.append(self.entry)

		button = QPushButton("Open")
		button.clicked.connect(self.dataScreen)
		button.setStyleSheet("border: 1 solid #bbb; color: #ccc; background-color: #444")
		self.layout.addWidget(button, 2, 0)
		self.active.append(button)

		self.quitButton(2, 1, 1, 1)

	def dataScreen(self) -> None:
		self.clearScreen()

		try:
			id = int(self.entry.text())
			if id < 0 or id > 223:
				self.errorScreen()
				return
			else:
				yokai = self.data[self.entry.text()]
		except:
			self.errorScreen()
			return

		name_label = QLabel(f"Name: {yokai['name']}")
		name_label.setStyleSheet("border: 1 solid #bbb; color: #ccc")
		self.layout.addWidget(name_label, 0, 0, 1, 2)
		self.active.append(name_label)

		food_label = QLabel(f"Fav. Food: {yokai['food']}")
		food_label.setStyleSheet("border: 1 solid #bbb; color: #ccc")
		self.layout.addWidget(food_label, 0, 2, 1, 2)
		self.active.append(food_label)

		for i, key in enumerate(yokai["links"]):
			image = QImage()
			image.loadFromData(get(yokai["links"][key]).content)

			image_label = QLabel()
			image_label.setStyleSheet("border: 1px solid #bbb")
			image_label.setPixmap(QPixmap(image))
			self.layout.addWidget(image_label, 1, i)
			self.active.append(image_label)

		back_button = QPushButton("Search")
		back_button.setStyleSheet("border: 1 solid #bbb; color: #ccc")
		back_button.clicked.connect(self.searchScreen)
		self.layout.addWidget(back_button, 2, 0, 1, 2)
		self.active.append(back_button)

		self.quitButton(2, 2, 1, 2)

	def errorScreen(self) -> None:
		self.searchScreen()

	def quitButton(self, row, col, rowspan, colspan) -> None:
		quit_button = QPushButton("Quit")
		quit_button.setStyleSheet("border: 1 solid #bbb; color: #ccc")
		quit_button.clicked.connect(QApplication.instance().quit)
		self.layout.addWidget(quit_button, row, col, rowspan, colspan)
		self.active.append(quit_button)

if __name__ == "__main__":
	import os
	os.system("cls")
	app = App()