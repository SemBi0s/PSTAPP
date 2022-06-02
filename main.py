from mainwindow import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox

from PyQt5.uic import loadUi
import sys


class Window(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


    def findAndReplace(self):
        dialog = FindReplaceDialog(self)
        dialog.exec()

class FindReplaceDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("PST_APP.ui", self)



def main():

	app = QApplication(sys.argv)

	# Create a Qt widget, which will be our window.
	window = Window()
	window.show()  # IMPORTANT!!!!! Windows are hidden by default.

	# Start the event loop.
	sys.exit(app.exec())


if __name__ == "__main__":
    main()
