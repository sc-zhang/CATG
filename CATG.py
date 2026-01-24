#!/usr/bin/env python3
import sys
from os import path
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from PySide6.QtCore import QCoreApplication, Qt
from qt_material import apply_stylesheet
from coll_asm_corr_gui.main.assembly_corrector_main import AssemblyCorrectorMain

if __name__ == "__main__":
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QApplication([])
    icon_path = path.join(path.dirname(path.abspath(__file__)), "coll_asm_corr_gui/resources/CATG.png")
    app.setWindowIcon(QIcon(icon_path))
    main_window = AssemblyCorrectorMain()
    apply_stylesheet(app, theme="dark_teal.xml")
    app.setStyleSheet(app.styleSheet() + """
    /* 输入框类：文字颜色 */
    QLineEdit, QTextEdit, QPlainTextEdit, QSpinBox, QDoubleSpinBox {
        color: #E6E6E6;
    }

    /* 下拉框显示区域 */
    QComboBox {
        color: #E6E6E6;
    }

    /* 下拉列表弹出框里的文字（非常常见的坑） */
    QComboBox QAbstractItemView {
        color: #E6E6E6;
    }

    /* Placeholder 文本（否则占位符还是发黑） */
    QLineEdit:!focus {
        selection-color: #FFFFFF;
    }

    /* 禁用态/只读态（可按需调） */
    QLineEdit:disabled, QTextEdit:disabled, QPlainTextEdit:disabled,
    QLineEdit[readOnly="true"] {
        color: #9A9A9A;
    }
    """)
    main_window.show()
    sys.exit(app.exec())
