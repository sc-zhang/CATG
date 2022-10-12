from os import path
from coll_asm_adj_gui.windows import file_loader_dialog
from coll_asm_adj_gui.io import file_reader, resources_loader
from coll_asm_adj_gui.adjuster import locator, vis, adjuster
from copy import deepcopy
from PySide2.QtWidgets import QWidget, QLabel, QGraphicsScene, QFileDialog
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile


class AssemblyAdjusterMain(QWidget):

    def __init__(self):
        super(AssemblyAdjusterMain, self).__init__()
        self.ui = None
        self.main_window = None
        self.statusbar_label = None
        self.graph_scene = None

        self.qry_bed_file = ""
        self.ref_bed_file = ""
        self.anchors_file = ""
        self.qry_agp_file = ""
        self.qry_name = ""
        self.ref_name = ""
        self.pic = ""

        self.qry_bed_reader = file_reader.Reader()
        self.ref_bed_reader = file_reader.Reader()
        self.anchors_reader = file_reader.Reader()
        self.qry_agp_reader = file_reader.Reader()

        self.qry_chr_list = []
        self.qry_blk_list = []

        self.qry_bed_db = None
        self.ref_bed_db = None
        self.gene_pairs = None
        self.qry_agp_db = None
        self.block_regions = None
        self.block_list_db = None

        self.graph_viewer = vis.VisContent()

        self.adjuster = adjuster.Adjuster()

        self.init_ui()

    def init_ui(self):
        main_ui_file = resources_loader.resource_path("coll_asm_adj_gui/ui/assembly_adjuster_main.ui")
        qfile_file_loader = QFile(main_ui_file)
        qfile_file_loader.open(QFile.ReadOnly)
        qfile_file_loader.close()

        self.ui = QUiLoader().load(qfile_file_loader)
        self.ui.file_loader_btn.clicked.connect(self.load_files)
        self.ui.file_save_btn.clicked.connect(self.save_files)
        self.ui.refresh_btn.clicked.connect(self.show_pic)
        self.ui.mod_btn.clicked.connect(self.modify)
        self.ui.src_chr_cbox.currentTextChanged.connect(self.__add_src_blks)
        self.ui.tgt_chr_cbox.currentTextChanged.connect(self.__add_tgt_blks)

        self.statusbar_label = QLabel("Ready.")
        self.ui.statusbar.addWidget(self.statusbar_label)

    def load_files(self):
        self.statusbar_label.setText("Loading files...")
        file_loader = file_loader_dialog.FileLoaderDialog(self)
        file_loader.show()
        file_loader.signal_path.connect(self.get_file_path)

    def save_files(self):
        self.statusbar_label.setText("Saving tours")
        folder_path = QFileDialog.getExistingDirectory(self.ui, "Select folder")
        if folder_path and path.isdir(folder_path):
            for chrn in self.qry_agp_db:
                tour_file = path.join(folder_path, '%s.tour' % chrn)
                with open(tour_file, 'w') as fout:
                    tour_list = []
                    for _, _, ctg, _, direct in self.qry_agp_db[chrn]:
                        tour_list.append("%s%s" % (ctg, direct))
                    fout.write("%s" % ' '.join(tour_list))
        self.statusbar_label.setText("Success")

    def show_pic(self):
        blk_loc = locator.Locator()
        blk_loc.convert_anchors(self.qry_bed_db, self.ref_bed_db, self.gene_pairs)
        if self.ui.resolution_text.text():
            resolution = int(float(self.ui.resolution_text.text()))
        else:
            resolution = 20
        if resolution == 0 or resolution == 20:
            resolution = 20
            self.ui.resolution_text.setText("20")
        blk_loc.get_break_blocks(resolution)

        self.graph_viewer.gen_figure(blk_loc.links, blk_loc.block_db, self.qry_agp_db, resolution,
                                     self.qry_name, self.ref_name)

        self.block_regions = self.graph_viewer.block_regions
        self.block_list_db = self.graph_viewer.block_list_db

        self.ui.src_blk_cbox.clear()
        if self.ui.src_chr_cbox.currentText() in self.block_list_db:
            self.ui.src_blk_cbox.addItems(self.block_list_db[self.ui.src_chr_cbox.currentText()])
        self.ui.tgt_blk_cbox.clear()
        if self.ui.tgt_chr_cbox.currentText() in self.block_list_db:
            self.ui.tgt_blk_cbox.addItems(self.block_list_db[self.ui.tgt_chr_cbox.currentText()])
        if not self.graph_scene:
            self.graph_scene = QGraphicsScene()
            self.graph_scene.addWidget(self.graph_viewer.figure_content)
            self.ui.plot_viewer.setScene(self.graph_scene)
            self.ui.plot_viewer.show()
        else:
            self.graph_viewer.figure_content.draw()

    def get_file_path(self, content):
        self.qry_bed_file, self.ref_bed_file, self.anchors_file, self.qry_agp_file = content
        if path.isfile(self.qry_bed_file) and path.isfile(self.ref_bed_file) and \
                path.isfile(self.anchors_file) and path.isfile(self.qry_agp_file):
            self.__enable_controls()
            self.__load_file()
            self.__add_options()
            self.show_pic()

            self.statusbar_label.setText("All file loaded.")
        else:
            self.statusbar_label.setText("Not all files selected.")

    def modify(self):
        self.ui.mod_btn.setEnabled(False)
        src_chr = self.ui.src_chr_cbox.currentText()
        src_blk = int(self.ui.src_blk_cbox.currentText()) - 1
        tgt_chr = self.ui.tgt_chr_cbox.currentText()
        tgt_blk = int(self.ui.tgt_blk_cbox.currentText()) - 1
        opt = self.ui.method_cbox.currentText()
        is_rev = self.ui.rev_chk.isChecked()

        if opt == "Source chromosome" and is_rev:
            self.statusbar_label.setText("Reversing chromosome: %s" % src_chr)
            tmp_dict = deepcopy(self.qry_agp_db)
            tmp_dict[src_chr] = self.adjuster.reverse_chr(tmp_dict[src_chr])
            self.qry_bed_db = self.adjuster.trans_anno(self.qry_agp_db, tmp_dict, self.qry_bed_db)
            self.qry_agp_db = deepcopy(tmp_dict)
            del tmp_dict
        elif opt == "Source block" and is_rev:
            self.statusbar_label.setText("Reversing block: %s %s" % (src_chr, src_blk))
            tmp_dict = deepcopy(self.qry_agp_db)
            tmp_dict[src_chr] = self.adjuster.reverse_block(tmp_dict[src_chr], self.block_regions[src_blk])
            self.qry_bed_db = self.adjuster.trans_anno(self.qry_agp_db, tmp_dict, self.qry_bed_db)
            self.qry_agp_db = deepcopy(tmp_dict)
            del tmp_dict
        elif opt == "Insert head":
            self.statusbar_label.setText("Inserting chromosome %s to %s's head" % (src_chr, tgt_chr))
            tmp_dict = deepcopy(self.qry_agp_db)
            tmp_dict[src_chr], extract_agp_list = self.adjuster.split_block(tmp_dict[src_chr],
                                                                            self.block_regions[src_blk])
            if is_rev:
                extract_agp_list = self.adjuster.reverse_chr(extract_agp_list)

            tmp_dict[tgt_chr] = self.adjuster.ins_term(tmp_dict[tgt_chr], extract_agp_list)
            self.qry_bed_db = self.adjuster.trans_anno(self.qry_agp_db, tmp_dict, self.qry_bed_db)
            self.qry_agp_db = deepcopy(tmp_dict)
            del tmp_dict
        elif opt == "Insert tail":
            self.statusbar_label.setText("Inserting chromosome %s to %s's tail" % (src_chr, tgt_chr))
            tmp_dict = deepcopy(self.qry_agp_db)
            tmp_dict[src_chr], extract_agp_list = self.adjuster.split_block(tmp_dict[src_chr],
                                                                            self.block_regions[src_blk])
            if is_rev:
                extract_agp_list = self.adjuster.reverse_chr(extract_agp_list)

            tmp_dict[tgt_chr] = self.adjuster.ins_term(tmp_dict[tgt_chr], extract_agp_list, False)
            self.qry_bed_db = self.adjuster.trans_anno(self.qry_agp_db, tmp_dict, self.qry_bed_db)
            self.qry_agp_db = deepcopy(tmp_dict)
            del tmp_dict
        elif opt == "Insert before":
            self.statusbar_label.setText("Inserting block %s %s before %s %s" % (src_chr, src_blk, tgt_chr, tgt_blk))
            tmp_dict = deepcopy(self.qry_agp_db)
            tmp_dict[src_chr], extract_agp_list = self.adjuster.split_block(tmp_dict[src_chr],
                                                                            self.block_regions[src_blk])
            if is_rev:
                extract_agp_list = self.adjuster.reverse_chr(extract_agp_list)

            tmp_dict[tgt_chr] = self.adjuster.ins_pos(tmp_dict[tgt_chr], extract_agp_list, self.block_regions[tgt_blk])
            self.qry_bed_db = self.adjuster.trans_anno(self.qry_agp_db, tmp_dict, self.qry_bed_db)
            self.qry_agp_db = deepcopy(tmp_dict)
            del tmp_dict
        elif opt == "Insert after":
            self.statusbar_label.setText("Inserting block %s %s after %s %s" % (src_chr, src_blk, tgt_chr, tgt_blk))
            tmp_dict = deepcopy(self.qry_agp_db)
            tmp_dict[src_chr], extract_agp_list = self.adjuster.split_block(tmp_dict[src_chr],
                                                                            self.block_regions[src_blk])
            if is_rev:
                extract_agp_list = self.adjuster.reverse_chr(extract_agp_list)

            tmp_dict[tgt_chr] = self.adjuster.ins_pos(tmp_dict[tgt_chr], extract_agp_list, self.block_regions[tgt_blk],
                                                      False)
            self.qry_bed_db = self.adjuster.trans_anno(self.qry_agp_db, tmp_dict, self.qry_bed_db)
            self.qry_agp_db = deepcopy(tmp_dict)
            del tmp_dict

        self.show_pic()
        self.ui.mod_btn.setEnabled(True)
        self.statusbar_label.setText("Success")

    def __load_file(self):
        self.qry_bed_reader.read_bed(self.qry_bed_file)
        self.ref_bed_reader.read_bed(self.ref_bed_file)
        self.anchors_reader.read_anchors(self.anchors_file)
        self.qry_agp_reader.read_agp(self.qry_agp_file)

        if '/' in self.qry_bed_file:
            sep = '/'
        else:
            sep = '\\'
        self.qry_name = self.qry_bed_file.split(sep)[-1].split('.')[0]
        self.ref_name = self.ref_bed_file.split(sep)[-1].split('.')[0]

        self.qry_bed_db = self.qry_bed_reader.dict
        self.ref_bed_db = self.ref_bed_reader.dict
        self.gene_pairs = self.anchors_reader.gene_pairs
        self.qry_agp_db = self.qry_agp_reader.dict

    def __enable_controls(self):
        self.ui.file_save_btn.setEnabled(True)
        self.ui.mod_btn.setEnabled(True)
        self.ui.refresh_btn.setEnabled(True)
        self.ui.src_chr_cbox.setEnabled(True)
        self.ui.src_blk_cbox.setEnabled(True)
        self.ui.tgt_chr_cbox.setEnabled(True)
        self.ui.tgt_blk_cbox.setEnabled(True)
        self.ui.method_cbox.setEnabled(True)
        self.ui.rev_chk.setEnabled(True)

    def __add_options(self):
        self.ui.src_chr_cbox.addItems(self.qry_bed_reader.chr_list)
        self.ui.tgt_chr_cbox.addItems(self.qry_bed_reader.chr_list)

    def __add_src_blks(self, value):
        self.ui.src_blk_cbox.clear()
        if self.block_list_db and value in self.block_list_db:
            self.ui.src_blk_cbox.addItems(self.block_list_db[value])

    def __add_tgt_blks(self, value):
        self.ui.tgt_blk_cbox.clear()
        if self.block_list_db and value in self.block_list_db:
            self.ui.tgt_blk_cbox.addItems(self.block_list_db[value])

    def show(self):
        self.ui.show()
