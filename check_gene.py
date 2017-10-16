fin = open("cleaned_genes.txt", mode = "r")

tlist = []
cumchr = 1
for line in fin:
    currchr = int(line.split()[0])
    if currchr > cumchr: 
        print('--------------------------------------------------\n')
        print('Checking chr '+str(cumchr)+'...\n')
        for i in range(len(tlist)-1):
            if tlist[i+1]<tlist[i]:
                print('Found error in this chr: i='+str(i)+'\n')
                
        cumchr = currchr
        tlist = []
        
    tlist.append(int(line.split()[1]))

fin.close()
