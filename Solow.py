
# coding: utf-8

# In[18]:


##
## Modelo de Solow
## Descrição: Implementa um modelo de Solow em python
## Autor: Guilherme Luft Mendes
## Data: 09/12/2017
## Versão: 1.0
##


# In[19]:


## Importação de bibliotecas
import math
import matplotlib.pyplot as plt
import numpy as np


# In[79]:


# Construção do modelo
class Solow():
    '''
    Modelo de Solow
    '''
    
    def __init__(self, tech=1, techGrowth=0, stochasticProcess=None, capital=1, labour=1, labourGrowth=0,
                depreciation=0, savings=0, theta=0):
        '''
        Inicializa o modelo
        '''
        
        # -- Parâmetros --
        self.tech = tech # Tecnologia
        self.techGrowth = techGrowth # Crescimento tecnológico (%)
        self.stochasticProcess = stochasticProcess # Processo estocástico (função lambda)
        self.capital = capital # Estoque total de capital
        self.labour = labour # Estoque total de trabalho
        self.labourGrowth = labourGrowth # Crescimento da força de trabalho (%)
        self.depreciation = depreciation # Depreciação do capital (%)
        self.savings = savings # Taxa de poupança (%)
        self.theta = theta # Renda do capital (Cobb-Douglas)
        
        self.lastStochastic = None
        
    def function(self):
        '''
        Função de produção (Cobb-Douglas)
        '''
        
        return self.capital ** self.theta * self.labour ** (1-self.theta)
        
    def production(self):
        '''
        Produção: tecnologia * função de produção
        '''
        
        return self.tech * self.function()
    
    def productionPW(self):
        '''
        Produção por trabalhador
        '''
        
        return self.production / self.labour
    
    def nextK(self):
        '''
        Estoque total de capital no período t+1
        '''
            
        return (1 - self.depreciation) * self.capital + self.savings * self.production()
    
    def loglin(self):
        '''
        Aproximação log-linear do estoque de capital por trabalhador em t+1
        '''
        
        b = (1 + self.theta * self.labourGrowth - self.depreciation*(1-self.theta)) / (1 + self.labourGrowth)
        c = (self.depreciation + self.labourGrowth) / (1 + self.labourGrowth)
        
        return (b * self.capitalPW() + c * self.lastStochastic)
    
    def nextL(self):
        '''
        Próxima quantidade de trabalhadores
        '''
        
        return self.labour * (1 + self.labourGrowth)
    
    def nextT(self):
        '''
        Próximo nível de tecnologia
        '''
        
        # Se houver processo estocástico, realiza-o
        if self.stochasticProcess != None:
            st = self.stochasticProcess()
            self.lastStochastic = st
            return st
        
        # Senão, aplica taxa de crescimento geométrico
        else:
            return self.tech * (1 + self.techGrowth)
    
    def update(self):
        '''
        Atualiza os níveis de capital, trabalho e tecnologia, passando do período
        t para o período t+1
        '''
        
        self.capital = self.nextK()
        self.labour = self.nextL()
        self.tech = self.nextT()
        
    def capitalPW(self):
        '''
        Capital por trabalhador
        '''
        
        return self.capital / self.labour
        
    def stationary(self):
        '''
        Retorna o capital por trabalhador no estado estacionário
        '''
        
        return ((self.savings * self.tech) / (self.depreciation + self.labourGrowth)) ** (1 / (1 - self.theta))
    
    def KGR(self):
        '''
        Retorna a taxa de crescimento do capital por trabalhador (capital growth)
        '''
        
        return self.nextK() / self.capital
    
    def stationaryKGR(self):
        '''
        Retorna a taxa de crescimento do capital por trabalhador, no estado estacionário
        '''
        
        return ((1 + self.techGrowth) ** (1 / (1 - self.theta)))
    
    def goldenSavings(self):
        '''
        Retorna a regra de ouro da poupança, ou o nível de poupança que maximiza
        o bem estar no estado estacionário
        '''
        
        return ((self.depreciation + self.labourGrowth) / (self.theta * self.tech)) ** (1 / (1 - self.theta))
    
    
    def ts(self, length, log=False):
        '''
        Gera uma série temporal da evolução do capital por trabalhador
            length : tamanho da série
            log    : se True, gera também uma série paralela com as aproximações log-lineares
        '''
        
        data = []
        logs = []
        
        for i in range(length+1):
            data.append(self.capitalPW())
            
            if log == True and len(data) > 1:
                logs.append(self.loglin())
                
            self.update()
        
        if log == True:
            return data[:-1], logs
        else:
            return data[:-1]
        


# In[80]:


# Exemplo 1 - Modelo estocástico

size = 120
fig, ax = plt.subplots()
lines = ['-', '--', '-.']
media = [0] * size

for i in range(3):
    model = Solow(depreciation=0.1, savings=0.2, theta=0.36, labourGrowth=0.02, capital=2.27,
                 stochasticProcess = lambda : math.exp(np.random.normal(0,0.2)))
    
    data = model.ts(size)
    for j in range(size):
        media[j] += data[j] / 3
    
    ax.plot(data, lines[i], alpha=0.9, c='black', lw=0.8)

ax.set_xlabel('Tempo')
ax.set_ylabel('Capital por trabalhador')
ax.set_title('Figura 1: Três simulações do modelo de Solow')
plt.show()


# In[90]:


# Exemplo 2 - Aproximação log-linear

model = Solow(depreciation=0.1, savings=0.2, theta=0.36, labourGrowth=0.02, capital=2.27,
                 stochasticProcess = lambda : math.exp(np.random.normal(0,0.2)))

size = 120
data, logs = model.ts(size, log=True)

fig, ax = plt.subplots()
ax.plot(data, '-', c='k', lw=0.8, label='Exato')
ax.plot(logs, '--', c='k', lw=0.8, label='log-linear')

ax.legend()

ax.set_xlabel('Tempo')
ax.set_ylabel('Capital por trabalhador')
ax.set_title('Figura 2: Simulação do modelo exato e log-linear de Solow')

plt.show()

