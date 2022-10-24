class Reader:

    def __init__(self):
        pass

    @staticmethod
    def read_bed(bed_file):
        dict = {}
        chr_set = set()
        with open(bed_file, 'r') as fin:
            for line in fin:
                if len(line.strip()) == 0 or line[0] == '#':
                    continue
                data = line.strip().split()
                if len(data) < 4:
                    continue
                chrn = data[0]
                chr_set.add(chrn)
                try:
                    sp = int(data[1])
                    ep = int(data[2])
                except ValueError:
                    return None, None
                direct = '+'
                if sp > ep:
                    sp, ep = ep, sp
                    direct = '-'
                gene = data[3]
                dict[gene] = [chrn, sp, ep, direct]
        return sorted(chr_set), dict

    @staticmethod
    def read_agp(in_agp):
        dict = {}
        with open(in_agp, 'r') as fin:
            for line in fin:
                data = line.strip().split()
                if len(line.strip()) == 0 or line[0] == '#' or data[4] == 'U' or len(data) < 8:
                    continue
                chr_x = data[0]
                try:
                    sp = int(float(data[1]))
                    ep = int(float(data[2]))
                    ctg_len = int(data[7])
                except ValueError:
                    return None
                ctg = data[5]
                direct = data[-1]
                if chr_x not in dict:
                    dict[chr_x] = []
                dict[chr_x].append([sp, ep, ctg, ctg_len, direct])
        return dict

    @staticmethod
    def read_anchors(in_anchors):
        gene_pairs = []
        with open(in_anchors, 'r') as fin:
            for line in fin:
                if len(line.strip()) == 0 or line[0] == '#':
                    continue
                data = line.strip().split()
                if len(data) < 2:
                    return None
                gene_pairs.append([data[0], data[1]])
        return gene_pairs
