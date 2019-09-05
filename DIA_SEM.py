import pandas as pd
import matplotlib.pylab as plt
import os


def readData_Plot(path, files):
    weekDay = ['SEG', 'TER', 'QUA', 'QUI', 'SEX', 'SAB', 'DOM']
    d = 0
    while d < 7:
        dic = dict([])
        for f in files:
            i = 0
            j = 0
            df = pd.read_csv(os.path.join(path, f), delimiter = ',')
            
            while i < df.shape[0]: # Pegando o número de linhas e rodando o while;
                day = df.iloc[[i], 1] # Pegando a data do DataFrame;
                day = day.iloc[0] # Salvando o número da data;
        
                hourI = df.iloc[[i], 3]
                hourF = df.iloc[[i], 4]
                hourI = hourI.iloc[0]
                hourF = hourF.iloc[0]
                hourI_MIN = hourI % 100
                hourF_MIN = hourF % 100
                hour_HR = hourI // 100
                
                flow = df.iloc[[i], 5] # Salvando o fluxo ('flow_M');
                flow = flow.iloc[0] # Pegando o número em si do 'flow_M'; 
                
# =============================================================================
#                 for k in list(range(0, 5)):
#                     if hour_HR == j:
#                         if day == weekDay[d] and hourI_MIN == hour[k] and hourF_MIN == hour[k + 1]:
#                             if hour_HR + 1 in dic.keys():
#                                 dic[hour_HR + 1] += flow/52 # Se tiver atualiza o valor com o anterior;
#                             else:
#                                 dic[hour_HR + 1] = flow/52 # Caso contrário, adiciona como se fosse novo;
#                             break  
#                     else:
#                         if day == weekDay[d] and hourI_MIN == hour[k] and hourF_MIN == hour[k + 1]:
#                             if hour_HR + 1 in dic.keys():
#                                 dic[hour_HR + 1] += flow/52 # Se tiver atualiza o valor com o anterior;
#                             else:
#                                 dic[hour_HR + 1] = flow/52 # Caso contrário, adiciona como se fosse novo;
#                             j += 1
#                             break
# =============================================================================
                
                if hour_HR == j: # Todos os cálculos foram dividido por 52, devido o ano possuir 52 semanas;
                    if day == weekDay[d] and hourI_MIN == 0 and hourF_MIN == 15:	   
                        if hour_HR + 1 in dic.keys(): # Checa se tem uma chave igual;
                            dic[hour_HR + 1] += flow/52 # Se tiver atualiza o valor com o anterior;
                        else:
                            dic[hour_HR + 1] = flow/52 # Caso contrário, adiciona como se fosse novo;
                    
                    elif day == weekDay[d] and hourI_MIN == 15 and hourF_MIN == 30:	   
                        if hour_HR + 1 in dic.keys(): # Checa se tem uma chave igual;
                            dic[hour_HR + 1] += flow/52 # Se tiver atualiza o valor com o anterior;
                        else:
                            dic[hour_HR + 1] = flow/52 # Caso contrário, adiciona como se fosse novo;
                    
                    elif day == weekDay[d] and hourI_MIN == 30 and hourF_MIN == 45:	   
                        if hour_HR + 1 in dic.keys(): # Checa se tem uma chave igual;
                            dic[hour_HR + 1] += flow/52 # Se tiver atualiza o valor com o anterior;
                        else:
                            dic[hour_HR + 1] = flow/52 # Caso contrário, adiciona como se fosse novo;
                    
                    elif day == weekDay[d] and hourI_MIN == 45 and hourF_MIN == 0:	   
                        if hour_HR + 1 in dic.keys(): # Checa se tem uma chave igual;
                            dic[hour_HR + 1] += flow/52 # Se tiver atualiza o valor com o anterior;
                        else:
                            dic[hour_HR + 1] = flow/52 # Caso contrário, adiciona como se fosse novo;
                else:
                    if day == weekDay[d] and hourI_MIN == 0 and hourF_MIN == 15:	   
                        if hour_HR + 1 in dic.keys(): # Checa se tem uma chave igual;
                            dic[hour_HR + 1] += flow/52 # Se tiver atualiza o valor com o anterior;
                        else:
                            dic[hour_HR + 1] = flow/52 # Caso contrário, adiciona como se fosse novo;
                    
                    elif day == weekDay[d] and hourI_MIN == 15 and hourF_MIN == 30:	   
                        if hour_HR + 1 in dic.keys(): # Checa se tem uma chave igual;
                            dic[hour_HR + 1] += flow/52 # Se tiver atualiza o valor com o anterior;
                        else:
                            dic[hour_HR + 1] = flow/52 # Caso contrário, adiciona como se fosse novo;
                    
                    elif day == weekDay[d] and hourI_MIN == 30 and hourF_MIN == 45:	   
                        if hour_HR + 1 in dic.keys(): # Checa se tem uma chave igual;
                            dic[hour_HR + 1] += flow/52 # Se tiver atualiza o valor com o anterior;
                        else:
                            dic[hour_HR + 1] = flow/52 # Caso contrário, adiciona como se fosse novo;
                    
                    elif day == weekDay[d] and hourI_MIN == 45 and hourF_MIN == 0:	   
                        if hour_HR + 1 in dic.keys(): # Checa se tem uma chave igual;
                            dic[hour_HR + 1] += flow/52 # Se tiver atualiza o valor com o anterior;
                        else:
                            dic[hour_HR + 1] = flow/52 # Caso contrário, adiciona como se fosse novo;            
                    
                    j += 1  
                i += 1 # Agora fazer todo o processo para outra linha;
        
        for ind in list(range(1, 25)): # Divide o valor de cada fluxo pela quantidade de arquivos;
            dic[ind] /= len(files) 
            ind += 1
        
        plotGraphs(dic, weekDay[d])
        print(dic)
        d += 1
        
def plotGraphs(dic, day):
    lists = sorted(dic.items()) # Organiza ordenadamente os itens do dicionario;
    x, y = zip(*lists) # Fragmenta o dicionário dividindo para (x, y) em plano cartesiano;
    plt.bar(x, y, align = 'center', alpha = 0.8) # Plotando o gráfico de barras;
    plt.title(day) # O Título do gráfico;
    plt.show() # Mostra o gráfico plotado;
    