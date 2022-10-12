from PySide2.QtWidgets import QDialog, QFileDialog, QDialogButtonBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile, Signal


class FileLoaderDialog(QDialog):

    signal_path = Signal(list)

    def __init__(self, parent=None):
        super(FileLoaderDialog, self).__init__(parent)
        self.qry_bed_file = ""
        self.ref_bed_file = ""
        self.anchors_file = ""
        self.qry_agp_file = ""
        self.ui = None
        self.init_ui()

    def init_ui(self):
        qfile_file_loader = QFile("coll_asm_adj_gui/ui/file_loader_dialog.ui")
        qfile_file_loader.open(QFile.ReadOnly)
        qfile_file_loader.close()

        self.ui = QUiLoader().load(qfile_file_loader)
        self.ui.qry_bed_btn.clicked.connect(self.load_qry_bed)
        self.ui.ref_bed_btn.clicked.connect(self.load_ref_bed)
        self.ui.anchors_btn.clicked.connect(self.load_anchors)
        self.ui.qry_agp_btn.clicked.connect(self.load_qry_agp)
        self.ui.check_btn.button(QDialogButtonBox.Ok).clicked.connect(self.send_path)

    def load_qry_bed(self):
        self.qry_bed_file = QFileDialog.getOpenFileName(self.ui, "Select query bed file",
                                                        filter="bed file(*.bed)")[0]
        self.ui.qry_bed_text.setText(self.qry_bed_file)

    def load_ref_bed(self):
        self.ref_bed_file = QFileDialog.getOpenFileName(self.ui, "Select reference bed file",
                                                        filter="bed file(*.bed)")[0]
        self.ui.ref_bed_text.setText(self.ref_bed_file)

    def load_anchors(self):
        self.anchors_file = QFileDialog.getOpenFileName(self.ui, "Select anchors file",
                                                        filter="anchors file(*.anchors)")[0]
        self.ui.anchors_text.setText(self.anchors_file)

    def load_qry_agp(self):
        self.qry_agp_file = QFileDialog.getOpenFileName(self.ui, "Select query agp file",
                                                        filter="agp file(*.agp)")[0]
        self.ui.qry_agp_text.setText(self.qry_agp_file)

    def send_path(self):
        self.qry_bed_file = self.ui.qry_bed_text.text()
        self.ref_bed_file = self.ui.ref_bed_text.text()
        self.anchors_file = self.ui.anchors_text.text()
        self.qry_agp_file = self.ui.qry_agp_text.text()
        content = [self.qry_bed_file, self.ref_bed_file, self.anchors_file, self.qry_agp_file]
        self.signal_path.emit(content)

    def show(self):
        self.ui.show()
