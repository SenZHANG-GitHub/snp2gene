"""
python view_gene.py maxpairs (-show)

maxpairs: -1 (no action)
        otherwise, all gene pairs with #snp-pairs >= maxpairs will force their #snp-pairs to be maxpairs
"""
import pdb, sys
import matplotlib.pyplot as plt
import numpy as np
from itertools import islice

nslice = 20

gene_filename = 'genes_snps.txt'
genefile = open(gene_filename, mode = 'r')

# genelist: chr bpstart bpend numsnps (all are of int format)
genelist = []
genelist_out = []
while True:
    next_n_lines = list(islice(genefile, nslice))
    if not next_n_lines:
        break 

    for line in next_n_lines:
        if int(line.split()[5]) > 0:
            genelist.append([int(line.split()[i]) for i in [0,1,2,5]])
            genelist_out.append(line)

genefile.close()

"""
outname = 'genes_snps_noempty.txt'
fout = open(outname, mode = 'w')
for gene in genelist_out:
    fout.write(gene)
fout.close()
"""
print('--------------------------------------------------')

numsnps_list = [x[3] for x in genelist]
genelen_list = [(x[2]-x[1])/1000.0 for x in genelist]

print('total number of non-empty genes: '+str(len(genelist)))
print('mean number of snps within a gene: '+str(np.mean(numsnps_list)))
print('median number of snps within a gene: '+str(np.median(numsnps_list)))
print('max number of snps within a gene: '+str(max(numsnps_list)))
print('min number of snps within a gene: '+str(min(numsnps_list)))
print('--------------------------------------------------')
print('mean range of a gene: '+str(np.mean(genelen_list))+' kbp')
print('median range of a gene: '+str(np.median(genelen_list))+' kbp')
print('max range of a gene: '+str(max(genelen_list))+' kbp')
print('min range of a gene: '+str(min(genelen_list))+' kbp')
print('--------------------------------------------------')

pdb.set_trace()
"""
plt.figure(1)
plt.hist(numsnps_list, bins = 'auto')
plt.title('Number of snps within a gene')
plt.figure(2)
plt.hist(genelen_list, bins = 'auto')
plt.title('Length of a gene (unit: kbp)')
plt.show()

interLen = []
nummax = 0
if len(sys.argv)>=2:
    maxpairs = int(sys.argv[1])
else:
    maxpairs = -1

target_pair = 16000
buff = 5
flag = False

for i in range(len(genelist)):
    for j in range(i+1, len(genelist)):
        numpairs = genelist[i][3]*genelist[j][3]
        if maxpairs == -1:
            interLen.append(numpairs)
        else:
            if numpairs >= maxpairs:
                interLen.append(maxpairs)
                nummax += 1
            else:
                interLen.append(numpairs)
        if flag and target_pair-buff < numpairs < target_pair+buff:
            flag = False
            print('--------------------------------------------------')
            print('i: '+str(i)+',  j: '+str(j))
            print('number of snp pairs: '+str(numpairs))
            print('--------------------------------------------------')
            flag = False
            fout1 = open('locipair_'+str(numpairs)+'.set', mode = 'w')
            fout1.write('SET_1\n')
            fout1.write('\n'.join(genelist_out[i].split()[6:]))
            fout1.write('\nEND\n\nSET_2\n')
            fout1.write('\n'.join(genelist_out[j].split()[6:]))
            fout1.write('\nEND\n')
            fout1.close()
            

print('--------------------------------------------------')
print('total number of gene-gene pairs: '+str(len(interLen)))
#print('mean number of snp-pairs within a gene-pair: '+str(np.mean(interLen)))
#print('median number of snp-pairs within a gene-pair: '+str(np.median(interLen)))
#print('max number of snp-pairs within a gene-pair: '+str(max(interLen)))
if not maxpairs == -1:
    print('number of max(>= '+str(maxpairs)+') gene-gene pairs: '+str(nummax)+'('+'{:.2f}'.format(float(100*nummax/len(interLen)))+'%)') 
#print('min number of snp-pairs within a gene-pair: '+str(min(interLen)))
print('--------------------------------------------------')

if len(sys.argv)==3 and sys.argv[2]=='-show':    
    plt.hist([x[3] for x in genelist], bins='auto')
    plt.title('Histogram for the number of snps within a gene')
    plt.show()
    
    plt.hist(interLen, bins='auto')
    plt.title('Histogram for the number of snp-snp pairs within a gene-gene pair')
    plt.show()



"""




