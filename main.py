from PyQt5.QtWidgets import QApplication
import sys
import UI
import config

def main_func():
    app = QApplication(sys.argv)
    ex = config.configPage()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main_func()