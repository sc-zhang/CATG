#!/usr/bin/env python3
from PySide2.QtWidgets import QApplication
from PySide2.QtGui import QIcon
from coll_asm_adj_gui.windows.assembly_adjuster_main import AssemblyAdjusterMain


if __name__ == "__main__":
    app = QApplication([])
    app.setWindowIcon(QIcon("coll_asm_adj_gui/ui/MCAAG.png"))
    main_window = AssemblyAdjusterMain()
    main_window.show()
    app.exec_()
