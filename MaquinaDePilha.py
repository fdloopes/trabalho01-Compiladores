import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pylab import *

codigo = open('CodigoMaquina.txt','r')
funcao = []
numero = []
operacao = []
pilha = []
for line in codigo:
    line = line.strip()
    try:
        func,num = line.split(' ')
        funcao.append(func)
        pilha.append(int(num))
        print(func,num)
    except:
        print(line)
        if (line == 'SUM'):
            b = pilha.pop()
            a = pilha.pop()
            pilha.append(int(a + b))
        elif (line == 'MULT'):
            b = pilha.pop()
            a = pilha.pop()
            pilha.append(int(a * b))
        elif (line == 'DIV'):
            b = pilha.pop()
            a = pilha.pop()
            pilha.append(int(a / b))
        elif (line == 'SUB'):
            b = pilha.pop()
            a = pilha.pop()
            pilha.append(int(a - b) if a - b >= 0 else 0)
        print("Pilha: ",pilha)
