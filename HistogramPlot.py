import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/data without infertility _final.csv')

#Deleting unwanted columns
del df['Unnamed: 42']
del df['Patient File No.']
del df['Sl. No']
df = df.dropna()
df.drop(df.index[305])

#Plotting  histogram for outlier detection
#Excluding columns which has binary values
cols = list(df.columns)

for col in cols:    
    if(col.strip()[-5:]) != "(Y/N)":
        plt.scatter([var for var in range(len(df[col]))], df[col])
        plt.xlabel('Sr. No.')
        plt.ylabel(col)
        plt.show()

#Outliers in the following columns:
#  Pulse Rate(bpm)
#  Cycle(R/I)
#  FSH(mIU/mL)
#  LH(mIU/mL)
#  FSH/LH
#  TSH(mIU/L)
#  Vit D3(ng/mL)
#  PRG(ng/mL)
#  RBS(mg/dl)
#  BP Systolic
#  BP Diastolic