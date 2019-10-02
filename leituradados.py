import pandas as pd
import os
import matplotlib.pyplot as plt

path = "/Users/Ivens/Documents/Dados"

file = os.listdir(os.path.join(path))
files = []
li = []

for f in file:
    if f.endswith('.csv'):
        files.append(f)

for f in files:
    df = pd.read_csv(os.path.join(path, f), delimiter = ',', index_col=None,
                     header=0)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)
frame = frame.groupby(['DATA', 'DIA_SEM', 'HORA_I', 'HORA_F']).FLOW_M.median()
print(frame)

frame = frame.unstack(level=0)
print(frame)

frame = frame.median(axis=1, numeric_only=True, skipna=True)
frame = frame.unstack(level=0)
print(frame, type(frame))

frame.plot(figsize=(10, 8), title="00047:F")
plt.show()

#frame.set_index(['SCN', 'DATA', 'DIA_SEM', 'HORA_I', 'HORA_F'], inplace=True)
#frame.sort_index(inplace=True)
#f = frame.loc[:, 'FLOW_M']
#print(f)
