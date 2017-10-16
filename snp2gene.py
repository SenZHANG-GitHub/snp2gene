import pdb
from itertools import islice
nslice = 20 

"""
## Leave all these annoying stuff to clean_gene.py

def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def getGeneChr(strchr):
    if strchr.find("_") >= 0:
        strchr =  strchr.split("_")[0]
        """ 

def isingene(genechr, snpchr, genestart, geneend, snpbp):
    if snpchr < genechr:
        return -1
    elif snpchr == genechr:
        if snpbp < genestart:
            return -1
        elif genestart <= snpbp <= geneend:
            return 0
        elif snpbp > geneend:
            return 1
        else:
            print("err1")
    elif snpchr > genechr:
        return 1
    else:
        print("err2")

genename = "cleaned_genes.txt"
mapname  = "CUHK_HKDRGWA_6445CC_Clean_Ch1-22.map"
resultname = "genes_snps.txt"
noemptyresname = "genes_snps_noempty.txt"

genefile = open(genename, mode = "r")
mapfile  = open(mapname, mode = "r")
outfile = open(resultname, mode = "w")
outfile2 = open(noemptyresname, mode = 'w')
genelist = []
snplist  = []

while True:
    next_n_lines = list(islice(genefile, nslice))
    if not next_n_lines:
        break

    for line in next_n_lines:
        if len(line) == 0:
            continue
        genelist.append(line.split()[:-1])

genefile.close()
print("Finished reading ucsc genes file: " + genename + '\n')

while True:
    next_n_lines = list(islice(mapfile, nslice))
    if not next_n_lines:
        break

    for line in next_n_lines:
        if len(line) == 0:
            continue
        snplist.append([line.split()[i] for i in [0, 1, 3]])        

mapfile.close()
print("Finished reading .map file" + mapname + '\n')

# i is the index for genelist (e.g. 30000+)
# j is the index for snplist  (e.g. 1250000+) 
i = 0
j = 0
numsnp = len(snplist)
numgene = len(genelist)

while True:
    if j >= numsnp or i >= numgene:
        print("i = " + str(i) + ", j = "+ str(j))
        break

    bpchr   = int(genelist[i][0])
    bpstart = int(genelist[i][1])
    bpend   = int(genelist[i][2])

    snpchr  = int(snplist[j][0])
    snpbp   = int(snplist[j][2])

    #pdb.set_trace()

    if isingene(bpchr, snpchr, bpstart, bpend, snpbp) == -1: 
    # (snpchr < bpchr) or (snpchr == bpchr and snpbp < bpstart)
        j += 1
        if j >= numsnp:
            print('----------------------------------------')
            print("i = " + str(i) + ", j = "+ str(j))
            print("isingene(): "+str(isingene(bpchr, snpchr, bpstart, bpend, snpbp)))
            print("Gene info: , ".join(genelist[i][:3]))
            print("snp info: , "+snplist[j-1][0]+", "+snplist[j-1][2])
            print('----------------------------------------')
            break


    elif isingene(bpchr, snpchr, bpstart, bpend, snpbp) == 0:
    # (snpchr == bpchr) and (bpstart <= snpbp <= bpend)
        genelist[i].append(snplist[j][1])
        j += 1
        if j >= numsnp:
            print('----------------------------------------')
            print("i = " + str(i) + ", j = "+ str(j))
            print("isingene(): "+str(isingene(bpchr, snpchr, bpstart, bpend, snpbp)))
            print("Gene info: , ".join(genelist[i][:3]))
            print("snp info: , "+snplist[j-1][0]+", "+snplist[j-1][2])
            print('----------------------------------------')
            break

    elif isingene(bpchr, snpchr, bpstart, bpend, snpbp) == 1:
    # (snpchr > bpchr) or (snpchr == bpchr and snpbp> bpend)
        i += 1
        if i >= numgene:
            print('----------------------------------------')
            print("i = " + str(i) + ", j = "+ str(j))
            print("isingene(): "+str(isingene(bpchr, snpchr, bpstart, bpend, snpbp)))
            print("Gene info: , ".join(genelist[i-1][:3]))
            print("snp info: , "+snplist[j][0]+", "+snplist[j][2])
            print('----------------------------------------')
            break
    else:
        print("err3")


print("Finished the snp -> gene mapping\n")

ncnt = 0
for gene in genelist:
    outfile.write('\t'.join(gene[0:5]) + '\t' + str(len(gene)-5)+'\t' + '\t'.join(gene[5:]) + '\n')

    if len(gene)-5 > 0:
        outfile2.write('\t'.join(gene[0:5]) + '\t' + str(len(gene)-5)+'\t' + '\t'.join(gene[5:]) + '\n')
        ncnt += 1
outfile.close()
outfile2.close()
print("Non-empty genes: "+str(ncnt))
print("Finished writing the result file: " + resultname + '\n')
print("Finished writing the result file: " + noemptyresname + '\n')

























