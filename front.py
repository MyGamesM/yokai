import os, sys, pyautogui, requests, json
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QLineEdit, QGridLayout
from PyQt6.QtGui import QImage,	QPixmap

os.system("cls")

class App:
	def __init__(self) -> None:
		self.width, self.height = 150, 150
		self.screen_width, self.screen_height = pyautogui.size()

		with open("data.json", "r", encoding="UTF-8") as f:
			self.data = json.loads(f.read())

		self.app = QApplication([])

		self.window = QWidget()
		self.window.setWindowTitle("\n")
		self.window.setStyleSheet("background-color: #333")
		self.window.setGeometry(
				int(self.screen_width / 2 - (self.width / 2)),
				int(self.screen_height / 2 - (self.height / 2)),
				self.width,
				self.height
			)

		self.layout = QGridLayout()
		self.window.setLayout(self.layout)

		self.entry = QLineEdit()
		self.entry.setFixedWidth(150)
		self.entry.setStyleSheet("color: #ccc")
		self.layout.addWidget(self.entry, 0, 0)

		self.button = QPushButton("Open")
		self.button.setFixedWidth(150)
		self.button.clicked.connect(self.load_data)
		self.button.setStyleSheet("color: #ccc; background-color: #444")
		self.layout.addWidget(self.button, 1, 0)

		self.window.show()

		sys.exit(self.app.exec())

	def load_data(self):
		self.entry.setParent(None)
		self.button.setParent(None)

		yokai = self.data[self.entry.text()]

		name_label = QLabel(f"Name: {yokai['name']}")
		name_label.setStyleSheet("border: 1 solid #f00; color: #ccc")
		self.layout.addWidget(name_label, 0, 0, 1, 2)

		food_label = QLabel(f"Fav. Food: {yokai['food']}")
		food_label.setStyleSheet("border: 1 solid #0f0; color: #ccc")
		self.layout.addWidget(food_label, 0, 2, 1, 2)

		for i, key in enumerate(yokai["links"]):
			image = QImage()
			image.loadFromData(requests.get(yokai["links"][key]).content)

			image_label = QLabel()
			image_label.setStyleSheet("border: 1px solid #000")
			image_label.setPixmap(QPixmap(image))
			self.layout.addWidget(image_label, 1, i)

if __name__ == "__main__":
	app = App()