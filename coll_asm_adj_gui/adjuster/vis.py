import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

matplotlib.use("qt5agg")
from coll_asm_adj_gui.adjuster.locator import euc_dist


class VisCanvas(FigureCanvas):

    def __init__(self, parent=None):
        fig = plt.figure(figsize=(10, 10), dpi=300, tight_layout=True, facecolor="#FFF2E2")
        self.plt = plt
        super(VisCanvas, self).__init__(fig)


class VisContent:

    def __init__(self):
        self.chr_list_x = []
        self.chr_list_y = []
        self.block_list_db = {}
        self.block_detail = []
        self.data_db = {}
        self.block_regions = []
        self.figure_content = VisCanvas()

    def convert_link(self, links):
        chr_set_x = set()
        chr_set_y = set()
        self.data_db = {}
        for chr_x, pos_x, chr_y, pos_y in links:
            chr_set_x.add(chr_x)
            chr_set_y.add(chr_y)
            if chr_x not in self.data_db:
                self.data_db[chr_x] = {}
            if chr_y not in self.data_db[chr_x]:
                self.data_db[chr_x][chr_y] = []
            self.data_db[chr_x][chr_y].append([pos_x, pos_y])

        self.chr_list_x = sorted(chr_set_x)
        self.chr_list_y = sorted(chr_set_y)

    @staticmethod
    def __get_ctg_pos(region, pos):
        s = 0
        e = len(region) - 1
        while s <= e:
            mid = int((s + e) / 2)
            if region[mid][0] > pos:
                e = mid - 1
            elif region[mid][0] < pos:
                s = mid + 1
            else:
                return mid
        if region[e][1] >= pos:
            return e
        elif e == len(region) - 1:
            return e
        else:
            return -1

    def gen_figure(self, links, block_db, agp_db, resolution, qry_name="", ref_name=""):
        self.convert_link(links)
        chr_len_db = {}

        for chrx in self.chr_list_x:
            if chrx not in chr_len_db:
                chr_len_db[chrx] = 0
            for chry in self.chr_list_y:
                if chry not in chr_len_db:
                    chr_len_db[chry] = 0
                if chry not in self.data_db[chrx]:
                    continue
                for x, y in self.data_db[chrx][chry]:
                    if x > chr_len_db[chrx]:
                        chr_len_db[chrx] = x
                    if y > chr_len_db[chry]:
                        chr_len_db[chry] = y
        base_x = 0
        base_y = 0
        offset_db = {}
        for chrx in self.chr_list_x:
            offset_db[chrx] = base_x
            base_x += chr_len_db[chrx]
        for chry in self.chr_list_y:
            offset_db[chry] = base_y
            base_y += chr_len_db[chry]

        data_x = []
        data_y = []
        for chrx in self.chr_list_x:
            for chry in self.chr_list_y:
                if chry not in self.data_db[chrx]:
                    continue
                for x, y in self.data_db[chrx][chry]:
                    data_x.append(x + offset_db[chrx])
                    data_y.append(y + offset_db[chry])

        block_x = []
        block_y = []

        idx = 0

        self.block_list_db = {}
        self.block_detail = []
        self.block_regions = []

        for chrx in self.chr_list_x:
            for chry in self.chr_list_y:
                if chrx not in block_db or chry not in block_db[chrx]:
                    continue
                for x1, y1, x2, y2 in block_db[chrx][chry]:
                    if euc_dist([x1, y1], [x2, y2]) * 1. * resolution / \
                            euc_dist([0, 0], [chr_len_db[chrx], chr_len_db[chry]]) < 1:
                        continue

                    idx += 1
                    if chrx not in self.block_list_db:
                        self.block_list_db[chrx] = []
                    self.block_list_db[chrx].append(str(idx))

                    block_x.append([x1 + offset_db[chrx], x2 + offset_db[chrx]])
                    rstart = self.__get_ctg_pos(agp_db[chrx], x1)
                    rend = self.__get_ctg_pos(agp_db[chrx], x2)
                    if rstart == -1 or rend == -1:
                        continue
                    self.block_detail.append([])
                    for _ in range(rstart, rend+1):
                        self.block_detail[-1].append(agp_db[chrx][_][2])
                    ctg1 = agp_db[chrx][rstart][2]
                    ctg2 = agp_db[chrx][rend][2]
                    self.block_regions.append([rstart, ctg1, rend, ctg2])
                    block_y.append([y1 + offset_db[chry], y2 + offset_db[chry]])

        max_x = 0
        max_y = 0
        for chrx in self.chr_list_x:
            max_x += chr_len_db[chrx]

        for chry in self.chr_list_y:
            max_y += chr_len_db[chry]

        x_ticks = []
        x_labels = []
        base_x = 0
        chrx_idx_db = {}
        idx = 0
        offset_x_list = []

        self.figure_content.plt.clf()

        for chrx in self.chr_list_x:
            offset_x_list.append(base_x)
            chrx_idx_db[chrx] = idx
            idx += 1
            self.figure_content.plt.plot([chr_len_db[chrx] + base_x, chr_len_db[chrx] + base_x], [0, max_y],
                                         linestyle='-',
                                         color='green',
                                         linewidth=0.5, markersize=0)
            x_ticks.append(base_x + int(chr_len_db[chrx] / 2))
            x_labels.append(chrx)
            base_x += chr_len_db[chrx]
        offset_x_list.append(base_x)

        y_ticks = []
        y_labels = []
        base_y = 0
        chry_idx_db = {}
        idx = 0
        offset_y_list = []

        for chry in self.chr_list_y:
            offset_y_list.append(base_y)
            chry_idx_db[chry] = idx
            idx += 1
            self.figure_content.plt.plot([0, max_x], [chr_len_db[chry] + base_y, chr_len_db[chry] + base_y],
                                         linestyle='-',
                                         color='green',
                                         linewidth=0.5, markersize=0)
            y_ticks.append(base_y + int(chr_len_db[chry] / 2))
            y_labels.append(chry)
            base_y += chr_len_db[chry]
        offset_y_list.append(base_y)

        self.figure_content.plt.plot(data_x, data_y, linestyle='', color='black', marker='o', markersize=0.5)

        for i in range(0, len(block_x)):
            block_pos = [(block_x[i][0] + block_x[i][1]) / 2.0, (block_y[i][0] + block_y[i][1]) / 2.0]

            self.figure_content.plt.plot(block_x[i], block_y[i], linestyle='-', color='orange', linewidth=0.5,
                                         markersize=0)
            self.figure_content.plt.annotate(i+1,
                                             xy=block_pos,
                                             bbox=dict(
                                                 boxstyle="circle,pad=0",
                                                 fc="white",
                                                 ec="black",
                                                 alpha=0.5,
                                                 lw=1
                                             ),
                                             fontsize=8, color='blue', ha='right')

        self.figure_content.plt.xlim([0, max_x])
        self.figure_content.plt.ylim([0, max_y])
        self.figure_content.plt.xticks(x_ticks)
        self.figure_content.plt.yticks(y_ticks)
        self.figure_content.plt.xlabel(qry_name)
        self.figure_content.plt.ylabel(ref_name)
        ax = self.figure_content.plt.gca()
        ax.set_facecolor("#FFF2E2")
        ax.set_xticklabels(x_labels, rotation=45)
        ax.set_yticklabels(y_labels, rotation=0)
        ax.xaxis.set_ticks_position('top')
        ax.yaxis.set_ticks_position('right')
        ax.invert_yaxis()
        ax.tick_params(top=False, right=False)
