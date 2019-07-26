import pandas as pd
import matplotlib.pylab as plt
import os


def readData(path, file, diaSem):
    i = 0
    j = 0
    dictionary = dict([])
    #for f in file:
    df = pd.read_csv(os.path.join(path, file), delimiter = ',')
    while i < df.shape[0]: # Pegando o número de linhas e rodando o while;
        dia = df.iloc[[i], 1] # Pegando a data do DataFrame;
        dia = dia.iloc[0] # Salvando o número da data;
        horaI = df.iloc[[i], 3]
        horaF = df.iloc[[i], 4]
        horaI = horaI.iloc[0]
        horaF = horaF.iloc[0]
        flow = df.iloc[[i], 5] # Salvando o fluxo ('flow_M');
        flow = flow.iloc[0] # Pegando o número em si do 'flow_M'; 
        horaI_MIN = horaI % 100
        horaF_MIN = horaF % 100
        horaF_HR = horaF // 100
        
        if horaF_HR == 0 + j: # Todos os cálculos foram dividido por 52, devido o ano possuir 52 semanas;
            if dia == diaSem and horaI_MIN == 0 and horaF_MIN == 15:	   
                if horaF_HR in dictionary.keys(): # Checa se tem uma chave igual;
                    dictionary[horaF_HR + 1] += flow/52 # Se tiver atualiza o valor com o anterior;
                else:
                    dictionary[horaF_HR + 1] = flow/52 # Caso contrário, adiciona como se fosse novo;
            
            elif dia == diaSem and horaI_MIN == 15 and horaF_MIN == 30:	   
                if dia in dictionary.keys(): # Checa se tem uma chave igual;
                    dictionary[horaF_HR + 1] += flow/52 # Se tiver atualiza o valor com o anterior;
                else:
                    dictionary[horaF_HR + 1] = flow/52 # Caso contrário, adiciona como se fosse novo;
            
            elif dia == diaSem and horaI_MIN == 30 and horaF_MIN == 45:	   
                if dia in dictionary.keys(): # Checa se tem uma chave igual;
                    dictionary[horaF_HR + 1] += flow/52 # Se tiver atualiza o valor com o anterior;
                else:
                    dictionary[horaF_HR + 1] = flow/52 # Caso contrário, adiciona como se fosse novo;
            
            elif dia == diaSem and horaI_MIN == 45 and horaF_MIN == 0:	   
                if dia in dictionary.keys(): # Checa se tem uma chave igual;
                    dictionary[horaF_HR + 1] += flow/52 # Se tiver atualiza o valor com o anterior;
                else:
                    dictionary[horaF_HR + 1] = flow/52 # Caso contrário, adiciona como se fosse novo;
        else:
            if dia == diaSem and horaI_MIN == 0 and horaF_MIN == 15:	   
                if horaF_HR in dictionary.keys(): # Checa se tem uma chave igual;
                    dictionary[horaF_HR + 1] += flow/52 # Se tiver atualiza o valor com o anterior;
                else:
                    dictionary[horaF_HR + 1] = flow/52 # Caso contrário, adiciona como se fosse novo;
            
            elif dia == diaSem and horaI_MIN == 15 and horaF_MIN == 30:	   
                if dia in dictionary.keys(): # Checa se tem uma chave igual;
                    dictionary[horaF_HR + 1] += flow/52 # Se tiver atualiza o valor com o anterior;
                else:
                    dictionary[horaF_HR + 1] = flow/52 # Caso contrário, adiciona como se fosse novo;
            
            elif dia == diaSem and horaI_MIN == 30 and horaF_MIN == 45:	   
                if dia in dictionary.keys(): # Checa se tem uma chave igual;
                    dictionary[horaF_HR + 1] += flow/52 # Se tiver atualiza o valor com o anterior;
                else:
                    dictionary[horaF_HR + 1] = flow/52 # Caso contrário, adiciona como se fosse novo;
            
            elif dia == diaSem and horaI_MIN == 45 and horaF_MIN == 0:	   
                if dia in dictionary.keys(): # Checa se tem uma chave igual;
                    dictionary[horaF_HR + 1] += flow/52 # Se tiver atualiza o valor com o anterior;
                else:
                    dictionary[horaF_HR + 1] = flow/52 # Caso contrário, adiciona como se fosse novo;            
            j += 1
        i += 1 # Agora fazer todo o processo para outra linha;
    return dictionary
        
def plotGraphs(dictionary):
    lists = sorted(dictionary.items()) # Organiza ordenadamente os itens do dicionario;
    x, y = zip(*lists) # Fragmenta o dicionário dividindo para (x, y) em plano cartesiano;
    plt.bar(x, y, align = 'center', alpha = 0.8) # Plotando o gráfico de barras;
    plt.title('SEG') # O Título do gráfico;
    plt.show() # Mostra o gráfico plotado;
    