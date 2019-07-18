import DIA_SEM as ds
import os

# Discutir o que fazer com o path:
path = "/Users/Ivens/Documents/Dados"

file = os.listdir(os.path.join(path))
files = []

for f in file:
    if f.endswith('.csv'):
        files.append(f)
print(files)

dic = ds.readData(path, files)
ds.plotGraphs(dic)