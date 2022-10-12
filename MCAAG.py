#!/usr/bin/env python3
from PySide2.QtWidgets import QApplication
from PySide2.QtGui import QIcon
from coll_asm_adj_gui.windows.assembly_adjuster_main import AssemblyAdjusterMain
from coll_asm_adj_gui.io.resources_loader import resource_path


if __name__ == "__main__":
    app = QApplication([])
    icon_path = resource_path("coll_asm_adj_gui/ui/MCAAG.png")
    app.setWindowIcon(QIcon(icon_path))
    main_window = AssemblyAdjusterMain()
    main_window.show()
    app.exec_()
