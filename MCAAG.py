#!/usr/bin/env python3
import sys
from os import path
from PySide2.QtWidgets import QApplication
from PySide2.QtGui import QIcon
from PySide2.QtCore import QCoreApplication, Qt
from qt_material import apply_stylesheet
from coll_asm_adj_gui.main.assembly_adjuster_main import AssemblyAdjusterMain


if __name__ == "__main__":
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QApplication([])
    icon_path = path.join(path.dirname(path.abspath(__file__)), "coll_asm_adj_gui/resources/MCAAG.png")
    app.setWindowIcon(QIcon(icon_path))
    main_window = AssemblyAdjusterMain()
    apply_stylesheet(app, theme="dark_teal.xml")
    main_window.show()
    sys.exit(app.exec_())
