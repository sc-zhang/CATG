# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'file_loader_dialogtGRscx.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_FileLoaderDialog(object):
    def setupUi(self, FileLoaderDialog):
        if not FileLoaderDialog.objectName():
            FileLoaderDialog.setObjectName(u"FileLoaderDialog")
        FileLoaderDialog.resize(640, 250)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FileLoaderDialog.sizePolicy().hasHeightForWidth())
        FileLoaderDialog.setSizePolicy(sizePolicy)
        FileLoaderDialog.setMinimumSize(QSize(640, 250))
        FileLoaderDialog.setMaximumSize(QSize(640, 250))
        self.verticalLayout = QVBoxLayout(FileLoaderDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(FileLoaderDialog)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.qry_bed_text = QLineEdit(FileLoaderDialog)
        self.qry_bed_text.setObjectName(u"qry_bed_text")
        self.qry_bed_text.setMinimumSize(QSize(0, 0))
        self.qry_bed_text.setDragEnabled(True)

        self.gridLayout.addWidget(self.qry_bed_text, 0, 1, 1, 1)

        self.qry_bed_btn = QPushButton(FileLoaderDialog)
        self.qry_bed_btn.setObjectName(u"qry_bed_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.qry_bed_btn.sizePolicy().hasHeightForWidth())
        self.qry_bed_btn.setSizePolicy(sizePolicy2)
        self.qry_bed_btn.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.qry_bed_btn, 0, 2, 1, 1)

        self.label_2 = QLabel(FileLoaderDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.ref_bed_text = QLineEdit(FileLoaderDialog)
        self.ref_bed_text.setObjectName(u"ref_bed_text")
        self.ref_bed_text.setMinimumSize(QSize(0, 0))
        self.ref_bed_text.setDragEnabled(True)

        self.gridLayout.addWidget(self.ref_bed_text, 1, 1, 1, 1)

        self.ref_bed_btn = QPushButton(FileLoaderDialog)
        self.ref_bed_btn.setObjectName(u"ref_bed_btn")
        sizePolicy2.setHeightForWidth(self.ref_bed_btn.sizePolicy().hasHeightForWidth())
        self.ref_bed_btn.setSizePolicy(sizePolicy2)
        self.ref_bed_btn.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.ref_bed_btn, 1, 2, 1, 1)

        self.label_3 = QLabel(FileLoaderDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.anchors_text = QLineEdit(FileLoaderDialog)
        self.anchors_text.setObjectName(u"anchors_text")
        self.anchors_text.setMinimumSize(QSize(0, 0))
        self.anchors_text.setDragEnabled(True)

        self.gridLayout.addWidget(self.anchors_text, 2, 1, 1, 1)

        self.anchors_btn = QPushButton(FileLoaderDialog)
        self.anchors_btn.setObjectName(u"anchors_btn")
        sizePolicy2.setHeightForWidth(self.anchors_btn.sizePolicy().hasHeightForWidth())
        self.anchors_btn.setSizePolicy(sizePolicy2)
        self.anchors_btn.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.anchors_btn, 2, 2, 1, 1)

        self.label_4 = QLabel(FileLoaderDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.qry_agp_text = QLineEdit(FileLoaderDialog)
        self.qry_agp_text.setObjectName(u"qry_agp_text")
        self.qry_agp_text.setMinimumSize(QSize(0, 0))
        self.qry_agp_text.setDragEnabled(True)

        self.gridLayout.addWidget(self.qry_agp_text, 3, 1, 1, 1)

        self.qry_agp_btn = QPushButton(FileLoaderDialog)
        self.qry_agp_btn.setObjectName(u"qry_agp_btn")
        sizePolicy2.setHeightForWidth(self.qry_agp_btn.sizePolicy().hasHeightForWidth())
        self.qry_agp_btn.setSizePolicy(sizePolicy2)
        self.qry_agp_btn.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.qry_agp_btn, 3, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.check_btn = QDialogButtonBox(FileLoaderDialog)
        self.check_btn.setObjectName(u"check_btn")
        self.check_btn.setOrientation(Qt.Horizontal)
        self.check_btn.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.check_btn)


        self.retranslateUi(FileLoaderDialog)
        self.check_btn.accepted.connect(FileLoaderDialog.accept)
        self.check_btn.rejected.connect(FileLoaderDialog.reject)

        QMetaObject.connectSlotsByName(FileLoaderDialog)
    # setupUi

    def retranslateUi(self, FileLoaderDialog):
        FileLoaderDialog.setWindowTitle(QCoreApplication.translate("FileLoaderDialog", u"File loader", None))
        self.label.setText(QCoreApplication.translate("FileLoaderDialog", u"Query bed file:", None))
        self.qry_bed_btn.setText(QCoreApplication.translate("FileLoaderDialog", u"...", None))
        self.label_2.setText(QCoreApplication.translate("FileLoaderDialog", u"Reference bed file:", None))
        self.ref_bed_btn.setText(QCoreApplication.translate("FileLoaderDialog", u"...", None))
        self.label_3.setText(QCoreApplication.translate("FileLoaderDialog", u"Anchors file:", None))
        self.anchors_btn.setText(QCoreApplication.translate("FileLoaderDialog", u"...", None))
        self.label_4.setText(QCoreApplication.translate("FileLoaderDialog", u"Query AGP file:", None))
        self.qry_agp_btn.setText(QCoreApplication.translate("FileLoaderDialog", u"...", None))
    # retranslateUi

