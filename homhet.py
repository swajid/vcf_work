import pandas as pd
import numpy as np

df = pd.read_csv("vcf2.vcf", sep='\s', lineterminator='\r', skiprows=1)
# gene_name = df.head()['INFO'][1].split(';')[11].split('|')[3]
df1 = df['INFO'].str.split(';', expand=True)[11]
gene_names = df1.str.split('|', expand=True)[3]
hh = df['xxx'].str.split(',', expand=True)[0].str.split(':', expand=True)[0]

un_gn = gene_names.unique()

alt = pd.DataFrame(dict(gene_names=un_gn))
alt.insert(0, 'hom',0)
alt.insert(0, 'het',0)

numarr = alt.to_numpy()#[:,2]

het = 0
hom = 0

def getRow(un_gn, gene_name):
    """
    Get row from unique gene
    name list
    """
    return un_gn.tolist().index(gene_name)

#for gene in gene_names:
for x in range(0,len(hh)):
    if hh[x] == "1/1" or hh[x] == "0/0":
        numarr[getRow(un_gn, gene_names[x]),1]+=1
    elif hh[x] == "0/1" or hh[x] == "1/0":
        numarr[getRow(un_gn, gene_names[x]),0]+=1
print(numarr)
