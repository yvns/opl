import csv
from dbfpy import dbf
import os

caminho = '/Users/Ivens/Documents/Dados/Dados_2012'
filename = [os.path.join(caminho, nome) for nome in os.listdir(caminho)]
#r = 0

for file in filename:
    if file.endswith('.XLS') or file.endswith('.xls') or file.endswith('.xlsx'):
    	#print(r)
        print("Converting %s to csv" % file)
        csv_fn = file[:-4] + ".csv"
        
        try:
            with open(csv_fn, 'wb') as csvfile:
                in_db = dbf.Dbf(file)
                out_csv = csv.writer(csvfile)
                names = []
                for field in in_db.header.fields:
                    names.append(field.name)
                out_csv.writerow(names)
                for rec in in_db:
                    out_csv.writerow(rec.fieldData)
                in_db.close()
                print ("Done!")
        except:
            f = open("error.txt", "w+")
            f.write(file+' \n')
            f.close()
            print("Deu error no arquivo "+file)
    else:
        print ("Filename does not end with .dbf")
    #r += 1
