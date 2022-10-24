from math import sqrt


def euc_dist(a, b):
    return sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)


class Locator:

    def __init__(self):
        self.links = []
        self.block_db = {}

    def convert_anchors(self, qry_db, ref_db, anc_list):
        link_db = {}

        for qry_gene, ref_gene in anc_list:
            if qry_gene not in qry_db or ref_gene not in ref_db:
                continue
            qchr, qsp, qep, _ = qry_db[qry_gene]
            qp = min(qsp, qep)
            schr, ssp, sep, _ = ref_db[ref_gene]
            sp = min(ssp, sep)
            if qchr not in link_db:
                link_db[qchr] = {}
            if schr not in link_db[qchr]:
                link_db[qchr][schr] = []
            link_db[qchr][schr].append([qp, sp])

        for chrx in sorted(link_db):
            for chry in sorted(link_db[chrx]):
                for x, y in sorted(link_db[chrx][chry]):
                    self.links.append([chrx, x, chry, y])

    def get_break_blocks(self, resolution):
        link_db = {}
        chr_len_db = {}
        for qchr, qp, schr, sp in self.links:
            if qchr not in link_db:
                link_db[qchr] = {}
            if schr not in link_db[qchr]:
                link_db[qchr][schr] = []
            link_db[qchr][schr].append([qp, sp])
            if qchr not in chr_len_db:
                chr_len_db[qchr] = {}
            if schr not in chr_len_db[qchr]:
                chr_len_db[qchr][schr] = [0, 0]
            if qp > chr_len_db[qchr][schr][0]:
                chr_len_db[qchr][schr][0] = qp
            if sp > chr_len_db[qchr][schr][1]:
                chr_len_db[qchr][schr][1] = sp

        for qchr in link_db:
            self.block_db[qchr] = {}
            for schr in link_db[qchr]:
                groups = []
                chr_len_merge = euc_dist([0, 0], chr_len_db[qchr][schr])
                for x, y in link_db[qchr][schr]:
                    if len(groups) == 0:
                        groups.append([[x, y]])
                    else:
                        is_add = False
                        for i in range(0, len(groups)):
                            tail_x, tail_y = groups[i][-1]
                            if euc_dist([x, y], [tail_x, tail_y]) * resolution / chr_len_merge < 1:
                                groups[i].append([x, y])
                                is_add = True
                                break
                        if not is_add:
                            groups.append([[x, y]])

                self.block_db[qchr][schr] = []
                for group in groups:
                    x = []
                    y = []
                    for i in range(0, len(group)):
                        x.append(group[i][0])
                        y.append(group[i][1])
                    min_y = min(y)
                    max_y = max(y)
                    min_index = y.index(min_y)
                    max_index = y.index(max_y)
                    min_x = x[min_index]
                    max_x = x[max_index]
                    sx, sy = group[0]
                    ex, ey = group[-1]
                    if min_x > max_x:
                        tmp = min_x
                        min_x = max_x
                        max_x = tmp
                        tmp = min_y
                        min_y = max_y
                        max_y = tmp
                    tmp_list = []
                    tmp_list.extend([sx, sy])
                    if sx < min_x < ex:
                        tmp_list.extend([min_x, min_y])
                    if sx < max_x < ex:
                        tmp_list.extend([max_x, max_y])
                    tmp_list.extend([ex, ey])
                    for i in range(0, len(tmp_list) - 2, 2):
                        self.block_db[qchr][schr].append([tmp_list[i], tmp_list[i + 1], tmp_list[i + 2], tmp_list[i + 3]])
