class Adjuster:

    def __init__(self):
        pass

    @staticmethod
    def get_gene_ctg(chr_list, sp, ep):
        infos = []
        for info in chr_list:
            chsp = info[0]
            chep = info[1]
            ovlp = min(chep, ep) - max(chsp, sp)
            if ovlp >= 0:
                infos.append([ovlp, info])
        if infos:
            return sorted(infos, reverse=True)[0][1]
        else:
            return []

    @staticmethod
    def trans_anno(ori_agp_db, adj_agp_db, ori_bed_db):
        adj_bed_db = {}

        cov_adj_agp_db = {}
        for chrn in adj_agp_db:
            for sp, ep, ctg, ctg_len, direct in adj_agp_db[chrn]:
                cov_adj_agp_db[ctg] = [chrn, sp, ep, ctg_len, direct]

        for gid in sorted(ori_bed_db):
            chrn, gsp, gep, gdir = ori_bed_db[gid]

            match_ctg = Adjuster.get_gene_ctg(ori_agp_db[chrn], gsp, gep)

            if not match_ctg:
                print(gid)
            else:
                csp, cep, tig, _, tdir = match_ctg
                nchrn, nsp, nep, nctg_len, ndir = cov_adj_agp_db[tig]

                if tdir == '+':
                    gts = gsp - csp + 1
                    gte = gep - csp + 1
                else:
                    gts = cep - gep + 1
                    gte = cep - gsp + 1
                if gdir == tdir:
                    gtd = '+'
                else:
                    gtd = '-'
                if ndir == '+':
                    gns = nsp + gts - 1
                    gne = nsp + gte - 1
                else:
                    gns = nep - gte + 1
                    gne = nep - gts + 1
                if gtd == ndir:
                    gnd = '+'
                else:
                    gnd = '-'
                if gns <= 0 or gne <= 0:
                    continue
                adj_bed_db[gid] = [nchrn, gns, gne, gnd]

        return adj_bed_db

    @staticmethod
    def reverse_chr(agp_list):
        adj_agp_list = []
        base = 1
        for _, _, ctg, ctg_len, direct in agp_list[::-1]:
            if direct == '+':
                direct = '-'
            else:
                direct = '+'
            adj_agp_list.append([base, base+ctg_len-1, ctg, ctg_len, direct])
            base += ctg_len+100
        return adj_agp_list

    @staticmethod
    def reverse_block(agp_list, pos):
        start_idx, _, end_idx, _ = pos
        adj_agp_list = []
        base = 1

        for _ in agp_list[:start_idx]:
            adj_agp_list.append(_)
            base += _[3]+100

        for i in range(end_idx, start_idx-1, -1):
            _, _, ctg, ctg_len, direct = agp_list[i]
            if direct == '+':
                direct = '-'
            else:
                direct = '+'
            adj_agp_list.append([base, base+ctg_len-1, ctg, ctg_len, direct])
            base += ctg_len+100

        for _ in agp_list[end_idx+1:]:
            adj_agp_list.append(_)
            base += _[3] + 100

        return adj_agp_list

    @staticmethod
    def split_block(agp_list, pos):
        start_idx, _, end_idx, _ = pos
        adj_agp_list = []
        extract_agp_list = []

        base = 1

        for _ in agp_list[:start_idx]:
            adj_agp_list.append(_)
            base += _[3] + 100

        extract_agp_list = agp_list[start_idx: end_idx+1]

        for _ in agp_list[end_idx + 1:]:
            _[0] = base
            _[1] = base+_[3]-1
            adj_agp_list.append(_)
            base += _[3] + 100

        return adj_agp_list, extract_agp_list

    @staticmethod
    def ins_term(agp_list, ins_agp_list, ins_head=True):
        adj_agp_list = []
        base = 1
        if ins_head:
            order = [ins_agp_list, agp_list]
        else:
            order = [agp_list, ins_agp_list]
        for cur_list in order:
            for _ in cur_list:
                _[0] = base
                _[1] = base+_[3]-1
                adj_agp_list.append(_)
                base += _[3]+100
        return adj_agp_list

    @staticmethod
    def ins_pos(agp_list, ins_agp_list, pos, ins_before=True):
        adj_agp_list = []
        base = 1
        if ins_before:
            ins_pos = pos[0]
            order = [agp_list[:ins_pos], ins_agp_list, agp_list[ins_pos:]]
        else:
            ins_pos = pos[2]
            order = [agp_list[:ins_pos+1], ins_agp_list, agp_list[ins_pos+1:]]
        for cur_list in order:
            for _ in cur_list:
                _[0] = base
                _[1] = base+_[3]-1
                adj_agp_list.append(_)
                base += _[3]+100
        return adj_agp_list
