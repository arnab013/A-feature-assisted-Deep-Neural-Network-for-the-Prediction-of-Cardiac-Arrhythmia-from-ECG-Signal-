# -*- coding: utf-8 -*-
"""10646_ECGDATA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cH9_9vASNYgXuPjF7d4g1nymyhYJ5752
"""

"""from google.colab import drive
drive.mount('/content/gdrive')"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm
import os
import glob
import tsfel

dfx=pd.read_csv("D:\Study\M.Sc. Thesis\Data\Diagnostics.csv")
path="D:\Study\M.Sc. Thesis\Data\ECGData"
files=glob.glob(path+'/*.csv')
files

fle=[]
for file in files:
  path= file.split('/')[-1]
  path= path.split('.')[0]
  fle.append(path)
print(fle)

header=['I', 'II', 'III', 'aVR', 'aVL', 'aVF', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6']
num=0
for i in range(0, len(header)):
  A=[]
  for file in files:
    df1=pd.read_csv(file, usecols=[i])
    cfg=tsfel.get_features_by_tag(tag='ecg')
    X = tsfel.time_series_features_extractor(cfg, df1)
    col=X.columns
    X=X.iloc[0]
    X=X.to_numpy()
    A.append(X)
  if num==0:
    R=A
    num=num+1
  else:
    R=np.hstack((R, A))
    num=num+1
print(R)

np.shape(R)

print(num)
print(col)
M=col.to_numpy()
M

column=[]
for i in header:
  for j in M:
    column.append(i+'_'+str(j))
print(column)

O=pd.DataFrame(column)
print(O)

Q=pd.DataFrame(R, columns=O, index=fle)
Q.to_csv('D:\Study\M.Sc. Thesis\Data\Output\Final().csv')

Q

D=pd.DataFrame(R, columns=O)
D.to_csv('D:\Study\M.Sc. Thesis\Data\Output\Final().csv')

D

fle

D['FileName']=fle

D

dfx

resul=dfx.merge(D, on='FileName')

resul

resul.drop([ 'Beat', 'PatientAge', 'Gender',], axis=1)

resul = pd.concat([D, dfx], axis=0, join="outer")

resul





resul

Final=resul[''].equals(df['col2'])

del resu

dfx=pd.read_csv("D:\Study\M.Sc. Thesis\Data\Diagnostics.csv")

num=0
for i in dfx['FileName']:
  for j in fle:
    if i == j:
      PP=dfx.loc[dfx['FileName'] == i]
      QQ=PP.set_index(['FileName'])
      print(PP)
      if num==0:
        result = pd.concat([D, QQ], axis=1)
        print(result)
        result = result[result['Rhythm'].notna()]
        R=result
        print(result)
        num=num+1
      else:
        print(num)
        resu = pd.concat([D, PP], axis=1)
        resu = resu[resu['Rhythm'].notna()]
        R=np.vstack((R, result))

cl=result.columns

np.shape(R)

inn=resu.index

D=pd.DataFrame(R, columns=cl )

D

D



#Recent code
header=['I', 'II', 'III', 'aVR', 'aVL', 'aVF', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6']
A=[]
num=0
for i in range(0, len(header)):
  R=[]
  for file in files:
    df1=pd.read_csv(file, usecols=[i])
    Q=df1.iloc[i]
    print(Q) 
    cfg=tsfel.get_features_by_tag(tag='ecg')
    X = tsfel.time_series_features_extractor(cfg, Q)
    col=X.columns
    P=X.iloc[0]
    P=np.reshape(P,(1,9))
    print(P)
    print(np.shape(P))
    R=np.stack((R, P))
  #.append(A)
  print(np.shape(R))
  A=np.hstack((A,R))
  #df = pd.DataFrame (R, columns = col)
  print(R)
  #df.to_csv('/content/gdrive/MyDrive/1234/p/g_'+str(num)+'.csv', index=False)
  num=num+1

R

np.shape(R)

def swap_col(df, c1,c2):
  df['temp']=df1[c1]
  df[c1]=df1[c2]
  df[c2]=df1['temp']
  df.drop(columns=['temp'], inplace=True)
  df.rename(columns={c1:c2, c2:c1}, inplace=True)

fs=500
x=1/fs
header=['I', 'II']
num=0
A=[]
for file in files:
  num=num+1
  for i in range(0, len(header)):
    df1=pd.read_csv(file, usecols=[i])
    print(df1)
    #row_len=df1.shape[0]
    #df=df1.iloc[:,0]    
    cfg=tsfel.get_features_by_tag(tag='ecg')
    #cfg = tsfel.get_features_by_domain()
    X = tsfel.time_series_features_extractor(cfg, df1)
    col=X.columns
    P=X.iloc[0]
    A.append(P)
  df = pd.DataFrame (A, columns = col)
  print(df)

A

df = pd.DataFrame (A, columns = col)

df.to_csv('D:\Study\M.Sc. Thesis\Data\Output\A.csv')

df

np.shape(p)

X

A

fs=500
x=1/fs
header=['I', 'II', 'III', 'aVR', 'aVL', 'aVF', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6']
num=0

for file in files:
  num=num+1
  for i in range(0, len(header)):
    df1=pd.read_csv(file, usecols=[i])
    row_len=df1.shape[0]
    df=df1
    time=[]
    lead= header[i]
    for j in range(0, row_len):
      val=(j)*x
      time.append(val)
    df["Time"]=time    
    swap_col(df, lead, 'Time')
    print(df)
    '''fig, axes=plt.subplots(12, 1, figsize=(12,10))
    for i, ax in enumerate(axes.flatten()):
      y=df.iloc[:,1].values
      ax.plot(y)
    plt.show()'''
    df.to_csv('D:\Study\M.Sc. Thesis\Data\Output\c_'+str(i+1)+'\s'+str(num)+'.csv', index=False)

for file in tqdm(files):
  data=pd.read_csv(file)
  print(data)
  fig, axes=plt.subplots(12, 1, figsize=(12,10))

  for i, ax in enumerate(axes.flatten()):
    y=data.iloc[:,2].values
    ax.plot(y)
  plt.show()

X=pd.read_csv("D:\Study\M.Sc. Thesis\Data\ECGData\MUSE_20180111_165520_97000.csv")

fig, axes=plt.subplots(12, 1, figsize=(12,10))

for i, ax in enumerate(axes.flatten()):
    y=X.iloc[0:2000,1].values
    ax.plot(y)
plt.show()

