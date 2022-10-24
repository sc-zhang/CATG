# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'assembly_adjuster_mainSfJexb.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGraphicsView, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QWidget)
from coll_asm_corr_gui.ui.custom_control import ControlGraphicsView

class Ui_AssemblyCorrectorMain(object):
    def setupUi(self, AssemblyCorrectorMain):
        if not AssemblyCorrectorMain.objectName():
            AssemblyCorrectorMain.setObjectName(u"AssemblyAdjusterMain")
        AssemblyCorrectorMain.resize(1936, 1147)
        self.gridLayout_2 = QGridLayout(AssemblyCorrectorMain)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.plot_viewer = ControlGraphicsView(AssemblyCorrectorMain)
        self.plot_viewer.setObjectName(u"plot_viewer")
        self.plot_viewer.setEnabled(False)

        self.gridLayout_2.addWidget(self.plot_viewer, 0, 0, 1, 1)

        self.Frame = QFrame(AssemblyCorrectorMain)
        self.Frame.setObjectName(u"Frame")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Frame.sizePolicy().hasHeightForWidth())
        self.Frame.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.Frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.Frame)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 9, 0, 1, 1)

        self.blk_lst = QListWidget(self.Frame)
        self.blk_lst.setObjectName(u"blk_lst")
        self.blk_lst.setEnabled(False)

        self.gridLayout.addWidget(self.blk_lst, 4, 0, 1, 2)

        self.src_chr_cbox = QComboBox(self.Frame)
        self.src_chr_cbox.setObjectName(u"src_chr_cbox")
        self.src_chr_cbox.setEnabled(False)

        self.gridLayout.addWidget(self.src_chr_cbox, 7, 1, 1, 1)

        self.line = QFrame(self.Frame)
        self.line.setObjectName(u"line")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy1)
        self.line.setSizeIncrement(QSize(0, 0))
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QFrame.HLine)

        self.gridLayout.addWidget(self.line, 2, 0, 1, 2)

        self.label_3 = QLabel(self.Frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 8, 0, 1, 1)

        self.line_2 = QFrame(self.Frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QFrame.HLine)

        self.gridLayout.addWidget(self.line_2, 13, 0, 1, 2)

        self.method_cbox = QComboBox(self.Frame)
        self.method_cbox.setObjectName(u"method_cbox")
        self.method_cbox.setEnabled(False)

        self.gridLayout.addWidget(self.method_cbox, 12, 1, 1, 1)

        self.tgt_chr_cbox = QComboBox(self.Frame)
        self.tgt_chr_cbox.setObjectName(u"tgt_chr_cbox")
        self.tgt_chr_cbox.setEnabled(False)

        self.gridLayout.addWidget(self.tgt_chr_cbox, 9, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.file_loader_btn = QPushButton(self.Frame)
        self.file_loader_btn.setObjectName(u"file_loader_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.file_loader_btn.sizePolicy().hasHeightForWidth())
        self.file_loader_btn.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.file_loader_btn.setFont(font1)

        self.horizontalLayout_2.addWidget(self.file_loader_btn)

        self.file_save_btn = QPushButton(self.Frame)
        self.file_save_btn.setObjectName(u"file_save_btn")
        self.file_save_btn.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.file_save_btn.sizePolicy().hasHeightForWidth())
        self.file_save_btn.setSizePolicy(sizePolicy2)
        self.file_save_btn.setFont(font1)

        self.horizontalLayout_2.addWidget(self.file_save_btn)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 2)

        self.label_5 = QLabel(self.Frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.gridLayout.addWidget(self.label_5, 11, 0, 1, 1)

        self.resolution_text = QLineEdit(self.Frame)
        self.resolution_text.setObjectName(u"resolution_text")

        self.gridLayout.addWidget(self.resolution_text, 11, 1, 1, 1)

        self.rev_chk = QCheckBox(self.Frame)
        self.rev_chk.setObjectName(u"rev_chk")
        self.rev_chk.setEnabled(False)

        self.gridLayout.addWidget(self.rev_chk, 12, 0, 1, 1)

        self.label_6 = QLabel(self.Frame)
        self.label_6.setObjectName(u"label_6")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_6.setFont(font2)

        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)

        self.label = QLabel(self.Frame)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 7, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.undo_btn = QPushButton(self.Frame)
        self.undo_btn.setObjectName(u"undo_btn")
        self.undo_btn.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.undo_btn.sizePolicy().hasHeightForWidth())
        self.undo_btn.setSizePolicy(sizePolicy2)
        self.undo_btn.setFont(font1)

        self.horizontalLayout.addWidget(self.undo_btn)

        self.refresh_btn = QPushButton(self.Frame)
        self.refresh_btn.setObjectName(u"refresh_btn")
        self.refresh_btn.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.refresh_btn.sizePolicy().hasHeightForWidth())
        self.refresh_btn.setSizePolicy(sizePolicy2)
        self.refresh_btn.setFont(font1)

        self.horizontalLayout.addWidget(self.refresh_btn)

        self.mod_btn = QPushButton(self.Frame)
        self.mod_btn.setObjectName(u"mod_btn")
        self.mod_btn.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.mod_btn.sizePolicy().hasHeightForWidth())
        self.mod_btn.setSizePolicy(sizePolicy2)
        self.mod_btn.setFont(font1)

        self.horizontalLayout.addWidget(self.mod_btn)


        self.gridLayout.addLayout(self.horizontalLayout, 14, 0, 1, 2)

        self.line_3 = QFrame(self.Frame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShadow(QFrame.Plain)
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QFrame.HLine)

        self.gridLayout.addWidget(self.line_3, 5, 0, 1, 2)

        self.src_blk_cbox = QComboBox(self.Frame)
        self.src_blk_cbox.setObjectName(u"src_blk_cbox")
        self.src_blk_cbox.setEnabled(False)

        self.gridLayout.addWidget(self.src_blk_cbox, 8, 1, 1, 1)

        self.tgt_blk_cbox = QComboBox(self.Frame)
        self.tgt_blk_cbox.setObjectName(u"tgt_blk_cbox")
        self.tgt_blk_cbox.setEnabled(False)

        self.gridLayout.addWidget(self.tgt_blk_cbox, 10, 1, 1, 1)

        self.label_4 = QLabel(self.Frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 10, 0, 1, 1)

        self.label_7 = QLabel(self.Frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)


        self.gridLayout_2.addWidget(self.Frame, 0, 1, 1, 1)


        self.retranslateUi(AssemblyCorrectorMain)

        QMetaObject.connectSlotsByName(AssemblyCorrectorMain)
    # setupUi

    def retranslateUi(self, AssemblyAdjusterMain):
        AssemblyAdjusterMain.setWindowTitle(QCoreApplication.translate("AssemblyAdjusterMain", u"CATG", None))
        self.label_2.setText(QCoreApplication.translate("AssemblyAdjusterMain", u"Target chromosome:", None))
        self.label_3.setText(QCoreApplication.translate("AssemblyAdjusterMain", u"Source block id:", None))
        self.file_loader_btn.setText(QCoreApplication.translate("AssemblyAdjusterMain", u"Load files", None))
        self.file_save_btn.setText(QCoreApplication.translate("AssemblyAdjusterMain", u"Save files", None))
        self.label_5.setText(QCoreApplication.translate("AssemblyAdjusterMain", u"Resolution:", None))
        self.resolution_text.setText(QCoreApplication.translate("AssemblyAdjusterMain", u"20", None))
        self.rev_chk.setText(QCoreApplication.translate("AssemblyAdjusterMain", u"Reverse", None))
        self.label_6.setText(QCoreApplication.translate("AssemblyAdjusterMain", u"Contigs in current block:", None))
        self.label.setText(QCoreApplication.translate("AssemblyAdjusterMain", u"Source chromosome:", None))
        self.undo_btn.setText(QCoreApplication.translate("AssemblyAdjusterMain", u"Undo", None))
        self.refresh_btn.setText(QCoreApplication.translate("AssemblyAdjusterMain", u"Refresh", None))
        self.mod_btn.setText(QCoreApplication.translate("AssemblyAdjusterMain", u"Modify", None))
        self.label_4.setText(QCoreApplication.translate("AssemblyAdjusterMain", u"Target block id:", None))
        self.label_7.setText(QCoreApplication.translate("AssemblyAdjusterMain", u"Operations:", None))
    # retranslateUi

