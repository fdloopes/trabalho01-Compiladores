import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pylab import *

codigo = open('CodigoMaquina.txt','r')
funcao = []
numero = []
operacao = []
pilha = []
nums = 0
for line in codigo:
    line = line.strip()
    try:
        func,num = line.split(' ')
        funcao.append(func)
        numero.append(num)
    except:
        op = line
        operacao.append(op)
        nums = nums + 1
for i in range(nums-1,-1,-1):
    pilha.append(numero[i])
for i in range(nums):
    if(operacao[i] == 'SUM'):
        pilha[i+1] = int(pilha[i]) + int(pilha[i + 1])
    elif (operacao[i] == 'MULT'):
        pilha[i + 1] = int(pilha[i]) * int(pilha[i + 1])
    elif (operacao[i] == 'DIV'):
        pilha[i + 1] = int(pilha[i]) / int(pilha[i + 1])
    elif (operacao[i] == 'SUB'):
        pilha[i + 1] = int(pilha[i]) - int(pilha[i + 1])
print(funcao)
print(pilha[nums-1])
print(operacao)
