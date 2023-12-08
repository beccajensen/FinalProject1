import sys

from PyQt6 import QtWidgets

import gui
import logic




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = gui.Ui_Form()
    ui.setupUi(Form)
    Logic = logic.Logic(ui)
    Form.show()
    sys.exit(app.exec())
