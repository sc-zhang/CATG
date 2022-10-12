class Reader:

    def __init__(self):
        self.chr_list = []
        self.gene_pairs = []
        self.dict = {}

    def read_bed(self, bed_file):
        chr_set = set()
        with open(bed_file, 'r') as fin:
            for line in fin:
                data = line.strip().split()
                chrn = data[0]
                chr_set.add(chrn)
                sp = int(data[1])
                ep = int(data[2])
                direct = '+'
                if sp > ep:
                    sp, ep = ep, sp
                    direct = '-'
                gene = data[3]
                self.dict[gene] = [chrn, sp, ep, direct]
        self.chr_list = sorted(chr_set)

    def read_agp(self, in_agp):
        idx = 0
        with open(in_agp, 'r') as fin:
            for line in fin:
                data = line.strip().split()
                if len(line.strip()) == 0 or line[0] == '#' or data[4] == 'U':
                    continue
                chr_x = data[0]
                sp = int(float(data[1]))
                ep = int(float(data[2]))
                ctg = data[5]
                ctg_len = int(data[7])
                direct = data[-1]
                if chr_x not in self.dict:
                    self.dict[chr_x] = []
                self.dict[chr_x].append([sp, ep, ctg, ctg_len, direct])

    def read_anchors(self, in_anchors):
        with open(in_anchors, 'r') as fin:
            for line in fin:
                if len(line.strip()) == 0 or line[0] == '#':
                    continue
                data = line.strip().split()
                self.gene_pairs.append([data[0], data[1]])
