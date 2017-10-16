from itertools import islice
import pdb
nslice = 20 

"""
def getGeneChr(strchr):
	if strchr.find("_") >= 0:
		strchr =  strchr.split("_")[0]
""" 

def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

genename = "gene_ucsc/knownCanonical.txt"
genefile = open(genename, mode = "r")

genelist = []
maxchr = 0
iclean = 0
while True:
    next_n_lines = list(islice(genefile, nslice))
    if not next_n_lines:
        break

    for line in next_n_lines:
        if len(line) == 0:
            continue

        chrstr = line.split()[0]
        if chrstr.find("_") >= 0:
        	# chrstr = chrstr.split("_")[0]
        	continue

        if not isInt(chrstr[3]):
        	continue

        chrint = int(chrstr[3:])
        if chrint > maxchr:
			maxchr = chrint
        elif chrint < maxchr:
        	outname = "gene_ucsc/knowngenes_" + str(iclean) + ".txt"
        	fout = open(outname, mode = "w")

        	for gene in genelist:
        		fout.write(' '.join(gene)+'\n')
        	fout.close()

        	genelist = []
        	maxchr = chrint
        	iclean += 1

        genelist.append([str(chrint)]+line.split()[1:])

genefile.close()


outname = "gene_ucsc/knowngenes_" + str(iclean) + ".txt"
fout = open(outname, mode = "w")

for gene in genelist:
	fout.write(' '.join(gene)+'\n')
fout.close()
















