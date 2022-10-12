#!/usr/bin/env python3
from PySide2.QtWidgets import QApplication
from coll_asm_adj_gui.windows.assembly_adjuster_main import AssemblyAdjusterMain


if __name__ == "__main__":
    app = QApplication([])
    main_window = AssemblyAdjusterMain()
    main_window.show()
    app.exec_()
