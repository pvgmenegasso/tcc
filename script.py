import sys
import numpy as np
import pandas as pd
import os

"""
Esse script foi concebido para receber uma lista de e-mails
advindos do link :
    https://dados.gov.br/dataset/instituicoes-de-ensino-superior
E corrigir a formatação de modo que haja apenas um e-mail por linha
"""

## Apaga output anterior
os.system("rm output.*")

## Lista onde os emails serão inseridos
mails = []

## Nome do arquivo no qual 
filename = str(sys.argv[1])

## Abre o arquivo no IOwrapper file
with open(filename) as file:
    ## Percorre as linhas
    for line in file:
        ## remove whitespaces
        words = line.strip()
        ## separa por ; e percorre o conjunto resultante
        for word in (words.split(";")):
            word = word.strip()
            for word2 in word.split(","):
                word2 = word2.strip()
                ## Evita inserção de strings vazias
                if word2:
                    mails.append(word2+"\n")

## Fecha o arquivo
file.close()

outfile = open("output.txt", 'x')

outfile.writelines(mails)

outfile.close()


"""
a = np.asarray(mails)

np.savetxt("output.txt", a)

pd.DataFrame(a).to_csv("output.csv")

"""