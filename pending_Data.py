import pandas as pd
from os import path
from os import listdir
from os.path import isfile, join

BaseDir = '/content/drive/MyDrive/Find_Pending_Icmr-master/'

mypath = BaseDir+'Icmr_Data'
file = [f for f in listdir(mypath) if isfile(join(mypath, f)) and not(f[0]=='~')]
print('Processing on ',file[0])
res=pd.read_excel(mypath+'/'+file[0],header=1,index_col="Icmr ID") 
fetchedId = [(str(l).split('/')[0]).strip() for l in list(res[' Patient ID'])]
srf = list(res[' SRF ID'][res[' SRF ID']!=' '])

mypath = BaseDir+'DataFolder'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) and not(f[0]=='~')]

for file in onlyfiles:
    print('Processing on ',file)
    df = pd.read_excel(mypath+'/'+file,header=1,index_col="S.NO")
    df = df[(~df['COVID NUMBER'].isin(fetchedId)) & (~df['SRF ID'].isin(srf))]
    writer = pd.ExcelWriter('/content/drive/MyDrive/Find_Pending_Icmr-master/Icmr_Pending/'+file)
    df.to_excel(writer, sheet_name='Sheet1')
    writer.save()
