from PyQt5.QtWidgets import QApplication
import sys

import UI

def main_func():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    ex = UI.FluidLenght()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main_func()