import pdb
from operator import itemgetter
from itertools import islice

nslice = 20
genelist_ordered = []
genetmp_chr = []
cumchr = 1

for i in range(3):
    fname = "gene_ucsc/knowngenes_"+str(i)+".txt"
    fgene = open(fname, mode = "r")

    while True:
        next_n_lines = list(islice(fgene, nslice))
        if not next_n_lines:
            break
        
        for line in next_n_lines:
            if len(line) == 0: # Skip the empty lines
                continue 
           
            currchr = int(line.split()[0])
            if currchr != cumchr:
               genetmp_chr.sort(key = lambda x:x[1]) 
               genelist_ordered.extend(genetmp_chr)
               genetmp_chr = []
               cumchr = currchr

            genetmp_chr.append([int(x) for x in line.split()[0:2]] + line.split()[2:])


genelist_ordered.sort(key = lambda x:x[0])

outname = "cleaned_genes.txt"
fout = open(outname, mode = "w")
for gene in genelist_ordered:
    fout.write(str(gene[0]) + '\t' + str(gene[1]) + '\t' + '\t'.join(gene[2:]) + '\n')
fout.close()

















