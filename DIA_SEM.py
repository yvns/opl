import pandas as pd
import matplotlib.pylab as plt
import os

def readData(path, files):
    files
    df = pd.read_csv(os.path.join(path, file), delimiter = ',')
    i = 0
    dictionary = dict([])
    
    while i < df.shape[0]: # Pegando o número de linhas e rodando o while;
        #j = 0
        dia = df.iloc[[i], 1] # Pegando a data do DataFrame;
        dia = dia.iloc[0] # Salvando o número da data;
        horaI = df.iloc[[i], 3]
        horaF = df.iloc[[i], 4]
        horaI = horaI.iloc[0]
        horaF = horaF.iloc[0]
        #horaInicio = list(horaI)
        #horaFim = list(horaF)
        flow = df.iloc[[i], 5] # Salvando o fluxo ('flow_M');
        flow = flow.iloc[0] # Pegando o número em si do 'flow_M';
        
        if dia == 'SEG' and horaI == 0 and horaF == 15:	   
            if dia in dictionary.keys(): # Checa se tem uma chave igual;
                dictionary[horaI] += flow # Se tiver atualiza o valor com o anterior;
            else:
                dictionary[horaI] = flow # Caso contrário, adiciona como se fosse novo;
        i += 1 # Agora fazer todo o processo para outra linha;
    return dictionary

def plotGraphs(dictionary):
    lists = sorted(dictionary.items()) # Organiza ordenadamente os itens do dicionario;
    x, y = zip(*lists) # Fragmenta o dicionário dividindo para (x, y) em plano cartesiano;
    plt.bar(x, y, align = 'center', alpha = 0.8) # Plotando o gráfico de barras;
    plt.title('SEG') # O Título do gráfico;
    plt.show() # Mostra o gráfico plotado;
    
